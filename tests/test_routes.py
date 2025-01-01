import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_products(client):
    rv = client.get('/products')
    assert rv.status_code == 200
    assert b'item1' in rv.data

