import math

def char_id(val):
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
    if val in char_name_dict.keys():
        return char_name_dict[val]
    else:
        return "Bad ID: " + str(val)


def stadium_id(val):
    stadium_id_dict = {
        0: "Mario Stadium",
        1: "Bowser's Castle",
        2: "Wario's Palace",
        3: "Yoshi's Island",
        4: "Peach's Garden",
        5: "DK's Jungle",
        6: "Toy Field"
    }
    if val in stadium_id_dict.keys():
        return stadium_id_dict[val]
    else:
        return "Bad ID: " + str(val)


def contact_id(val):
    contact_id_dict = {
        255: "Miss",
        0: "Sour - Left",
        1: "Nice - Left",
        2: "Perfect",
        3: "Nice - Right",
        4: "Sour - Right"
    }
    if val in contact_id_dict.keys():
        return contact_id_dict[val]
    else:
        return "Bad ID: " + str(val)


def hand_id(val):
    hand_id_dict = {
        0: "Right",
        1: "Left"
    }
    if val in hand_id_dict.keys():
        return hand_id_dict[val]
    else:
        return "Bad ID: " + str(val)


def hand_bool(bool):
    hand_bool_dict = {
        True: "Left",
        False: "Right"
    }
    if bool in hand_bool_dict.keys():
        return hand_bool_dict[bool]
    else:
        return "Bad ID: " + str(bool)


def input_direction_id(val):
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
    if val in input_direction_dict.keys():
        return input_direction_dict[val]
    else:
        return "Bad ID: " + str(val)


def pitch_type_id(val):
    pitch_type_dict = {
        0: "Curve",
        1: "Charge",
        2: "ChangeUp"
    }
    if val in pitch_type_dict.keys():
        return pitch_type_dict[val]
    else:
        return "Bad ID: " + str(val)


def charge_pitch_id(val):
    charge_type_dict = {
        0: "N/A",
        2: "Slider",
        3: "Perfect"
    }
    if val in charge_type_dict.keys():
        return charge_type_dict[val]
    else:
        return "Bad ID: " + str(val)


def type_of_swing_id(val):
    type_of_swing_dict = {
        0: "None",
        1: "Slap",
        2: "Charge",
        3: "Star",
        4: "Bunt"
    }
    if val in type_of_swing_dict.keys():
        return type_of_swing_dict[val]
    else:
        return "Bad ID: " + str(val)


def position_id(val):
    position_id_dict = {
        0: "P",
        1: "C",
        2: "1B",
        3: "2B",
        4: "3B",
        5: "SS",
        6: "LF",
        7: "CF",
        8: "RF",
        255: "Inv",
        None: "None"
    }
    if val in position_id_dict.keys():
        return position_id_dict[val]
    else:
        return "Bad ID: " + str(val)


def fielder_actions_id(val):
    fielder_actions_dict = {
        0: "None",
        2: "Sliding",
        3: "Walljump",
    }
    if val in fielder_actions_dict.keys():
        return fielder_actions_dict[val]
    else:
        return "Bad ID: " + str(val)


def fielder_bobbles_id(val):
    fielder_bobbles_dict = {
        0: "None",
        1: "Slide/stun lock",
        2: "Fumble",
        3: "Bobble",
        4: "Fireball",
        16: "Garlic knockout",
        255: "None"
    }
    if val in fielder_bobbles_dict.keys():
        return fielder_bobbles_dict[val]
    else:
        return "Bad ID: " + str(val)


def steal_type_id(val):
    steal_type_dict = {
        0: "None",
        1: "Ready",
        2: "Normal",
        3: "Perfect",
        55: "None"
    }
    if val in steal_type_dict.keys():
        return steal_type_dict[val]
    else:
        return "Bad ID: " + str(val)


def out_type_id(val):
    out_type_dict = {
        0: "None",
        1: "Caught",
        2: "Force",
        3: "Tag",
        4: "Force Back",
        16: "Strike-out",
    }
    if val in out_type_dict.keys():
        return out_type_dict[val]
    else:
        return "Bad ID: " + str(val)


def pitch_result_id(val):
    pitch_result_dict = {
        0: "HBP",
        1: "BB",
        2: "Ball",
        3: "Strike-looking",
        4: "Strike-swing",
        5: "Strike-bunting",
        6: "Contact",
        7: "Unknown"
    }
    if val in pitch_result_dict.keys():
        return pitch_result_dict[val]
    else:
        return "Bad ID: " + str(val)


def primary_contact_result_id(val):
    primary_contact_result_dict = {
        0: "Out",
        1: "Foul",
        2: "Fair",
        3: "Fielded",
        4: "Unknown"
    }
    if val in primary_contact_result_dict.keys():
        return primary_contact_result_dict[val]
    else:
        return "Bad ID: " + str(val)


def secondary_contact_result_id(val):
    secondary_contact_result_dict = {
        0: "Out-caught",
        1: "Out-force",
        2: "Out-tag",
        3: "foul",
        7: "Single",
        8: "Double",
        9: "Triple",
        10: "HR",
        11: "Error - Input",
        12: "Error - Chem",
        13: "Bunt",
        14: "SacFly",
        15: "Ground Ball Double Play",
        16: "Foul catch",
    }
    if val in secondary_contact_result_dict.keys():
        return secondary_contact_result_dict[val]
    else:
        return "Bad ID: " + str(val)


def final_result_id(val):
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
    if val in final_result_id_dict.keys():
        return final_result_id_dict[val]
    else:
        return "Bad ID: " + str(val)

def final_result_id(val):
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
    if val in final_result_id_dict.keys():
        return final_result_id_dict[val]
    else:
        return "Bad ID: " + str(val)

def pitch_result(val):
    pitch_result_id_dict = {
        0: "HBP",
        1: "BB",
        2: "Ball",
        3: "Strike-looking",
        4: "Strike-swing",
        5: "Strike-bunting",
        6: "Contact",
        7: "Unknown"
    }
    if val in pitch_result_id_dict.keys():
        return pitch_result_id_dict[val]
    else:
        return "Bad ID: " + str(val)


def manual_select_id(val):
    manual_select_dict = {
        0: "No Selected Char",
        1: "Selected Other Char",
        2: "Selected This Char",
        None: "None"
    }
    if val in manual_select_dict.keys():
        return manual_select_dict[val]
    else:
        return "Bad ID: " + str(val)

def distance_to_starting_coordinates(pos_str, x_coor, z_coor):
    fielder_starting_coordinates_dict = {
        "P": [0,18.4],
        "C": [0, -3.8],
        "1B": [18.5, 22],
        "2B": [11,36],
        "3B": [-18.5,22],
        "SS": [-11, 36],
        "LF": [-34, 60],
        "CF": [0,76],
        "RF": [34,60]
    }
    if pos_str in fielder_starting_coordinates_dict.keys():
        distance = math.sqrt((x_coor - fielder_starting_coordinates_dict[pos_str][0])**2
                             + (z_coor - fielder_starting_coordinates_dict[pos_str][1])**2)
        return distance
    else:
        return "Bad ID: " + str(pos_str)