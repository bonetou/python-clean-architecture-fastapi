import pytest
from fastapi.testclient import TestClient
from book_store.infrastructure.api.app import app


@pytest.fixture
def test_client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client
