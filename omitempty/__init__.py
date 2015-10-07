# -*- coding: UTF-8 -*-

import sys

__version__ = "0.1.0"

class mod_omitempty(object):
    def __init__(self):
        self.__version__ = __version__

    def __call__(self, d):
        return d  # TODO

sys.modules[__name__] = mod_omitempty()
