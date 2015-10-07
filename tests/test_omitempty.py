# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import omitempty

class EmptyObj(object):
    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

class ZeroLenObj(object):
    def __len__(self):
        return 0

class TestOmitempty(unittest.TestCase):

    def test_empty(self):
        self.assertEquals({}, omitempty({}))

    def test_empty_values(self):
        self.assertEquals({}, omitempty({
            "x": 0,
            "y": [],
            "z": False,
            3: {},
            5: (),
            6: EmptyObj(),
            4: ZeroLenObj(),
        }))

    def test_simple_rec(self):
        d = {}
        d["x"] = d

        self.assertEquals(d, omitempty(d))

    def test_simple(self):
        self.assertEquals({"a": 1, "c": 3}, omitempty({"a": 1, "b": 0, "c": 3}))

    def test_deep(self):
        d = {"a": {"b": {"c": {"d": 1, "e": 0}, "f": False}, "g": []}, "h":9}
        self.assertEquals({"a": {"b": {"c": {"d": 1}}}, "h":9}, omitempty(d))
