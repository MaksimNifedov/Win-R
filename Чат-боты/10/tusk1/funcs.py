import random


def shuffle_cards(i_start: int, i_end: int) -> str:
    items = list(map(lambda x: str(x), range(i_start, i_end + 1)))
    random.shuffle(items)
    return ' '.join(items)

def str_in_list(str_list: str) -> list:
    str_list = str_list.split(' ')
    try:
        str_list = list(map(lambda x: int(x), str_list))
    except Exception:
        str_list = []
    return str_list

def list_in_str(int_list: list) -> str:
    int_list = list(map(lambda x: str(x), int_list))
    return ' '.join(int_list)