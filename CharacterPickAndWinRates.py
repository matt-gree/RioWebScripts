import json
import os
import requests

import Export_List_To_Excel

player = str(input("Enter player name (Leave blank for all): "))
stars = int(input("Enter '0' for stars-off data; '1' for stars-on: "))
ranked = int(input("Enter '0' for all data, '1' for ranked only: "))
print_or_excel = int(input("Enter '0' to display, '1' for display and excel (openpyxl required): "))

excel_filename = "/PickRates_"

url = "https://projectrio-api-1.api.projectrio.app/detailed_stats/?exclude_batting=1&exclude_fielding=1&exclude_pitching=1&by_char=1"
if player != "":
    url += "&username=" + player
if stars == 0:
    url += "&tag=Normal"
    excel_filename += "StarsOff_"
elif stars == 1:
    url += "&tag=Superstar"
    excel_filename += "StarsOn_"
if ranked == 1:
    url += "&tag=Ranked"
    excel_filename += "RankedOnly"

excel_filename += ".xlsx"
filepath = str(os.path.dirname(__file__)) + str(excel_filename)

response = requests.get(url).json()
stats = response["Stats"]

sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: response["Stats"][x]["Misc"]["game_appearances"], reverse=True)
pick_rate_list = []


for char in sorted_char_list:
    char_stats = response["Stats"][char]["Misc"]
    away_wins = char_stats["away_wins"]
    away_losses = char_stats["away_loses"]
    home_wins = char_stats["home_wins"]
    home_losses = char_stats["home_loses"]
    game_appearances = char_stats["game_appearances"]

    # Totals
    total_wins = away_wins + home_wins
    total_losses = away_losses + home_losses
    total = total_wins + total_losses

    # Calculations
    win_percentage = round((total_wins / total) * 100, 2)

    # Store Stats
    pick_rate_list.append([char, total_wins, total, win_percentage])

total_games = 0
total_wins = 0
for item in pick_rate_list:
    total_games += item[2]/9
    total_wins += item[1]/9

total_wins = round(total_wins, 0)
total_games = round(total_games, 0)
for item in pick_rate_list:
    item.append(round((item[2]/total_games) *100,2))

pick_rate_list.insert(0,["Character", "Wins", "Games", "Win Percentage", "Pick Rate"],)
pick_rate_list.insert(1,["Total", total_wins, total_games, round((total_wins/total_games)*100,2), "N/A"],)

for character in pick_rate_list:
    print(str(character[0]) + "   " + str(character[1])+ "   " + str(character[2])+ "   " + str(character[3])+ "   " + str(character[4]))

if print_or_excel == 1:
    import openpyxl

    wb = openpyxl.Workbook()
    wb.save(filepath)

    Export_List_To_Excel.export_to_excel(pick_rate_list, filepath)