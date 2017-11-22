import math
import re


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


def get_most_played(file_name):
    games = openfile(file_name)
    datas = makelist(games, "x", str)
    most = ""
    for i in range(len(datas)):
        if most == "" or float(datas[i][1]) > most[1]:
            most = [datas[i][0], float(datas[i][1])]
    return most[0]


def sum_sold(file_name):
    games = openfile(file_name)
    datas = makelist(games, 1, float)
    sumsold = sum(datas)
    return sumsold


def get_selling_avg(file_name):
    games = openfile(file_name)
    datas = makelist(games, 1, float)
    avgofselling = sum_sold(file_name) / len(datas)
    return avgofselling


def count_longest_title(file_name):
    titles = openfile(file_name)
    datas = makelist(titles, "x", str)
    longest = ""
    for i in range(len(datas)):
        if longest == "" or len(datas[i][0]) > longest:
            longest = len(datas[i][0])
    return longest


def get_date_avg(file_name):
    years = openfile(file_name)
    datas = makelist(years, 2, int)
    avgofyears = sum(datas) / len(datas)
    return math.ceil(avgofyears)


def convertdata(datalist):
    for i in range(len(datalist)):
        datalist[i] = datalist[i].strip()
        m = re.search(r'\.', datalist[i])
        try:
            var = m.start()
            datalist[i] = float(datalist[i])
        except:
            try:
                datalist[i] = int(datalist[i])
            except:
                datalist[i] = str(datalist[i])
    return datalist


def get_game(file_name, title):
    titles = openfile(file_name)
    datas = makelist(titles, "x", str)
    for i in range(len(datas)):
        if datas[i][0] == title:
            gamedata = datas[i]
    gamedata = convertdata(gamedata)
    return gamedata


if __name__ == "__main__":
    print(get_game("game_stat.txt","The Sims"))
