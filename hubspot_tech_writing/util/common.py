import logging
import typing as t
from pathlib import Path

import colorlog
from colorlog.escape_codes import escape_codes


def setup_logging(level=logging.INFO, verbose: bool = False):
    reset = escape_codes["reset"]
    log_format = f"%(asctime)-15s [%(name)-36s] %(log_color)s%(levelname)-8s:{reset} %(message)s"

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(log_format))

    logging.basicConfig(format=log_format, level=level, handlers=[handler])

    logging.getLogger("urllib3.connectionpool").setLevel(level)


class ContentTypeResolver:
    MARKUP_SUFFIXES = [".md", ".rst"]
    HTML_SUFFIXES = [".html", ".html5", ".htm"]
    TEXT_SUFFIXES = MARKUP_SUFFIXES + HTML_SUFFIXES + [".txt"]

    def __init__(self, name: t.Union[str, Path]):
        self.name = name
        self.suffix = Path(name).suffix

    def is_markup(self):
        return self.suffix in self.MARKUP_SUFFIXES

    def is_html(self):
        return self.suffix in self.HTML_SUFFIXES

    def is_text(self):
        return self.suffix in self.TEXT_SUFFIXES

    def is_file(self):
        return not self.is_text()
