'''
CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, name TEXT, system TEXT, rating INTEGER);
INSERT INTO games (name,system,rating) VALUES ("Exclusive Blend", 'Percolator', 65);
#SELECT * FROM games;  #star means all the columns. we don't want the ID
SELECT system, rating FROM games ORDER BY rating DESC LIMIT 1; #limit means only one row returned
SELECT * FROM games WHERE name = "Exclusive Blend" ORDER BY rating DESC LIMIT 1;
SELECT system, AVG(rating) FROM games GROUP BY system;
'''

import sqlite3

#queries
CREATE_GAMES_TABLE = "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, name TEXT, system TEXT, rating INTEGER);"

INSERT_GAME =  "INSERT INTO games (name,system,rating) VALUES (?,?,?);"

GET_ALL_GAMES = "SELECT * FROM games;"
GET_GAMES_BY_NAME = "SELECT * FROM games WHERE name = ?;"
GET_BEST_SYSTEM_FOR_GAME = """
SELECT * FROM games
WHERE name = ?
ORDER BY rating DESC LIMIT 1;"""
DELETE_GAME_BYID = "DELETE from games WHERE id = ?;"
DELETE_GAME_BYNAME = "DELETE from games WHERE name = ?;"

def delete_game_byID(connection,id): #https://www.geeksforgeeks.org/how-to-delete-a-specific-row-from-sqlite-table-using-python/
    with connection:
        connection.execute(DELETE_GAME_BYID, (id,))
def delete_games_byNAME(connection,name):
    with connection:
        connection.execute(DELETE_GAME_BYNAME, (name,))

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_GAMES_TABLE)


def add_game(connection, name, system, rating):
    with connection:
        connection.execute(INSERT_GAME, (name, system, rating))


def get_all_games(connection):
    with connection:
        return connection.execute(GET_ALL_GAMES).fetchall()


def get_games_by_name(connection,name):
    with connection:
        return connection.execute(GET_GAMES_BY_NAME, (name,)).fetchall() #name has to be a tuple


def get_best_system_for_game(connection, name):
    with connection:
        return connection.execute(GET_BEST_SYSTEM_FOR_GAME, (name,)).fetchone()
