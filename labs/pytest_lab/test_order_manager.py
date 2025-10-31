import pytest
from service_body_test import Order

def test_total_normal_items():
    order = Order(1, [
        {"price": 185.0, "quantity": 9},
        {"price": 36.0, "quantity": 5}
    ])
    assert order.total() == 1845.0

def test_total_empty_list():
    order = Order(2, [])
    assert order.total() == 0.0

def test_total_zero_quantity():
    order = Order(3, [{"price": 99.0, "quantity": 0}])
    assert order.total() == 0.0

def test_total_negative_price():
    order = Order(4, [{"price": -5.0, "quantity": 2}])
    assert order.total() == -10.0

def test_total_non_numeric():
    order = Order(5, [{"price": "abc", "quantity": 2}])
    with pytest.raises(TypeError):
        order.total()

def test_most_expensive_normal():
    order = Order(6, [
        {"price": 17.0, "quantity": 1},
        {"price": 25.0, "quantity": 1},
        {"price": 43.0, "quantity": 1}
    ])
    result = order.most_expensive()
    assert result["price"] == 43.0

def test_most_expensive_single_item():
    order = Order(7, [{"price": 31.0, "quantity": 1}])
    assert order.most_expensive()["price"] == 31.0

def test_apply_discount_valid_20_percent():
    order = Order(8, [
        {"price": 100.0, "quantity": 1},
        {"price": 50.0, "quantity": 1}
    ])
    order.apply_discount(20)
    assert order.items[0]["price"] == 80.0
    assert order.items[1]["price"] == 40.0

def test_apply_discount_zero_percent():
    order = Order(9, [{"price": 85.0, "quantity": 1}])
    order.apply_discount(0)
    assert order.items[0]["price"] == 85.0

def test_apply_discount_100_percent():
    order = Order(10, [{"price": 100.0, "quantity": 1}])
    order.apply_discount(100)
    assert order.items[0]["price"] == 0.0

def test_apply_discount_over_100():
    order = Order(11, [{"price": 100.0, "quantity": 1}])
    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(101)

def test_apply_discount_negative():
    order = Order(12, [{"price": 100.0, "quantity": 1}])
    with pytest.raises(ValueError, match="Invalid discount"):
        order.apply_discount(-1)

def test_apply_discount_empty_list():
    order = Order(13, [])
    order.apply_discount(50) 
    assert order.items == [] 

def test_repr_with_items():
    order = Order(14, [{"price": 12.0, "quantity": 1}, {"price": 11, "quantity": 1}])
    assert repr(order) == "<Order 14: 2 items>"

def test_repr_empty():
    order = Order(15, [])
    assert repr(order) == "<Order 15: 0 items>"

def test_repr_single_item():
    order = Order(16, [{"price": 11, "quantity": 1}])
    assert repr(order) == "<Order 16: 1 items>"