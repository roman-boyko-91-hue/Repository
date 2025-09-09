import pytest

@pytest.fixture
def card_number():
    return "7020 7922 8960 6361"

@pytest.fixture
def card_result():
    return "7020 79** **** 6361"
