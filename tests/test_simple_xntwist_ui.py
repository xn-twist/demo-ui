#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from simple_xntwist_ui import simple_xntwist_ui


class SimpleXntwistUiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = simple_xntwist_ui.app.test_client()

    def test_get_index(self):
        rv = self.app.get('/')
        self.assertIn('Simple XNTwist UI', rv.data.decode())
        self.assertIn('Simple demonstration of the XNTwist algorithm using Flask.', rv.data.decode())
        self.assertIn('Welcome!', rv.data.decode())
        self.assertIn('This is the start of something great.', rv.data.decode())
