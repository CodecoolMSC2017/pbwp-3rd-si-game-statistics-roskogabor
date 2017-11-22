import printing


file_name = "game_stat.txt"
gameyear = "2004"
gametitle = "Diablo II"
gamegenre = "First-person shooter"


# Export functions
def exportdata(datas):
    with open("export.txt", "w") as data:
        for i in range(len(datas)):
            data.write(str(datas[i]) + "\n")


if __name__ == "__main__":
    gamedata = printing.print_datas(file_name, gameyear, gametitle, gamegenre)
    exportdata(gamedata)
