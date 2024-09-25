import pytest

from python.enum.Category import Category


@pytest.mark.parametrize("name", ["Entertainment", "Science", "Technology"])
def test_one(name):
    categories: list[str] = [c for c in Category]
    assert name in categories
