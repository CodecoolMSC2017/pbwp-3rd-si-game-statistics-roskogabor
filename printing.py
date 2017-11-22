import reports


file_name = "game_stat.txt"
gameyear = "2004"
gametitle = "Diablo II"
gamegenre = "First-person shooter"


# Printing functions
def print_datas(fname, year, title, genre):
    countgames = reports.count_games(fname)
    decideres = reports.decide(fname, year)
    getlatest = reports.get_latest(fname)
    cbygenre = reports.count_by_genre(fname, genre)
    getlnumbytit = reports.get_line_number_by_title(fname, title)
    return [countgames, decideres, getlatest, cbygenre, getlnumbytit]


if __name__ == "__main__":
    datas = print_datas(file_name, gameyear, gametitle, gamegenre)
    for i in range(len(datas)):
        print(datas[i])
