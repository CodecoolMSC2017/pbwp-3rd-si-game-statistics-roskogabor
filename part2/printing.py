import reports

# datas to work with
file_name = "game_stat.txt"
gametitle = "Diablo II"


# Printing functions
def print_datas(fname, title):
    getmost = reports.get_most_played(fname)
    sumsold = reports.sum_sold(fname)
    getsavg = reports.get_selling_avg(fname)
    countlongest = reports.count_longest_title(fname)
    getdateavg = reports.get_date_avg(fname)
    getgame = reports.get_game(fname, gametitle)
    return [getmost, sumsold, getsavg, countlongest, getdateavg, getgame]


if __name__ == "__main__":
    datas = print_datas(file_name, gametitle)
    for i in range(len(datas)):
        print(datas[i])