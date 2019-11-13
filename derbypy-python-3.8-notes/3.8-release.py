import sys
import os
import curses
from dataclasses import dataclass
from typing import Optional

@dataclass
class WindowContent:
    title: str
    subtitle: str
    content: str

def main_menu():
    return WindowContent("What's new in Python 3.8",
                         f"Alexander Hagerman DerbyPy November 2019",
                         """
                                    [1] walrus := assignment_expressions
                                    [2] from sys import audit
                                    [3] typing protocols
                                    [4] vectorcall
                                    [5] release notes
                                    [6] release schedule
                         """,
                         )

def window_one():
    return WindowContent("Assignment Expressions",
                         "Naming the result of expressions",
                         """
                            # Handle a matched regex
                            if (match := pattern.search(data)) is not None:
                                # Do something with match

                            # A loop that can't be trivially rewritten using 2-arg iter()
                            while chunk := file.read(8192):
                            process(chunk)

                            # Reuse a value that's expensive to compute
                            [y := f(x), y**2, y**3]

                            # Share a subexpression between a comprehension filter
                            # clause and its output
                            filtered_data = [y for x in data if (y := f(x)) is not None]
                         """)

def window_two():
    return WindowContent("Audithooks and metadata",
                         "No more secrets",
                         """
                      import sys
                      sys.audit(django.execute_sql, sql, params)

                      $ manage.py migrate
                      $ Operations to perform: Apply all migrations:
                      $ Running migrations:
                      $         django.execute_sql(SELECT "django_migrations"."app"m "dj..., ())
                      $         django.execute_sql(.......)


                      https://mastodon.social/@freakboy3742/103019925896462510
                        """,
                         )

def window_three():
    return WindowContent("Typehint Updates",
                         "Protocols, TypedDict and more",
                         """
                                from typing import Iterable
                                from typing_extensions import Protocol

                                class SupportsClose(Protocol):
                                    def close(self) -> None:
                                    ...  # Empty method body (explicit '...')

                                class Resource:  # No SupportsClose base class!
                                    # ... some methods ...

                                    def close(self) -> None:
                                    self.resource.release()

                                def close_all(items: Iterable[SupportsClose]) -> None:
                                    for item in items:
                                        item.close()

                                close_all([Resource(), open('some/file')])

                                Also included in 3.8: Literal, Final and TypedDict
                         """,
                         )

def window_four():
    return WindowContent("C Updates and Python Optimizations",
                         "Gotta go fast!",
                         """
                        C API for Python Initialization Configuration.

                        C API for CPython, the “vectorcall” calling protocol allowing
                        faster calls to internal Python methods without temp objects.

                        Many shutil functions now use platform specific "fast-copy" syscalls.

                        Sped-up field lookups in collections.namedtuple(). They are now
                        the fastest form of instance variable lookup in Python.

                        Doubled the speed of class variable writes. 

                        Reduced overhead of converting arguments passed to many builtin
                        functions. This sped up calling some simple builtins 20–50%.

                        LOAD_GLOBAL instruction now uses new “per opcode cache” mechanism.
                        It is about 40% faster now.
                         """,
                         )

def window_five():
    return WindowContent("Release Notes",
                         "",
                         """
                            https://docs.python.org/3.9/whatsnew/3.8.html

                            https://docs.python.org/3.9/whatsnew/changelog.html#changelog
                         """
                         )

def window_six():
    return WindowContent("Release Schedule",
                         "",
                         """
                Releases
                --------
                3.8.0 release: Monday, 2019-10-14

                Subsequent bugfix releases at a bi-monthly cadence.

                Expected: -
                3.8.1 candidate 1: Monday, 2019-12-09
                3.8.1 final: Monday, 2019-12-16

                3.8 Lifespan
                ------------

                3.8 will receive bugfix updates approximately every 1-3 months for approximately 18 months.
                After the release of 3.9.0 final, a final 3.8 bugfix update will be released. After that,
                it is expected that security updates (source only) will be released until 5 years after the
                release of 3.8 final, so until approximately October 2024.

                https://www.python.org/dev/peps/pep-0569/
                         """
                         )

def render(stdscr):
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    #Don't render cursor
    curses.curs_set(0)

    # Default window content
    content = main_menu()
    status = "Press 'q' to exit | PRESENTING | Pos: {}, {} | Last key pressed: {} | Python {}"
    k = ord("-")
    _py = f"{'-' * 4}🐍{'-' * 4}"

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1
        elif k == 49:
            content = window_one()
        elif k == 50:
            content = window_two()
        elif k == 51:
            content = window_three()
        elif k == 52:
            content = window_four()
        elif k == 53:
            content = window_five()
        elif k == 54:
            content = window_six()
        elif k == 77 or k == 109:
            content = main_menu()


        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Centering calculations
        start_x_title = int((width // 2) - (len(content.title) // 2) - len(content.title) % 2)
        start_x_py = int((width // 2) - (len(_py) // 2) - len(_py) % 2)
        start_x_subtitle = int((width // 2) - (len(content.subtitle) // 2) - len(content.subtitle) % 2)
        start_y = int((height // 8) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, status.format(cursor_x, cursor_y, chr(k), f"{sys.version_info.major}.{sys.version_info.minor}"))

        stdscr.addstr(height-1, len(status), " " * (width - len(status) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, content.title)
        stdscr.addstr(start_y + 3, start_x_py, _py)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, content.subtitle)
        stdscr.addstr(start_y + 5, 0, content.content)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(render)

if __name__ == "__main__":
    main()
