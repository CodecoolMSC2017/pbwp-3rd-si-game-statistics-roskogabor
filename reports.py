
# Report functions
def count_games(file_name):
    with open(file_name, "r") as gamedata:
        games = gamedata.readlines()
        number = len(games)
    return number

def decide(file_name, year):
    yearlist = []
    result = False
    with open(file_name, "r") as yeardata:
        games = yeardata.readlines()
        for i in range(len(games)):
            data = games[i].split("\t")
            gameyear = int(data[2])
            yearlist.append(gameyear)
        result = True if int(year) in yearlist else False
    return result

if __name__ == "__main__":
    print(decide("game_stat.txt",2000))