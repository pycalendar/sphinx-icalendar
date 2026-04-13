"""Tests for sphinx_icalendar._transform (CalendarTransform)."""

from __future__ import annotations

from docutils import nodes
from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser
from docutils.utils import new_document

from sphinx_icalendar._nodes import calendar_block
from sphinx_icalendar._transform import CalendarTransform


ICS_SOURCE = """\
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
BEGIN:VEVENT
SUMMARY:Demo event
DTSTART:20260301T090000Z
DTEND:20260301T100000Z
UID:demo-001@test
END:VEVENT
END:VCALENDAR
"""


def _make_document() -> nodes.document:
    settings = OptionParser(components=(Parser,)).get_default_values()
    return new_document("<test>", settings)


def _apply_transform(document: nodes.document) -> None:
    transform = CalendarTransform(document)
    transform.apply()


def test_calendar_block_replaces_calendar_code_block():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    document += block

    _apply_transform(document)

    result = list(document.findall(calendar_block))
    assert len(result) == 1
    assert result[0]["ical_source"] == ICS_SOURCE


def test_non_calendar_code_block_is_left_alone():
    document = _make_document()
    block = nodes.literal_block("print('hi')", "print('hi')")
    block["language"] = "python"
    document += block

    _apply_transform(document)

    assert not list(document.findall(calendar_block))
    assert len(list(document.findall(nodes.literal_block))) == 1


def test_calendar_block_stores_ical_source():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    document += block

    _apply_transform(document)

    [node] = document.findall(calendar_block)
    assert node["ical_source"] == ICS_SOURCE


def test_linenos_forwarded_to_calendar_block():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    block["linenos"] = True
    document += block

    _apply_transform(document)

    [node] = document.findall(calendar_block)
    assert node["linenos"] is True


def test_emphasize_lines_forwarded_to_calendar_block():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    block["highlight_args"] = {"hl_lines": [1, 3]}
    document += block

    _apply_transform(document)

    [node] = document.findall(calendar_block)
    assert node["highlight_args"] == {"hl_lines": [1, 3]}


def test_default_linenos_is_false():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    document += block

    _apply_transform(document)

    [node] = document.findall(calendar_block)
    assert not node["linenos"]


def test_default_highlight_args_is_empty():
    document = _make_document()
    block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
    block["language"] = "calendar"
    document += block

    _apply_transform(document)

    [node] = document.findall(calendar_block)
    assert node["highlight_args"] == {}


def test_multiple_calendar_blocks_all_replaced():
    document = _make_document()
    for _ in range(3):
        block = nodes.literal_block(ICS_SOURCE, ICS_SOURCE)
        block["language"] = "calendar"
        document += block

    _apply_transform(document)

    assert len(list(document.findall(calendar_block))) == 3
    assert not list(document.findall(nodes.literal_block))
