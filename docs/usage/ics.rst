ICS syntax highlighting
=======================

The extension also registers an ``ics`` (and ``icalendar``) language alias for Pygments so you can highlight raw ICS snippets in ordinary code blocks without triggering the calendar rendering:

.. code-block:: rst

    .. code-block:: ics

        BEGIN:VCALENDAR
        BEGIN:VEVENT
        DTSTART;TZID="America/New_York":20260401T090000
        DTEND;TZID="America/New_York":20260401T100000
        SUMMARY:Quarterly review
        END:VEVENT
        END:VCALENDAR

The result is a static, highlighted code block:

.. code-block:: ics

    BEGIN:VCALENDAR
    BEGIN:VEVENT
    DTSTART;TZID="America/New_York":20260401T090000
    DTEND;TZID="America/New_York":20260401T100000
    SUMMARY:Quarterly review
    END:VEVENT
    END:VCALENDAR

Options
-------

``ics`` supports the ``linenos`` and ``emphasize-lines`` options, just like any
other ``.. code-block::`` language:

.. code-block:: rst

    .. code-block:: ics
       :linenos:
       :emphasize-lines: 3, 5

        BEGIN:VCALENDAR
        BEGIN:VEVENT
        DTSTART;TZID="America/New_York":20260401T090000
        DTEND;TZID="America/New_York":20260401T100000
        SUMMARY:Quarterly review
        END:VEVENT
        END:VCALENDAR

.. code-block:: ics
   :linenos:
   :emphasize-lines: 3, 5

    BEGIN:VCALENDAR
    BEGIN:VEVENT
    DTSTART;TZID="America/New_York":20260401T090000
    DTEND;TZID="America/New_York":20260401T100000
    SUMMARY:Quarterly review
    END:VEVENT
    END:VCALENDAR
