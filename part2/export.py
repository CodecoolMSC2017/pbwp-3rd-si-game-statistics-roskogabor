import printing


file_name = "game_stat.txt"
gametitle = "Diablo II"


# Export functions
def exportdata(datas):
    with open("export.txt", "w") as data:
        for i in range(len(datas)):
            data.write(str(datas[i]) + "\n")


if __name__ == "__main__":
    gamedata = printing.print_datas(file_name, gametitle)
    exportdata(gamedata)