import pytest

from src.main import *


def test_html():
    @make_html("p")
    @make_html("strong")
    def get_text(text="I code with Pybites"):
        return text

    assert get_text() == "<p><strong>I code with Pybites</strong></p>"
