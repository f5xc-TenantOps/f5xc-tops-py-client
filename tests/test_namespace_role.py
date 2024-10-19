"""Namespace_role Class Test"""
import pytest
from orijenpy import nsrole

@pytest.mark.usefixtures("test_session")
class TestNSrole:
    """Class used to test APIcred"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(nsrole(test_session).list()['items'])>0
