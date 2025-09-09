import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("list_dict, state", [
    ("", "EXECUTED"),
    ("", "CANCELED"),
    ({"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"})
    ])
def test_filter_by_state(list_dict: str | dict[str, str | int],
                         state: str | dict[str, str | int]) -> None:
    assert filter_by_state(list_dict) == state

def test_sort_by_date(list_dict, reverse=False) -> None:
    assert sort_by_date(list_dict) == reverse