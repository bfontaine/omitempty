# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import omitempty

class TestOmitempty(unittest.TestCase):

    def test_empty(self):
        self.assertEquals({}, omitempty({}))
