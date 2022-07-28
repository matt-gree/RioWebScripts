import json
import os
import requests

import MattGreeRioWebExtensions
import RioStatsConverter
import MattGreeRioWebExtensions as RWext

import openpyxl
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

print("Enter '0' for stars-off data; '1' for stars-on")
stars = int(input())
print("Enter '0' for all data, '1' for ranked only")
ranked = int(input())

excel_filename = "/LandingData_"

url = "https://projectrio-api-1.api.projectrio.app/landing_data/?tag=Netplay"
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
wb = openpyxl.Workbook()
wb.save(filepath)

r = requests.get(url)
jsonObj = r.json()

print("RioWeb Request Complete, Excel File in Progess...")

export_list = [["Game ID", "Event Number", "Batter Username", "Batter Name", "Batter, Colors Combined", "Batting Hand", "Batter Horizontal Traj", "Batter Veritcal Traj", "Type of Swing", "Relevant Batting Power", "Type of Contact", "Frame of Contact", "Stick Input", "Stick Frame Aligment", "Charge Power Up", "Charge Power Down", "Chem Links",
                "Ball Angle", "x_velo (mph)", "y_velo (mph)", "z_velo (mph)", "Exit Velocity (mph)", "Launch Angle", "Max Height (m)", "Fielder Character Name", "Fielder Jump", "Fielder Position", "Fielding Hand", "Fielder X Pos (m)", "Fielder Y Pos (m)", "Fielder Z Pos (m)",  "Manual Select State",
                "Final Result", "Simplified Result", "ball_x_pos (m)", "ball_y_pos (m)", "ball_z_pos (m)", "Distance from fielder starting location to ball landing location", "Pitcher Username", "Pitcher Character Name", "Pitcher Cursed Ball"]]

for event in jsonObj["Data"]:
    export_list.append([
                        event["game_id"],
                        event["event_num"],
                        event["batter_username"],
                        RioStatsConverter.char_id(event["batter_char_id"]),
                        RWext.simplified_character(event["batter_char_id"]),
                        RioStatsConverter.hand_bool(event["batting_hand"]),
                        MattGreeRioWebExtensions.traj(event["batter_char_id"],0),
                        MattGreeRioWebExtensions.traj(event["batter_char_id"],1),
                        RioStatsConverter.type_of_swing_id(event["type_of_swing"]),
                        MattGreeRioWebExtensions.relevant_batting_power(event["type_of_swing"], event["batter_char_id"]),
                        RioStatsConverter.contact_id(event["type_of_contact"]),
                        event["frame_of_swing"],
                        RioStatsConverter.input_direction_id(event["stick_input"]),
                        RWext.stick_frame_allignment(event["frame_of_swing"], event["stick_input"], RioStatsConverter.hand_bool(event["batting_hand"])),
                        event["charge_power_up"],
                        event["charge_power_down"],
                        event["chem_links_ob"],
                        str(int(event["ball_angle"]) / 10),
                        RWext.velo_to_mph(event["x_velo"]),
                        RWext.velo_to_mph(event["y_velo"]),
                        RWext.velo_to_mph(event["z_velo"]),
                        RWext.velo_to_mph(RWext.exit_velo(event["x_velo"], event["y_velo"], event["z_velo"])),
                        RWext.launch_angle(event["x_velo"],event["y_velo"],event["z_velo"]),
                        event["ball_max_height"],
                        RioStatsConverter.char_id(event["fielder_char_id"]),
                        event["fielder_jump"],
                        RioStatsConverter.position_id(event["fielder_position"]),
                        RioStatsConverter.hand_bool(event["fielding_hand"]),
                        event["fielder_x_pos"],
                        event["fielder_y_pos"],
                        event["fielder_z_pos"],
                        RioStatsConverter.manual_select_id(event["manual_select_state"]),
                        RioStatsConverter.final_result_id(event["final_result"]),
                        RWext.simplifed_result(event["final_result"], event["ball_x_pos"], event["ball_z_pos"]),
                        event["ball_x_pos"],
                        event["ball_y_pos"],
                        event["ball_z_pos"],
                        MattGreeRioWebExtensions.distance_to_starting_coordinates(event["fielder_position"], event["ball_x_pos"], event["ball_z_pos"]),
                        event["pitcher_username"],
                        RioStatsConverter.char_id(event["pitcher_char_id"]),
                        MattGreeRioWebExtensions.stat_lookup(event["pitcher_char_id"],"0x2")
                        ])


def export_to_excel(stats, excel_file):
    wb = load_workbook(excel_file)
    sheets = wb.sheetnames
    ws1 = wb[sheets[0]]

    try:
        del ws1.tables["MarioBaseballStats"]
    except KeyError:
        table = True

    wb.save(excel_file)

    ws1.delete_rows(1, ws1.max_row)  # clears out old values in the excel sheet
    wb.save(excel_file)

    for row in stats:
        ws1.append(row)
    wb.save(excel_file)

    def column_string(n):
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string

    table_size = "A1:" + str(column_string(len(export_list[0]))) + str(len(export_list))
    tab = Table(displayName="MarioBaseballStats", ref=table_size)
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style
    ws1.add_table(tab)
    wb.save(excel_file)


export_to_excel(export_list, filepath)
print("Complete")

