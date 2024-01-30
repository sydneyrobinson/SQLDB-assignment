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
            prompt_find_best_method(connection)

        else:
            print("\ninvalid input please try again")


def sub_menu_find_game():
    pass




def prompt_find_best_method(connection):
    name = input("Enter game name to find: ")
    best_method = database.get_best_preparation_for_game(connection, name)
    print(f"The best preparation method for {name} is: {best_method[2]}")  # column number 2
    # error here when typed in game name that does not exist


def prompt_find_game(connection):
    name = input("Enter game name to find: ")
    games = database.get_games_by_name(connection, name)
    for game in games:
        print(f"{game[1]} ({game[2]}) - {game[3]}/100")


def prompt_see_all_games(connection):
    games = database.get_all_games(connection)
    for game in games:
        print(f"{game[1]} ({game[2]}) - {game[3]}/100")


def prompt_add_new_game(connection):
    name = input("Enter game name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))
    database.add_game(connection, name, method, rating)


menu()
