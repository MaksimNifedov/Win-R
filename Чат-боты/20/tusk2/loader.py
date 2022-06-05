import sqlite3

import vkwave
from vkwave.bots import SimpleLongPollBot
import database

import config

bot = SimpleLongPollBot(tokens=config.BOT_TOKEN,
                        group_id=213723214)

try:
    bd = database.Database(path_to_db=r'database/imaginarium.db')
    bd.create_table_UserCards()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    bd.create_table_UserScore()
except sqlite3.OperationalError as e:
    print(e)