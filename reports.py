
# Report functions
def count_games(file_name):
    with open(file_name, "r") as gamedata:
        games = gamedata.readlines()
        number = len(games)
    return number

if __name__ == "__main__":
    print(count_games("game_stat.txt"))