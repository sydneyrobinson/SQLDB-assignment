import database
#if adding new columns after database has been structured, delete data.db and run again

MENU_PROMPT = """
-- Video Game App --

Please choose one of these options:

1) Add a new game
2) See all games
3) Find a game by...[Opens Sub-Menu]
4) Compare Games (Best/Worst Attributes for a Game) [Opens Sub-Menu]
5) Change rating for a game
6) Delete game by ID
7) Delete games by name
8) Wipe Database
9) Find game by rating range
10) Exit.


Your Selection: """

SUB_MENU_FIND_GAME_PROMPT = """
-- Find Game --
1) by Name
2) by Price Range


Your Selection: 
"""

SUB_MENU_COMPARE_GAMES_PROMPT = """
-- Compare Games (Best/Worst Attributes for a Game) --
1) See which system is best for a game
2) Sort games from lowest to highest price


Your Selection:
"""

SUB_MENU_DELETE_PROMPT = """
-- Delete Rows --
1) Delete game by ID
2) Delete games by name
3) Wipe Database
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "10":
        if user_input == "1":
            prompt_add_new_game(connection)
            prompt_see_all_games(connection)

        elif user_input == "2":
            prompt_see_all_games(connection)

        elif user_input == "3":
            prompt_find_game_by_name(connection)

        elif user_input == "4":
            prompt_find_best_system(connection)

        elif user_input == "6":
            prompt_delete_game_byID(connection)
            prompt_see_all_games(connection)

        elif user_input == "7":
            prompt_delete_games_byNAME(connection)
            prompt_see_all_games(connection)

        elif user_input == "8":
            prompt_wipe_db(connection)

        elif user_input == "9":
            prompt_find_games_by_rating_range(connection)

        else:
            print("\ninvalid input please try again")


def sub_menu_find_game(connection):
    while (user_input := input(MENU_PROMPT)) != "9":
        if user_input == "1":
            prompt_add_new_game(connection)
            prompt_see_all_games(connection)

        else:
            print("\ninvalid input please try again")



def prompt_delete_game_byID(connection):
    id = input("Enter game ID (row ID) to delete: ")
    games = database.delete_game_byID(connection, id)

def prompt_delete_games_byNAME(connection):
    name = input("Enter game name to delete all instances: ")
    games = database.get_games_by_name(connection, name)
    for game in games:
        games = database.delete_games_byNAME(connection, name)

def prompt_wipe_db(connection):
    try:
        answer = str(input("Are you sure you want to wipe your database? (y/n): ")).lower()
        if answer == 'y':
            games = database.wipe_db(connection)
            prompt_see_all_games(connection)
        elif answer == 'n':
            print("\nOkay. Your database will not be deleted.")
            pass
        else:
            raise TypeError
    except TypeError:
        print("not a valid response!")
        prompt_wipe_db(connection)

def prompt_find_games_by_rating_range(connection):
    try:
        min = int(input("Please enter your minimum rating value: "))
        max = int(input("Please enter your maximum rating value: "))
        if min >= 0 and max <= 100:
            games = database.get_games_by_rating_range(connection, min, max)
            for game in games:
                print(f"{game[1]} ({game[2]}) {game[3]} - {game[4]}/100")

        else:
            raise ValueError
    except ValueError:
        print("That is not an acceptable value! Please only type an integer between 0-100.")
        prompt_find_games_by_rating_range(connection)

def prompt_find_best_system(connection):
    name = input("Enter game name to find the best system for: ")
    best_system = database.get_best_system_for_game(connection, name)
    print(f"The best system for {name} is: {best_system[2]}")  # column number 2
    if name not in best_system("data.db"):
        print("no game exists with that name!")
    # error here when typed in game name that does not exist


def prompt_find_game_by_name(connection):
    name = input("Enter game name to find: ")
    games = database.get_games_by_name(connection, name)
    for game in games:
        print(f"{game[1]} ({game[2]}) {game[3]} - {game[4]}/100")
    if name not in games:
        print("no game exists with that name!")


def prompt_see_all_games(connection):
    games = database.get_all_games(connection)
    print("--->Game DB")
    for game in games:
        print(f"{game[1]} ({game[2]}) {game[3]} - {game[4]}/100")
    print("-->")


def prompt_add_new_game(connection):
    try:
        name = input("Enter game name: ")
        method = input("Enter a system that it is on: ")
        year = int(input("Enter when it came out on that system: "))
        rating = int(input("Enter your rating score (for that particular system!) (0-100): "))
        database.add_game(connection, name, method, year, rating)
    except ValueError:
        print("Invalid input! please type an integer :)")


menu()
