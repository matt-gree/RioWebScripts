import numpy as np
import csv

def simplifed_result(val, x_pos, z_pos):
    final_result_id_dict = {
        0: "None",
        1: "Strikeout",
        2: "Walk (BB)",
        3: "Walk HBP",
        4: "Out",
        5: "Caught (Anything Else)",
        6: "Caught (Line Drive)",
        7: "Single",
        8: "Double",
        9: "Triple",
        10: "HR",
        11: "Error Input",
        12: "Error Chem",
        13: "Bunt",
        14: "Sac Fly",
        15: "Ground Ball Double Play",
        16: "Foul Catch"
    }
    if val == 0:
        if x_pos != 0 and (abs(z_pos/x_pos) <= 1):
            return "Foul"
        else:
            return "Other"
    elif val == 7 or val == 8 or val == 9:
        return "Hit (excl. HR)"
    elif val == 10:
        return "HR"
    elif val == 4 or val == 5 or val == 6 or val == 15 or val == 16:
        return "Out"
    elif val in final_result_id_dict.keys():
        return "Other"
    else:
        return "Bad ID" + str(val)

def stick_frame_allignment(frame, input_val, hand_string):
    input_direction_dict = {
        0: "None",
        1: "Left",
        2: "Right",
        4: "Down",
        5: "Down and Left",
        6: "Down and Right",
        8: "Up",
        9: "Up and Left",
        10: "Up and Right"
    }
    if frame == 0:
        return "Bunt"
    if (frame > 1 and frame < 11) and (input_val in input_direction_dict.keys()):
        if input_val == 0 and frame != 6:
            return "No Stick Input"
        elif ((frame > 6) and (frame < 11) and input_val == 2) or ((frame > 1) and (frame < 6) and input_val == 1):
            if hand_string == "Left":
                return "Same"
            if hand_string == "Right":
                return "Opposite"
        elif ((frame > 6) and (frame < 11) and input_val == 1) or ((frame > 1) and (frame < 6) and input_val == 2):
            if hand_string == "Left":
                return "Opposite"
            if hand_string == "Right":
                return "Same"
    else:
        return "Bad ID: Frame:" + str(frame) + ", Stick Input: " + str(input_val)

def simplified_character(val):
    char_name_dict = {
        0: "Mario",
        1: "Luigi",
        2: "DK",
        3: "Diddy",
        4: "Peach",
        5: "Daisy",
        6: "Yoshi",
        7: "Baby Mario",
        8: "Baby Luigi",
        9: "Bowser",
        10: "Wario",
        11: "Waluigi",
        12: "Koopa(G)",
        13: "Toad(R)",
        14: "Boo",
        15: "Toadette",
        16: "Shy Guy(R)",
        17: "Birdo",
        18: "Monty",
        19: "Bowser Jr",
        20: "Paratroopa(R)",
        21: "Pianta(B)",
        22: "Pianta(R)",
        23: "Pianta(Y)",
        24: "Noki(B)",
        25: "Noki(R)",
        26: "Noki(G)",
        27: "Bro(H)",
        28: "Toadsworth",
        29: "Toad(B)",
        30: "Toad(Y)",
        31: "Toad(G)",
        32: "Toad(P)",
        33: "Magikoopa(B)",
        34: "Magikoopa(R)",
        35: "Magikoopa(G)",
        36: "Magikoopa(Y)",
        37: "King Boo",
        38: "Petey",
        39: "Dixie",
        40: "Goomba",
        41: "Paragoomba",
        42: "Koopa(R)",
        43: "Paratroopa(G)",
        44: "Shy Guy(B)",
        45: "Shy Guy(Y)",
        46: "Shy Guy(G)",
        47: "Shy Guy(Bk)",
        48: "Dry Bones(Gy)",
        49: "Dry Bones(G)",
        50: "Dry Bones(R)",
        51: "Dry Bones(B)",
        52: "Bro(F)",
        53: "Bro(B)",
        None: "None"
    }
    if val == 12 or val == 42:
        return "Koopa"
    elif val == 13 or val == 29 or val == 30 or val == 31 or val == 32:
        return "Toad"
    elif val == 43 or val == 20:
        return "Paratroopa"
    elif val == 16 or val == 44 or val == 45 or val == 46 or val == 47:
        return "Shy Guy"
    elif val == 21 or val == 22 or val == 23:
        return "Pianta"
    elif val == 24 or val == 25 or val == 26:
        return "Noki"
    elif val == 27 or val == 52 or val == 53:
        return "Bro"
    elif val == 33 or val == 34 or val == 35 or val == 36:
        return "Magikoopa"
    elif val == 48 or val == 49 or val == 50 or val == 51:
        return "Dry Bones"
    elif val in char_name_dict.keys():
        return char_name_dict[val]
    else:
        return "Bad ID: " + str(val)

def launch_angle(x_velo, y_velo, z_velo):
    return np.degrees(np.arctan2((y_velo), (np.sqrt(x_velo**2 + z_velo**2))))

def velo_to_mph(velo):
    return velo*60*2.24

def exit_velo(x_velo, y_velo, z_velo):
    return np.sqrt(x_velo**2+y_velo**2+z_velo**2)

def stat_lookup(char_id, stat_name):
    stat_obj = []
    with open("CharStats.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            stat_obj.append(row)
    return stat_obj[char_id+1][stat_obj[0].index(stat_name)]

def relevant_batting_power(type_of_swing, char_id):
    if type_of_swing == 1:
        return stat_lookup(char_id, "Slap Hit Power")
    elif type_of_swing == 2:
        return stat_lookup(char_id, "Charge Hit Power")
    elif type_of_swing == 4:
        return stat_lookup(char_id, "Bunting")

def traj(char_id, horiz0_or_vert1):
    string = stat_lookup(char_id, "Trajectory")
    string = string.strip(" ")
    string = string.split("/")
    return string[horiz0_or_vert1]

