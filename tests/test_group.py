"""Group Class Tests"""
import pytest
from orijenpy import group

@pytest.mark.usefixtures("test_session")
class TestGroup:
    """Class used to test Group"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(group(test_session).list()['user_groups'])>0

    def test_get(self, test_session):
        """Method to test get()"""
        r = group(test_session).list()['user_groups'][0]['name']
        assert isinstance(group(test_session).get(r), dict)
