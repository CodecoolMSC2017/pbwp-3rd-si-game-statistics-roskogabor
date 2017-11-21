import math


# Report functions
def get_most_played(file_name):
    with open(file_name, "r") as gamedata:
        games = gamedata.readlines()
        datas = []
        for i in range(len(games)):
            datalist = games[i].split("\t")
            datas.append(datalist)
        most = ""
        for i in range(len(datas)):
            if most == "" or float(datas[i][1]) > most[1]:
                most = [datas[i][0], float(datas[i][1])]
    return most[0]


def sum_sold(file_name):
    with open(file_name, "r") as gamedata:
        games = gamedata.readlines()
        datas = []
        for i in range(len(games)):
            datalist = games[i].split("\t")
            datas.append(float(datalist[1]))
        sumsold = sum(datas)
    return sumsold


def get_selling_avg(file_name):
    with open(file_name, "r") as gamedata:
        games = gamedata.readlines()
        datas = []
        for i in range(len(games)):
            datalist = games[i].split("\t")
            datas.append(float(datalist[1]))
        avgofselling = sum_sold(file_name) / len(datas)
    return avgofselling


def count_longest_title(file_name):
    with open(file_name, "r") as titledata:
        titles = titledata.readlines()
        datas = []
        for i in range(len(titles)):
            datalist = titles[i].split("\t")
            datas.append(datalist)
        longest = ""
        for i in range(len(datas)):
            if longest == "" or len(datas[i][0]) > longest:
                longest = len(datas[i][0])
    return longest


def get_date_avg(file_name):
    with open(file_name, "r") as yeardata:
        years = yeardata.readlines()
        datas = []
        for i in range(len(years)):
            datalist = years[i].split("\t")
            datas.append(int(datalist[2]))
        avgofyears = sum(datas) / len(datas)
    return math.ceil(avgofyears)


if __name__ == "__main__":
    print(count_longest_title("game_stat.txt"))
