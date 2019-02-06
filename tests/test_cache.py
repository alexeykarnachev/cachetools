import unittest

import cachetools

from tests import CacheTestMixin


class CacheTest(unittest.TestCase, CacheTestMixin):

    Cache = cachetools.Cache
