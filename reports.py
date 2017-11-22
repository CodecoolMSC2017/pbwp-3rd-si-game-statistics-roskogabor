# Report functions
def openfile(fname):
    with open(fname, "r") as datas:
        datalist = datas.readlines()
    return datalist


def makelist(datas, indexof, datatype):
    datalist = []
    for i in range(len(datas)):
        data = datas[i].split("\t")
        if indexof != "x":
            datalist.append(datatype(data[indexof]))
        else:
            datalist.append(data)
    return datalist


def count_games(file_name):
    games = openfile(file_name)
    number = len(games)
    return number


def decide(file_name, year):
    result = False
    games = openfile(file_name)
    yearlist = makelist(games, 2, int)
    result = True if int(year) in yearlist else False
    return result


def get_latest(file_name):
    latest = ""
    games = openfile(file_name)
    datas = makelist(games, "x", str)
    for i in range(len(datas)):
        if latest == "" or datas[i][2] > latest[1]:
            latest = [datas[i][0], datas[i][2]]
    return latest[0]


def count_by_genre(file_name, genre):
    genres = openfile(file_name)
    datas = makelist(genres, "x", str)
    counter = 0
    for i in range(len(datas)):
        if datas[i][3] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    datas = openfile(file_name)
    titles = makelist(datas, 0, str)
    listindex = titles.index(title)
    return int(listindex) + 1


if __name__ == "__main__":
    print(get_line_number_by_title("game_stat.txt", "Counter-Strike"))
