import doctest
import unittest2


DOCTEST_FLAGS = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_NDIFF
)


class TestSonata(unittest2.TestCase):
    def test_dummy(self):
        # TODO: replace with a test which does something once we start to have
        # tests!
        pass


def additional_tests():
    return unittest2.TestSuite(
        # TODO: add files which use doctests here
        #doctest.DocFileSuite('../audioscrobbler.py', optionflags=DOCTEST_FLAGS),
    )
