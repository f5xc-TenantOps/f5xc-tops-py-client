"""Common fixture(s) for test"""
import os
import pytest
from orijenpy import session

@pytest.fixture(scope='session')
def test_session():
    """
    Create a Session object needed for test session
    """
    tenant_url = os.getenv('ORIJEN_TENANT_URL')
    token = os.getenv('ORIJEN_TOKEN')
    if None in [tenant_url, token]:
        raise EnvironmentError("Missing env variable(s) needed for testing.")
    api = session(tenant_url=tenant_url, api_token=token)
    yield api