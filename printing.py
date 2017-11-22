import reports


file_name = "game_stat.txt"
# Printing functions
print(reports.count_games(file_name))
print(reports.decide(file_name, "2004"))
print(reports.get_latest(file_name))
print(reports.count_by_genre(file_name, "First-person shooter"))
print(reports.get_line_number_by_title(file_name, "Diablo II"))
