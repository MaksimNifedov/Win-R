import sqlite3


async def on_startup(dp):
    pass

if __name__ == '__main__':
    from handlers import bot
    bot.run_forever()
