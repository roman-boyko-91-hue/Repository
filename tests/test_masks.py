import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number_long() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("7020 7922 8960 6361")


def test_get_mask_card_number_null() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")