import database
#if adding new columns after database has been structured, delete data.db and run again

MENU_PROMPT = """
-- Video Game App --

Please choose one of these options:

1) Add a new game
2) See all games
3) Find a game by name [Opens Sub-Menu]
4) Compare Games (Best/Worst Attributes for a Game) [Opens Sub-Menu]
5) Change rating for a game
6) Delete game
7) Wipe Database
8) Exit.


Your Selection: """

SUB_MENU_FIND_GAME_PROMPT = """
-- Find Game --
1) by Name
2) by System
3) by Publisher
4) by Developer
5) by Year Released
6) by Genre
7) by Price Range


Your Selection: 
"""

SUB_MENU_COMPARE_GAMES_PROMPT = """
-- Compare Games (Best/Worst Attributes for a Game) --
1) See which system is best for a game
2) Sort games from lowest to highest price
3) Sort games from newest to oldest


Your Selection:
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "8":
        if user_input == "1":
            prompt_add_new_game(connection)

        elif user_input == "2":
            prompt_see_all_games(connection)

        elif user_input == "3":
            prompt_find_game(connection)

        elif user_input == "4":
            prompt_find_best_system(connection)

        elif user_input == "6":
            prompt_delete_game_byID(connection)
        else:
            print("\ninvalid input please try again")


def sub_menu_find_game(connection):
    pass


def prompt_delete_game_byID(connection):
    id = input("Enter game ID (row ID) to delete: ")
    games = database.delete_game_byID(connection, id)

def prompt_delete_game_byNAME(connection):
    name = input("Enter game name to delete all instances: ")

    games = database.delete_game_byNAME(connection, name)
    for name in games:
def prompt_find_best_system(connection):
    name = input("Enter game name to find the best system for: ")
    best_system = database.get_best_system_for_game(connection, name)
    print(f"The best system for {name} is: {best_system[2]}")  # column number 2
    if name not in best_system("data.db"):
        print("no game exists with that name!")
    # error here when typed in game name that does not exist


def prompt_find_game(connection):
    name = input("Enter game name to find: ")
    games = database.get_games_by_name(connection, name)
    for game in games:
        print(f"{game[1]} ({game[2]}) - {game[3]}/100")
    if name not in games:
        print("no game exists with that name!")


def prompt_see_all_games(connection):
    games = database.get_all_games(connection)
    print("--->Game DB")
    for game in games:
        print(f"{game[1]} ({game[2]}) - {game[3]}/100")
    print("-->")


def prompt_add_new_game(connection):
    name = input("Enter game name: ")
    method = input("Enter a system that it is on : ")
    rating = int(input("Enter your rating score (for that particular system!) (0-100): "))
    database.add_game(connection, name, method, rating)


menu()
