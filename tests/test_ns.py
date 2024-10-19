"""NS class tests"""
import pytest
from orijenpy import ns

@pytest.mark.usefixtures("test_session")
class TestNS:
    """Class used to test NS"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(ns(test_session).list()['items'])>0

    def test_get(self, test_session):
        """Method to test get()"""
        r = ns(test_session).list()['items'][0]['name']
        assert isinstance(ns(test_session).get(r), dict)
