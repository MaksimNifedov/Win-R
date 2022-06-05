from vkwave.bots import SimpleBotEvent, PhotoUploader, Keyboard
from vkwave.bots.core.dispatching import filters

from loader import bot
from loader import bd
import funcs
import random


@bot.message_handler(bot.text_filter(["старт"]))
async def start_game(event: SimpleBotEvent):
    await event.answer('Сейчас раздам карты...')
    user_id = event.object.object.message.peer_id
    uploader = PhotoUploader(bot.api_context)

    # если пользователя нет, то создадим колоду
    items = bd.select_UserCards(id=user_id)
    if items is None:
        items = funcs.shuffle_cards(1, 98)
        bd.add_UserCards(id=user_id, cards=items)
        bd.add_UserScore(id=user_id, score=0)
        items = (user_id, funcs.str_in_list(items))

    # преобразовать строку в массив
    cards = items[1]
    if type(cards) is str:
        cards = funcs.str_in_list(cards)

    # если карт не хватает, пересоздать колоду
    if len(cards) < 5:
        await event.answer(
            message='Ого, все карты уже посмотрели! Сейчас все перетусую.'
        )
        cards = funcs.shuffle_cards(1, 98)
        bd.update_cards_UserCards(id=user_id, cards=cards)
        cards = funcs.str_in_list(cards)

    # формируем список карт
    # собираем клавиатуру
    list_send_cards = []
    img_keyboard = Keyboard(one_time=True)
    word_info = funcs.get_word(cards[:5])
    count_btm = 1
    for img in cards[:5]:
        list_send_cards.append(f"data/photo/{img}.jpg")
        btm_payload = {"choice_img": "true", "is_true": "false"}
        if word_info['img_name'] == img:
            btm_payload["is_true"] = "true"
        img_keyboard.add_text_button(f"{count_btm}", payload=btm_payload)
        count_btm += 1

    # удаляем использованные карты
    cards = funcs.list_in_str(cards[5:])
    bd.update_cards_UserCards(id=user_id, cards=cards)

    big_attachment = await uploader.get_attachments_from_paths(
        peer_id=user_id,
        file_paths=list_send_cards,
    )

    await event.answer(
        attachment=big_attachment
    )
    # отправляем слово
    print(word_info, "WORD INFO")
    await event.answer(
        message=word_info['word'],
        keyboard=img_keyboard.get_keyboard(),
    )


@bot.message_handler(filters.PayloadContainsFilter("choice_img"))
async def only_start_button_pressed(event: SimpleBotEvent):
    user_id = event.object.object.message.peer_id
    call_back = event.object.object.message.payload
    res = call_back.split(',')[1].split(':')[1].replace('"', '').replace('}', '')
    user_score = bd.select_UserScore(id=user_id)
    if res == "true":
        new_score = user_score[1] + 3
        bd.update_score_UserScore(id=user_id, score=new_score)
        await event.answer(
            message=f'Верно! Сыграем ещё? Пиши "Старт". Счёт: {new_score}',
        )
    else:
        await event.answer(
            message=f'Не верно, сыграем ещё? Пиши "Старт". Счёт: {user_score[1]}',
        )