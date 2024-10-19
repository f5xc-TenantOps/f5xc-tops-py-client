"""Role Class Tests"""
import pytest
from orijenpy import role

@pytest.mark.usefixtures("test_session")
class TestRole:
    """Class used to test Group"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(role(test_session).list()['items'])>0
