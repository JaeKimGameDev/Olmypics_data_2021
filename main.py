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

athleteDataFile.info()

# drop tables if needed, improves efficiency, placeholder
athleteData = athleteDataFile

# find athletes that won any medal and games that are in the summer, used 1980's and up for relevancy
athleteData = athleteData.query("Medal.notnull() & Season == 'Summer' & Year >= 1980")

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
    # prints % of athletes by age that won any medal
    # numOfAthletesTo25 = len(athleteData.query("Age <= 25 & Sport == '" + listOfSports[i] + "'"))
    # numOfAthletes26To30 = len(athleteData.query("Age > 25 & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
    # numOfAthletesFrom31 = len(athleteData.query("Age > 30 & Sport == '" + listOfSports[i] + "'"))
    # totalMedalWinners = numOfAthletesTo25 + numOfAthletes26To30 + numOfAthletesFrom31
    # numOfAthletesTo25 = round((numOfAthletesTo25/totalMedalWinners) * 100, 2)
    # numOfAthletes26To30 = round((numOfAthletes26To30 / totalMedalWinners) * 100, 2)
    # numOfAthletesFrom31 = round((numOfAthletesFrom31 / totalMedalWinners) * 100, 2)
    # print(listOfSports[i])
    # print("Athletes age <= 25 that won a medal: ", numOfAthletesTo25, "%")
    # print("Athletes age 26 to 30 that won a medal: ", numOfAthletes26To30, "%")
    # print("Athletes age > 31 that won a medal: ", numOfAthletesFrom31, "%")

    # query male medalists by age
    maleUnder25 = len(athleteData.query("Age < 25 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))
    male25To30 = len(athleteData.query("Age >= 25 & Sex == 'M' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
    maleOver30 = len(athleteData.query("Age > 30 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))

    # get total male medalists
    maleTotalMedalists = maleUnder25 + male25To30 + maleOver30
    if (maleTotalMedalists < 1):    # catch the ones that are 0, error for 0 athletes
        maleTotalMedalists = 1
        print("no male athletes participated in this event")

    # convert number of medalists by age to percentage
    maleUnder25 = round((maleUnder25/maleTotalMedalists) * 100, 2)
    male25To30 = round((male25To30/maleTotalMedalists) * 100, 2)
    maleOver30 = round((maleOver30/maleTotalMedalists) * 100, 2)

    print(listOfSports[i])
    print("Male athletes age <= 25 that won a medal: ", maleUnder25, "%")
    print("Male athletes age 26 to 30 that won a medal: ", male25To30, "%")
    print("Male athletes age > 31 that won a medal: ", maleOver30, "%")
    print("\n")  # newline to tidy it up

    femaleUnder25 = len(athleteData.query("Age < 25 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))
    female25To30 = len(athleteData.query("Age >= 25 & Sex == 'F' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
    femaleOver30 = len(athleteData.query("Age > 30 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))

    # get total female medalists
    femaleTotalMedalists = femaleUnder25 + female25To30 + femaleOver30

    if (femaleTotalMedalists < 1):    # catch the ones that are 0, error for 0 athletes
        femaleTotalMedalists = 1
        print("no female athletes participated in this event")

    # convert number of medalists by age to percentage
    femaleUnder25 = round((femaleUnder25/femaleTotalMedalists) * 100, 2)
    female25To30 = round((female25To30/femaleTotalMedalists) * 100, 2)
    femaleOver30 = round((femaleOver30/femaleTotalMedalists) * 100, 2)

    print("Female athletes age <= 25 that won a medal: ", femaleUnder25, "%")
    print("Female athletes age 26 to 30 that won a medal: ", female25To30, "%")
    print("Female athletes age > 31 that won a medal: ", femaleOver30, "%")

    print("\n") # newline to tidy it up

    # go further and base it on which medals? Country?





# not relevent now
# dataset used: https://www.kaggle.com/datasets/llui85/tokyo-2021-olympics-complete-grouped-by-type

# data is organized by
# "Aggregate",
# "Ceremony",
# "Competitor",
# "Discipline",
# "Event",
# "EventUnit",
# "Individual",
# "Medal",
# "MedalCount",
# "Organisation",
# "Participant",
# "Phase",
# "Result",
# "ScheduleItem",
# "ScheduleSession",
# "Stage",
# "SubEventUnit",
# "Venue"

# Opening JSON file
#f = open(r'C:\Users\Jae\Desktop\Olympic_Dataset\')

# returns JSON object as a dictionary
#data = jn.load(f)

# Iterating through the json list
# for i in data['Medal']:
#     print(i)

# Closing file
# f.close()