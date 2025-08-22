def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    card_info = card_type_number.rsplit(' ', 1)
    if "Счет" in card_type_number:
        first_number = "**"
        return f"{first_number}{card_info[1][-4:]}"
    else:
        return f"{card_info[0]} {card_info[1][:4]} {card_info[1][4:6]}** **** {card_info[1][-4:]}"

print(mask_account_card("Visa Platinum 73654108430135874305"))


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
       и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
