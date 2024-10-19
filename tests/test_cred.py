"""Cred classes tests"""
import pytest
from orijenpy import apicred, svccred

@pytest.mark.usefixtures("test_session")
class TestAPIcred:
    """Class used to test APIcred"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(apicred(test_session).list()['items'])>0

    def test_get(self, test_session):
        """Method to test get()"""
        r = apicred(test_session).list()['items'][0]['name']
        assert isinstance(apicred(test_session).get(r), dict)

@pytest.mark.usefixtures("test_session")
class TestSVCcred:
    """Class used to test SVCcred"""

    def test_list(self, test_session):
        """Method to test list()"""
        assert len(svccred(test_session).list()['items'])>0

