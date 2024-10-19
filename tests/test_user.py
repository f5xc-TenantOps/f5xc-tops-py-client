"""User Class Tests"""
import pytest
from orijenpy import user

@pytest.mark.usefixtures("test_session")
class TestUser:
    """Class used to test APIcred"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(user(test_session).list()['items'])>0
