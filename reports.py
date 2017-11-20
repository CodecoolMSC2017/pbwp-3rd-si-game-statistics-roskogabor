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


def get_latest(file_name):
    latest = ""
    with open(file_name, "r") as yeardata:
        games = yeardata.readlines()
        datas = []
        for i in range(len(games)):
            datalist = games[i].split("\t")
            datas.append(datalist)
        for i in range(len(datas)):
            if latest == "" or datas[i][2] > latest[1]:
                latest = [datas[i][0], datas[i][2]]
        return latest[0]


def count_by_genre(file_name, genre):
    with open(file_name, "r") as genredata:
        genres = genredata.readlines()
        datas = []
        for i in range(len(genres)):
            datalist = genres[i].split("\t")
            datas.append(datalist)
        counter = 0
        for i in range(len(datas)):
            if datas[i][3] == genre:
                counter += 1
        return counter


def get_line_number_by_title(file_name, title):
    pass


if __name__ == "__main__":
    print(count_by_genre("game_stat.txt", "First-person shooter"))
