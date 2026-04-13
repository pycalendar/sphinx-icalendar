"""Tests for sphinx_icalendar._visitors (pure helper functions)."""

from __future__ import annotations

from datetime import date, datetime, timezone

import pytest
from icalendar import Calendar

from sphinx_icalendar._visitors import _fmt_dt, _render_table, _tab_id, pretty_jcal


# ── _fmt_dt ───────────────────────────────────────────────────────────────────


def test_fmt_dt_none_returns_empty():
    assert _fmt_dt(None) == ""


def test_fmt_dt_date_only():
    assert _fmt_dt(date(2026, 3, 1)) == "2026-03-01"


def test_fmt_dt_datetime_utc():
    dt = datetime(2026, 3, 1, 9, 0, 0, tzinfo=timezone.utc)
    result = _fmt_dt(dt)
    assert result.startswith("2026-03-01 09:00")


# ── _tab_id ───────────────────────────────────────────────────────────────────


def test_tab_id_length():
    assert len(_tab_id("hello")) == 8


def test_tab_id_deterministic():
    assert _tab_id("same") == _tab_id("same")


def test_tab_id_differs_for_different_sources():
    assert _tab_id("source-a") != _tab_id("source-b")


# ── _render_table ─────────────────────────────────────────────────────────────

ICS_SINGLE_EVENT = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
BEGIN:VEVENT
SUMMARY:Team standup
DTSTART:20260301T090000Z
DTEND:20260301T100000Z
UID:standup-001@test
END:VEVENT
END:VCALENDAR
"""

ICS_NAMED_CAL = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
X-WR-CALNAME:My Calendar
X-WR-CALDESC:A short description
BEGIN:VEVENT
SUMMARY:Kickoff
DTSTART:20260301T090000Z
DTEND:20260301T100000Z
UID:kickoff-001@test
END:VEVENT
END:VCALENDAR
"""

ICS_EMPTY = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
END:VCALENDAR
"""


def _parse(ics: str):
    import recurring_ical_events

    cal = Calendar.from_ical(ics)
    occurrences = recurring_ical_events.of(cal).all()
    return occurrences, cal


def test_render_table_contains_summary():
    occurrences, cal = _parse(ICS_SINGLE_EVENT)
    html = _render_table(occurrences, cal)
    assert "Team standup" in html


def test_render_table_has_thead():
    occurrences, cal = _parse(ICS_SINGLE_EVENT)
    html = _render_table(occurrences, cal)
    assert "<thead>" in html
    assert "Summary" in html
    assert "Start" in html
    assert "End" in html


def test_render_table_named_calendar_has_caption():
    occurrences, cal = _parse(ICS_NAMED_CAL)
    html = _render_table(occurrences, cal)
    assert "<caption>My Calendar</caption>" in html


def test_render_table_named_calendar_has_description():
    occurrences, cal = _parse(ICS_NAMED_CAL)
    html = _render_table(occurrences, cal)
    assert "A short description" in html


def test_render_table_empty_calendar_shows_no_events():
    occurrences, cal = _parse(ICS_EMPTY)
    html = _render_table(occurrences, cal)
    assert "No events found" in html


def test_render_table_escapes_html_in_summary():
    ics = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
BEGIN:VEVENT
SUMMARY:<script>alert(1)</script>
DTSTART:20260301T090000Z
DTEND:20260301T100000Z
UID:xss-001@test
END:VEVENT
END:VCALENDAR
"""
    occurrences, cal = _parse(ics)
    html = _render_table(occurrences, cal)
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


# ── pretty_jcal ───────────────────────────────────────────────────────────────

JCAL_SIMPLE = ["vcalendar", [["version", {}, "text", "2.0"]], []]


def test_pretty_jcal_returns_string():
    result = pretty_jcal(JCAL_SIMPLE)
    assert isinstance(result, str)


def test_pretty_jcal_contains_name():
    result = pretty_jcal(JCAL_SIMPLE)
    assert "vcalendar" in result


def test_pretty_jcal_rejects_non_list():
    with pytest.raises(TypeError):
        pretty_jcal("not a list")  # type: ignore[arg-type]
