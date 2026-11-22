import pytest

from shop import OrderService, ProductRepository


@pytest.fixture
def repo():
    return ProductRepository()


@pytest.fixture
def service(repo):
    return OrderService(repo)
