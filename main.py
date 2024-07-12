import pandas as pd
import numpy as np
import plotly.express as px

# Lets find all the necessary data I need from past olympics and find a pattern
# find data of atheletes that win multiple events back to back (swimming 100m and 200m, etc) believe strong swimmers have won multiple events
# AND through olympic history, how long can they stay in shape and win again for the next olympics
# at what age do athletes drop off and have a very low chance of winning
# is there a correlation to winning between the coach and player? Does the coach have a history of training multiple winning atheletes?
# does origin play a significant role in the types of sports they win constantly

# then use this data to compare to the data in paris 2024 summer olympics

# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
# Dataset from 1896-2014, use this data to find athletes that won medals, and extract what we need

athleteDataFile = pd.read_csv(r'C:\Users\Jae\Desktop\Olympic_Dataset\athlete_Dataset.csv')

#athleteDataFile.info()

# drop tables if needed, improves efficiency, placeholder
athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

# find athletes that won any medal and games that are in the summer, used 1980's and up for relevancy
#athleteData = athleteData.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

#pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#print(athleteData[['Name', 'Games', 'Medal', 'Sport']])
# irrelevent from Paris 2024 Olympic website vs that didn't translate to dataset I downloaded, returns 0, find name he may have renamed too
# Artistic Gymnastics, Artistic Swimming, Basketball 3x3, Breaking, Canoe Slalom, Canoe Sprint
# Cycling BMX Freestyle, Cycling BMX Racing, Cycling Mountain Bike, Cycling Road, Cycling Track, Equestrian
# Marathon Swimming, Skateboarding, Sport Climbing, Surfing, Trampoline
listOfSports = ['Archery','Gymnastics','Athletics','Badminton',
                'Basketball','Beach Volleyball','Boxing',
                'Diving','Fencing','Football','Golf',
                'Handball','Hockey','Judo','Modern Pentathlon','Rhythmic Gymnastics',
                'Rowing','Rugby Sevens','Sailing','Shooting',
                'Swimming','Table Tennis','Taekwondo','Tennis','Triathlon','Volleyball',
                'Water Polo','Weightlifting','Wrestling']

# adjust as needed, find the relevant data here through the sports, ex. find % of difference in ages
# TODO print out the unique strings of different sports from csv TODO
for i in range(len(listOfSports)):

    # query male medalists by age
    maleUnder25 = len(athleteData.query("Age < 25 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))
    male25To30 = len(athleteData.query("Age >= 25 & Sex == 'M' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
    maleOver30 = len(athleteData.query("Age > 30 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))

    print(listOfSports[i], "data from 1990 to 2014")
    print("Male athletes age <= 25 that won a medal: ", maleUnder25)
    print("Male athletes age 26 to 30 that won a medal: ", male25To30)
    print("Male athletes age > 31 that won a medal: ", maleOver30)
    print("\n")  # newline to tidy it up

    femaleUnder25 = len(athleteData.query("Age < 25 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))
    female25To30 = len(athleteData.query("Age >= 25 & Sex == 'F' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
    femaleOver30 = len(athleteData.query("Age > 30 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))

    print(listOfSports[i], "data from 1990 to 2014")
    print("Female athletes age <= 25 that won a medal: ", femaleUnder25)
    print("Female athletes age 26 to 30 that won a medal: ", female25To30)
    print("Female athletes age > 31 that won a medal: ", femaleOver30)

    print("\n") # newline to tidy it up

# go further and base it on which medals? Country?
athleteCountry = athleteData['Team'].unique()
#print(athleteCountry)

for j in range(len(athleteCountry)):
    print(athleteCountry[j])

    try:
        athleteTeam = len(athleteData.query("Team == '" + athleteCountry[j] + "'"))
    except:
        # some string has been inputted as "" instead of ' given ' was used in the string
        # create a new word without '
        newWord = ""
        for letter in athleteCountry[j]:
            if letter == "'":
                continue
            else:
                newWord = newWord + letter
        athleteTeam = len(athleteData.query("Team == '" + newWord + "'"))

    print(athleteTeam)





