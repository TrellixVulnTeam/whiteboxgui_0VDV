#!/usr/bin/env python

"""Tests for `whiteboxgui` package."""


import unittest
import platform

from whiteboxgui import whiteboxgui


class TestWhiteboxgui(unittest.TestCase):
    """Tests for `whiteboxgui` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        if platform.system() != 'Windows':
            whiteboxgui.show()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
