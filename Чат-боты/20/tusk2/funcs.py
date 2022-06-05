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


def get_word(img_numbers: list) -> dict:
    word_book = {}
    all_words = []
    with open(r'data/words.txt', 'r') as f:
        lines = f.read().splitlines()
        for img_num in img_numbers:
            line = lines[img_num - 1].replace('\t', ' ').split(' ')
            if '' in line:
                line.remove('')
            index_img = int(line[0].split('.')[0])
            word_book[index_img] = line[1:]
            all_words += line[1:]
        set_words = set(all_words)
        result = {}
        for word in set_words:
            if all_words.count(word) == 1:
                result['word'] = word
                for img_name, words in word_book.items():
                    if word in words:
                        result['img_name'] = img_name
                        break
                break
    return result

