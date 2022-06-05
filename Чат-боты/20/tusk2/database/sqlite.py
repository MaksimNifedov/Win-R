import pathlib
import sqlite3


class Database:
    def __init__(self, path_to_db='database/user_info_database.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_UserCards(self):
        sql = """
        CREATE TABLE UserCards (
        id int,
        cards text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_UserCards(self, id: int, cards: str):
        sql = "INSERT INTO UserCards(id, cards) VALUES(?, ?)"
        parameters = (id, cards)
        self.execute(sql, parameters=parameters, commit=True)

    def update_cards_UserCards(self, id: int, cards: str):
        sql = "UPDATE UserCards SET cards=? WHERE id=?"
        return self.execute(sql, parameters=(cards, id), commit=True)

    def select_UserCards(self, **kwargs):
        sql = "SELECT * FROM UserCards WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_UserCards(self):
        sql = "SELECT * FROM UserCards"
        return self.execute(sql, fetchall=True)

    def create_table_UserScore(self):
        sql = """
        CREATE TABLE UserScore (
        id int,
        score int,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_UserScore(self, id: int, score: int):
        sql = "INSERT INTO UserScore(id, score) VALUES(?, ?)"
        parameters = (id, score)
        self.execute(sql, parameters=parameters, commit=True)

    def update_score_UserScore(self, id: int, score: int):
        sql = "UPDATE UserScore SET score=? WHERE id=?"
        return self.execute(sql, parameters=(score, id), commit=True)

    def select_UserScore(self, **kwargs):
        sql = "SELECT * FROM UserScore WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_UserScore(self):
        sql = "SELECT * FROM UserScore"
        return self.execute(sql, fetchall=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    @staticmethod
    def format_args_2(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} <> ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def delete_all(self):
        self.execute("DELETE FROM UserCards WHERE True", commit=True)
        self.execute("DELETE FROM UserScore WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE UserCards", commit=True)
        self.execute("DROP TABLE UserScore", commit=True)


def logger(statement):
    print(f"""
Executing:
{statement}
""")