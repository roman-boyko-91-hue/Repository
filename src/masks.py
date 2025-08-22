def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    first_number = card_number[:6]
    last_number = card_number[-4:]
    avg_number = "** ****"
    return f"{first_number[:4]} {first_number[4:6]}{avg_number} {last_number}"


print(get_mask_card_number("7020 7922 8960 6361"))


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    first_number = "**"
    last_number = account_number[-4:]
    return f"{first_number}{last_number}"


print(get_mask_account("706361"))
