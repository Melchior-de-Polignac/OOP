def test_successful_order_returns_total_and_reduces_stock(service, repo):
    result = service.place_order("SHIRT", 2)
    assert result == {"success": True, "item": "T-Shirt", "quantity": 2, "total": 60.0}
    assert repo.get_product("SHIRT")["stock"] == 48


def test_unknown_product(service):
    assert service.place_order("NOPE", 1) == {
        "success": False,
        "error": "Product not found",
    }


def test_not_enough_stock_leaves_stock_untouched(service, repo):
    result = service.place_order("HAT", 31)
    assert result == {"success": False, "error": "Not enough stock"}
    assert repo.get_product("HAT")["stock"] == 30


def test_fixtures_are_isolated_between_tests(repo):
    assert repo.get_product("SHIRT")["stock"] == 50
