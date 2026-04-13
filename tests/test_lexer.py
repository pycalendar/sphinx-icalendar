"""Tests for sphinx_icalendar._lexer (ICalendarLexer, JCalLexer)."""

from __future__ import annotations

from pygments.token import Token

from sphinx_icalendar._lexer import ICalendarLexer, JCalLexer


# ── ICalendarLexer ────────────────────────────────────────────────────────────


def test_icalendar_lexer_aliases():
    assert "ics" in ICalendarLexer.aliases
    assert "icalendar" in ICalendarLexer.aliases


def test_icalendar_lexer_filenames():
    assert "*.ics" in ICalendarLexer.filenames


ICS_SNIPPET = """\
BEGIN:VCALENDAR
DTSTART:20260301T090000Z
SUMMARY:Hello world
END:VCALENDAR
"""


def test_icalendar_lexer_tokenises_begin_end():
    lexer = ICalendarLexer()
    tokens = list(lexer.get_tokens(ICS_SNIPPET))
    token_types = {t for t, _ in tokens}
    # BEGIN/END lines → Name.Tag
    assert Token.Name.Tag in token_types


def test_icalendar_lexer_tokenises_property_name():
    lexer = ICalendarLexer()
    tokens = list(lexer.get_tokens(ICS_SNIPPET))
    token_types = {t for t, _ in tokens}
    # DTSTART → Keyword
    assert Token.Keyword in token_types


def test_icalendar_lexer_tokenises_datetime():
    lexer = ICalendarLexer()
    tokens = list(lexer.get_tokens(ICS_SNIPPET))
    token_types = {t for t, _ in tokens}
    assert Token.Literal.Date in token_types


# ── JCalLexer ─────────────────────────────────────────────────────────────────


def test_jcal_lexer_aliases():
    assert "jcal" in JCalLexer.aliases
    assert "jcalendar" in JCalLexer.aliases


def test_jcal_lexer_produces_tokens():
    lexer = JCalLexer()
    tokens = list(lexer.get_tokens('["vcalendar", [], []]'))
    assert tokens  # non-empty
