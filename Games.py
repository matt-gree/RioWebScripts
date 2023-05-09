import json
import os
import requests
import datetime
import Export_List_To_Excel

import MattGreeRioWebExtensions
import RioStatsConverter
import MattGreeRioWebExtensions as RWext

import openpyxl

stars = int(input("Enter '0' for stars-off-ranked data; '1' for stars-on-ranked: "))
teams = int(input("Enter '1' to include teams: "))

by_user = int(input("Enter '1' to create a second sheet by user: "))


excel_filename = "/Games_"

simple_url = "https://api.projectrio.app/games/?"
if stars == 0:
    simple_url += "&tag=StarsOffSeason5"
    excel_filename += "StarsOff_"
elif stars == 1:
    simple_url += "@tag=StarsOnSeason5"
    excel_filename += "StarsOn_"

simple_url += "&limit_games=10000"

excel_filename += ".xlsx"
filepath = str(os.path.dirname(__file__)) + str(excel_filename)
wb = openpyxl.Workbook()
wb.save(filepath)

export_list = [["Winner User", "Winner Captain", "Winner Score", "Winner Side", "Winner Elo Before", "Winner Elo After",
                    "Loser User", "Loser Captain", "Loser Score", "Loser Side", "Loser Elo Before", "Loser Elo After",
                    "Innings Played", "Game ID", "Game Start Date", "Game End Date", "Game Time Length (Minutes)", "Stadium"]]

if teams == 1:
    teams = True
    for h in range(2):
        for i in range(9):
            if h < 1:
                export_list[0].append(f"Winner Roster {i}")
            else:
                export_list[0].append(f"Loser Roster {i}")

def parse_games_endpoint(url):
    print(url)
    r = requests.get(url)
    jsonObj = r.json()

    print("RioWeb Request Complete, Excel File in Progess")
    print("This will take a few minutes...")
    last_unix_time = None
    intermediate_list = []
    for event in jsonObj["games"]:
        intermediate_list = []
        if event["away_score"] > event["home_score"]:
            winner, loser = "away", "home"
        else:
            winner, loser = "home", "away"

        intermediate_list.extend([
            event[f"{winner}_user"],
            event[f"{winner}_captain"],
            event[f"{winner}_score"],
            winner,
            event["winner_incoming_elo"],
            event["winner_result_elo"],
            event[f"{loser}_user"],
            event[f"{loser}_captain"],
            event[f"{loser}_score"],
            loser,
            event["loser_incoming_elo"],
            event["loser_result_elo"],
            event["innings_played"],
            event["game_id"],
            str(datetime.datetime.fromtimestamp(event["date_time_start"])),
            str(datetime.datetime.fromtimestamp(event["date_time_end"])),
            str((event["date_time_end"] - event["date_time_start"])/60),
            RioStatsConverter.stadium_id(event["stadium"]),
            ])

        last_unix_time = event["date_time_start"]
        print(last_unix_time)

        if not teams:
            export_list.append(intermediate_list)
            continue

        rosters = [event["away_roster"], event["home_roster"]] if winner == "away" else [event["home_roster"],
                                                                                         event["away_roster"]]
        for roster in rosters:
            for player in roster.values():
                intermediate_list.append(RioStatsConverter.char_id(player))

        export_list.append(intermediate_list)

    print(export_list)
    return export_list, len(jsonObj["games"]), last_unix_time

def limit_games_chunking():
    complex_url = f"{simple_url[:-5]}500&include_teams=1"
    export_list, len, last_unix_time = parse_games_endpoint(complex_url)
    print(export_list, len, last_unix_time)
    while len == 500:
        more_complex_url = f"{complex_url}&end_time={last_unix_time}"
        export_list, len, last_unix_time = parse_games_endpoint(more_complex_url)
        print(len)

    return export_list

if not teams:
    Export_List_To_Excel.export_to_excel(parse_games_endpoint(simple_url)[0], filepath)
else:
    Export_List_To_Excel.export_to_excel(limit_games_chunking(), filepath)

print("Complete")