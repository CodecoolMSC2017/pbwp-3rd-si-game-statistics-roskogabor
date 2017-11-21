

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


if __name__ == "__main__":
    print(sum_sold("game_stat.txt"))
