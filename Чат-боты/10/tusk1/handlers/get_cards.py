from vkwave.bots import SimpleBotEvent, PhotoUploader
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
    list_send_cards = []
    for img in cards[:5]:
        list_send_cards.append(f"data/photo/{img}.jpg")

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