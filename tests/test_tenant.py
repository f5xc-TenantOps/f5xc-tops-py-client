"""Tenant class tests"""
import pytest
from orijenpy import tenant

@pytest.mark.usefixtures("test_session")
class TestTenant:
    """Class used to test Tenant"""

    def test_last_login(self, test_session):
        """Method to test last_login()"""
        assert len(tenant(test_session).last_login()['last_login_map'])>0

    def test_inactive_users(self, test_session):
        """Method to test list_inactive_users()"""
        r = tenant(test_session).list_inactive_users()
        assert isinstance(r, dict)

    def test_get_settings(self, test_session):
        """Method to test get_settings()"""
        r = tenant(test_session).get_settings()
        assert isinstance(r, dict)