import  pytest

from src.widget import mask_account_card, get_date

def test_invalid_length():
    with pytest.raises(ValueError):
        mask_account_card("")
        get_date("")