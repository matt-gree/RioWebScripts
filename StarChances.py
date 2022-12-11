import RioStatLib
import json

file = str(input("Enter File Path: "))

with open(file, "r") as test:
    jsonObj = json.load(test)
    myStats = RioStatLib.StatObj(jsonObj)

all_events = myStats.events()
star_chance_oppurtunity = 0
star_chance = 0
home_defensive_star_chance_oppurtunities = 0
home_defensive_star_chance = 0
away_defensive_star_chance_oppurtunities = 0
away_defensive_star_chance = 0

for event in all_events:
    if event["Balls"] == 0 and event["Strikes"] == 0:
        if ("Runner 1B" not in event.keys()) and ("Runner 2B" not in event.keys()) and ("Runner 3B" not in event.keys()) and event["Event Num"] != 0 and ("Pitch" in event.keys()):
            star_chance_oppurtunity +=1
            if event["Half Inning"] == 0:
                home_defensive_star_chance_oppurtunities += 1
            else:
                away_defensive_star_chance_oppurtunities += 1
            if event["Star Chance"] == 1:
                star_chance += 1
                if event["Half Inning"] == 0:
                    home_defensive_star_chance += 1
                else:
                    away_defensive_star_chance += 1

print("Star Chance Opportunities: " + str(star_chance_oppurtunity) + "   " + "Star Chances: " + str(star_chance) + "   " + "Star Chance Rate: {:0.2f}%".format(float(100*star_chance/star_chance_oppurtunity)))
print("{} Defensive Star Chance Opportunities: ".format(myStats.player(0)) + str(home_defensive_star_chance_oppurtunities) + "   " "Star Chances: " + str(home_defensive_star_chance) + "   " + "Star Chance Rate: {:0.2f}%".format(float(100*home_defensive_star_chance/home_defensive_star_chance_oppurtunities)))
print("{} Defensive Star Chance Opportunities: ".format(myStats.player(1)) + str(away_defensive_star_chance_oppurtunities) + "   " "Star Chances: " + str(away_defensive_star_chance) + "   " + "Star Chance Rate: {:0.2f}%".format(float(100*away_defensive_star_chance/away_defensive_star_chance_oppurtunities)))
