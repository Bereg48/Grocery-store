import pytest
from src.utils import Product, category

product = Product("Яблоко", 250, 20)


def test__init__product():
    assert product.name == "Яблоко"
    assert product.price == 250
    assert product.count == 20


def test_sale():
    product.sale(1)
    assert product.count == 19


def test_fill():
    product.fill(1)
    assert product.count == 20


def test__init__category():
    assert category.name == "Яблоки"
    assert category.products == [product]


def test_remove():
    category.remove(0)
    assert category.products == []


def test_add():
    category + product
    assert category.products == [product]
