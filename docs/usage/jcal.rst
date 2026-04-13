jCal syntax highlighting
========================

The extension also registers ``jcal`` (and ``jcalendar``) as language aliases that apply JSON highlighting to raw jCal snippets without triggering the calendar rendering:

.. code-block:: rst

    .. code-block:: jcal

        ["vcalendar",
          [["version", {}, "text", "2.0"]],
          [["vevent",
            [
              ["summary",  {}, "text",      "Quarterly review"],
              ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
              ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
            ], []
          ]]
        ]

The result is a static, JSON-highlighted code block:

.. code-block:: jcal

    ["vcalendar",
      [["version", {}, "text", "2.0"]],
      [["vevent",
        [
          ["summary",  {}, "text",      "Quarterly review"],
          ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
          ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
        ], []
      ]]
    ]

The highlighting is provided by Pygments' built-in JSON lexer.

Options
-------

``jcal`` supports the ``linenos`` and ``emphasize-lines`` options, just like any
other ``.. code-block::`` language:

.. code-block:: rst

    .. code-block:: jcal
       :linenos:
       :emphasize-lines: 5, 6

        ["vcalendar",
          [["version", {}, "text", "2.0"]],
          [["vevent",
            [
              ["summary",  {}, "text",      "Quarterly review"],
              ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
              ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
            ], []
          ]]
        ]

.. code-block:: jcal
   :linenos:
   :emphasize-lines: 5, 6

    ["vcalendar",
      [["version", {}, "text", "2.0"]],
      [["vevent",
        [
          ["summary",  {}, "text",      "Quarterly review"],
          ["dtstart",  {}, "date-time", "2026-04-01T09:00:00Z"],
          ["dtend",    {}, "date-time", "2026-04-01T10:00:00Z"]
        ], []
      ]]
    ]
