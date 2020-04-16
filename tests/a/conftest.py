from mycode.som import A

import pytest


@pytest.fixture
def a():
    return A('abc')
