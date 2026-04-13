"""Tests for sphinx_icalendar._setup (get_lexers, setup metadata)."""

from __future__ import annotations

from sphinx_icalendar._lexer import ICalendarLexer, JCalLexer
from sphinx_icalendar._setup import get_lexers


def test_get_lexers_returns_all_aliases():
    lexers = get_lexers()
    assert set(lexers) == {"ics", "icalendar", "jcal", "jcalendar"}


def test_get_lexers_ics_is_icalendar_lexer():
    assert get_lexers()["ics"] is ICalendarLexer


def test_get_lexers_icalendar_is_icalendar_lexer():
    assert get_lexers()["icalendar"] is ICalendarLexer


def test_get_lexers_jcal_is_jcal_lexer():
    assert get_lexers()["jcal"] is JCalLexer


def test_get_lexers_jcalendar_is_jcal_lexer():
    assert get_lexers()["jcalendar"] is JCalLexer
