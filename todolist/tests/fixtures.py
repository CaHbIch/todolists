import pytest


@pytest.fixture
def get_auth_client(client):
    def _get_auth_client(user):
        client.force_login(user=user)
        return client

    return _get_auth_client