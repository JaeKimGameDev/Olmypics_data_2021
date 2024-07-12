import pandas as pd
import numpy as np
import plotly.express as px
import csv
import plotly.graph_objects as go

# find chance or pattern that will ensure to win a medal in sporting events

# Let's find all the necessary data I need from past olympics and find a pattern
# find data of atheletes that win multiple events back to back (swimming 100m and 200m, etc) believe strong swimmers have won multiple events
# AND through olympic history, how long can they stay in shape and win again for the next olympics
# at what age do athletes drop off and have a very low chance of winning
# is there a correlation to winning between the coach and player? Does the coach have a history of training multiple winning atheletes?
# does origin play a significant role in the types of sports they win constantly

# then use this data to compare to the data in paris 2024 summer olympics

# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
# Dataset from 1896-2014, use this data to find athletes that won medals, and extract what we need

# organized by age and gender
def remakeCSVFile2():

    # read the data in our local PC
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\PycharmProjects\Hackathon_Official\athlete_Dataset.csv')

    # drop tables if needed, improves efficiency, placeholder
    athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1970")

    pd.set_option('display.max_rows', None)

    # irrelevent from Paris 2024 Olympic website vs that didn't translate to dataset I downloaded, returns 0, find name he may have renamed too
    # Artistic Gymnastics, Artistic Swimming, Basketball 3x3, Breaking, Canoe Slalom, Canoe Sprint
    # Cycling BMX Freestyle, Cycling BMX Racing, Cycling Mountain Bike, Cycling Road, Cycling Track, Equestrian
    # Marathon Swimming, Skateboarding, Sport Climbing, Surfing, Trampoline
    listOfSports = ['Archery','Gymnastics','Athletics','Badminton',
                    'Basketball','Beach Volleyball','Boxing',
                    'Diving','Fencing','Football','Golf',
                    'Handball','Hockey','Judo','Modern Pentathlon',
                    'Rhythmic Gymnastics','Rowing','Rugby Sevens',
                    'Sailing','Shooting','Swimming','Table Tennis',
                    'Taekwondo','Tennis','Triathlon','Volleyball',
                    'Water Polo','Weightlifting','Wrestling']

    # create a new csv file with data that is organized the way we want it
    with open('newAthleteData2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["sport", "gender", "age<25", "age(25-30)", "age>30", "totalAthletes"]
        writer.writerow(field)

        # adjust as needed, find the relevant data here through the sports, sorting by country, age and gender
        # TODO print out the unique strings of different sports from csv TODO
        for i in range(len(listOfSports)):
            # using * as a way to make the data more easily readable for the person
            print("******************************", listOfSports[i], "data from 1970 to 2014 ******************************\n")

            maleUnder25 = len(athleteData.query("Age < 25 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))
            male25To30 = len(athleteData.query("Age >= 25 & Sex == 'M' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
            maleOver30 = len(athleteData.query("Age > 30 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))

            print("Gender: Male")
            print("Athletes age <= 25 that won a medal: ", maleUnder25)
            print("Athletes age 26 to 30 that won a medal: ", male25To30)
            print("Athletes age > 31 that won a medal: ", maleOver30, "\n")

            totalAthletesMen = maleUnder25 + male25To30 + maleOver30

            writer.writerow([listOfSports[i], "m", maleUnder25, male25To30, maleOver30, totalAthletesMen])

            femaleUnder25 = len(athleteData.query("Age < 25 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))
            female25To30 = len(athleteData.query("Age >= 25 & Sex == 'F' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
            femaleOver30 = len(athleteData.query("Age > 30 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))

            print("Gender: Females")
            print("Athletes age <= 25 that won a medal: ", femaleUnder25)
            print("Athletes age 26 to 30 that won a medal: ", female25To30)
            print("Athletes age > 31 that won a medal: ", femaleOver30, "\n")

            totalAthletesFemale = femaleUnder25 + female25To30 + femaleOver30

            writer.writerow([listOfSports[i], "f", femaleUnder25, female25To30, femaleOver30, totalAthletesFemale])

    return

def makeGraph2():
    # read the data in our local PC
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\PycharmProjects\Hackathon_Official\newAthleteData2.csv')

    y = [athleteDataFile["age<25"], athleteDataFile["age(25-30)"], athleteDataFile["age>30"]]
    x = [athleteDataFile["sport"], athleteDataFile["gender"]]
    fig = go.Figure()

    barName = ["Age < 25", "Age 25-30", "Age > 30"]
    for i in range(3):
        fig.add_bar(
            x=x,
            y=y[i],
            name=barName[i])

    fig.update_layout(
        barmode="group",
        title_text="Prediction of Medalists for Olympics 2024 Paris",
        xaxis_title="Sport",
        yaxis_title="Number of Athletes",
        legend_title_text="Age Group")
    fig.show()

    return

def main():
    # remakeCSVFile()
    # makeGraph()

    remakeCSVFile2()
    makeGraph2()

    return

if __name__ == "__main__":
    main()








# did not use**********************************************************************************************************
# organized by country, age and gender DID NOT USE THIS ONE
def remakeCSVFile():

    # this is used for print out relevant data of medals that needs to be won in total for a country to be added to data
    minimumMedalForData = 40

    # used to capture data for other countries that doesn't achieve minimum medals
    otherCountriesMaleUnder25 = 0
    otherCountriesMale25To30 = 0
    otherCountriesMaleOver30 = 0
    otherCountriesFemaleUnder25 = 0
    otherCountriesFemale25To30 = 0
    otherCountriesFemaleOver30 = 0

    # read the data in our local PC
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\PycharmProjects\Hackathon_Official\athlete_Dataset.csv')

    # drop tables if needed, improves efficiency, placeholder
    athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1970")

    pd.set_option('display.max_rows', None)

    # get a list of unique countries for teams in the Olympics that participated
    athleteCountry = athleteData['Team'].unique()

    # irrelevent from Paris 2024 Olympic website vs that didn't translate to dataset I downloaded, returns 0, find name he may have renamed too
    # Artistic Gymnastics, Artistic Swimming, Basketball 3x3, Breaking, Canoe Slalom, Canoe Sprint
    # Cycling BMX Freestyle, Cycling BMX Racing, Cycling Mountain Bike, Cycling Road, Cycling Track, Equestrian
    # Marathon Swimming, Skateboarding, Sport Climbing, Surfing, Trampoline
    listOfSports = ['Archery','Gymnastics','Athletics','Badminton',
                    'Basketball','Beach Volleyball','Boxing',
                    'Diving','Fencing','Football','Golf',
                    'Handball','Hockey','Judo','Modern Pentathlon',
                    'Rhythmic Gymnastics','Rowing','Rugby Sevens',
                    'Sailing','Shooting','Swimming','Table Tennis',
                    'Taekwondo','Tennis','Triathlon','Volleyball',
                    'Water Polo','Weightlifting','Wrestling']

    # create a new csv file with data that is organized the way we want it
    with open('newAthleteData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["sport", "country", "gender", "age<25", "age(25-30)", "age>30"]
        writer.writerow(field)

        # adjust as needed, find the relevant data here through the sports, sorting by country, age and gender
        # TODO print out the unique strings of different sports from csv TODO
        for i in range(len(listOfSports)):
            # using * as a way to make the data more easily readable for the person
            print("******************************", listOfSports[i], "data from 1970 to 2014 ******************************\n")

            # reset the data for each sporting event
            otherCountriesMaleUnder25 = 0
            otherCountriesMale25To30 = 0
            otherCountriesMaleOver30 = 0

            otherCountriesFemaleUnder25 = 0
            otherCountriesFemale25To30 = 0
            otherCountriesFemaleOver30 = 0

            for j in range(len(athleteCountry)):

                # TODO, never use try and except, this is a special case. Bandage fix (bad practice) because of ' in some countries ex. Cote d'Ivoire. break the program (makes the string into "Cote d'Ivoire" for query
                try:
                    maleUnder25 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age < 25 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))
                    male25To30 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age >= 25 & Sex == 'M' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
                    maleOver30 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age > 30 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))

                    totalMaleMedalists = maleUnder25 + male25To30 + maleOver30

                    # this is used to clean up the data, we don't want a dataset where it is too spread across
                    # TODO must create a dataset for 'others' where the rest of the data gets accumulated here to show client TODO
                    if (totalMaleMedalists >= minimumMedalForData):
                        print("Country Team: " + athleteCountry[j] + ", Gender: Male")
                        print("Athletes age <= 25 that won a medal: ", maleUnder25)
                        print("Athletes age 26 to 30 that won a medal: ", male25To30)
                        print("Athletes age > 31 that won a medal: ", maleOver30, "\n")

                        writer.writerow([listOfSports[i], athleteCountry[j], "m", maleUnder25, male25To30, maleOver30])

                    else:
                        # TODO build off this if time is given TODO
                        # check if the athlete is relevent, (participating in next olympics, this case 2024 Paris), if this medalists even just one from this team had won)
                        # we can check data if he/she has a chance to win another based on cross referencing data from age observation of peak athleticism
                        # make note or a special mention, no reason to include on the bar graph though
                        # to build on this, we would comb through the current data on this sport and see the relevence on the age incase he has a higher chance to compete for a medal
                        # thinking about it, this is a dataset to 2014, 2024 Paris would be too far away to be relevent, for future implementation and datasets I guess
                        otherCountriesMaleUnder25 = otherCountriesMaleUnder25 + maleUnder25
                        otherCountriesMale25To30 = otherCountriesMale25To30 + male25To30
                        otherCountriesMaleOver30 = otherCountriesMaleOver30 + maleOver30

                    femaleUnder25 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age < 25 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))
                    female25To30 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age >= 25 & Sex == 'F' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
                    femaleOver30 = len(athleteData.query("Team == '" + athleteCountry[j] + "' & Age > 30 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))

                    totalFemaleMedalists = femaleUnder25 + female25To30 + femaleOver30

                    # this is used to clean up the data, we don't want a dataset where it is too spread across
                    # TODO must create a dataset for 'others' where the rest of the data gets accumulated here to show client TODO
                    if (totalFemaleMedalists >= minimumMedalForData):
                        print("Country Team: " + athleteCountry[j] + ", Gender: Females")
                        print("Athletes age <= 25 that won a medal: ", femaleUnder25)
                        print("Athletes age 26 to 30 that won a medal: ", female25To30)
                        print("Athletes age > 31 that won a medal: ", femaleOver30, "\n")

                        writer.writerow([listOfSports[i], athleteCountry[j], "f", femaleUnder25, female25To30, femaleOver30])

                    else:
                        # TODO build off this if time is given TODO
                        # check if the athlete is relevent, (participating in next olympics, this case 2024 Paris), if this medalists even just one from this team had won)
                        # we can check data if he/she has a chance to win another based on cross referencing data from age observation of peak athleticism
                        # make note or a special mention, no reason to include on the bar graph though
                        # to build on this, we would comb through the current data on this sport and see the relevence on the age incase he has a higher chance to compete for a medal
                        # thinking about it, this is a dataset to 2014, 2024 Paris would be too far away to be relevent, for future implementation and datasets I guess
                        otherCountriesFemaleUnder25 = otherCountriesFemaleUnder25 + femaleUnder25
                        otherCountriesFemale25To30 = otherCountriesFemale25To30 + female25To30
                        otherCountriesFemaleOver30 = otherCountriesFemaleOver30 + femaleOver30

                # TODO love to optimize this in the future TODO
                except:
                    # some string has been inputted as "" instead of ' given ' was used in the string, ex. Cote d'Ivoire. break the program
                    # create a new word without '
                    newWord = ""
                    for letter in athleteCountry[j]:
                        if letter == "'":
                            continue
                        else:
                            newWord = newWord + letter
                    athleteTeam = len(athleteData.query("Team == '" + newWord + "'"))

                    maleUnder25 = len(athleteData.query("Team == '" + newWord + "' & Age < 25 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))
                    male25To30 = len(athleteData.query("Team == '" + newWord + "' & Age >= 25 & Sex == 'M' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
                    maleOver30 = len(athleteData.query("Team == '" + newWord + "' & Age > 30 & Sex == 'M' & Sport == '" + listOfSports[i] + "'"))

                    totalMaleMedalists = maleUnder25 + male25To30 + maleOver30

                    # this is used to clean up the data, we don't want a dataset where it is too spread across
                    # TODO must create a dataset for 'others' where the rest of the data gets accumulated here to show client TODO
                    if (totalMaleMedalists >= minimumMedalForData):
                        print("Country Team: " + newWord + ", Gender: Males")
                        print("Athletes age <= 25 that won a medal: ", maleUnder25)
                        print("Athletes age 26 to 30 that won a medal: ", male25To30)
                        print("Athletes age > 31 that won a medal: ", maleOver30, "\n")

                        writer.writerow([listOfSports[i], athleteCountry[j], "m", maleUnder25, male25To30, maleOver30])

                    else:
                        # TODO build off this if time is given TODO
                        # check if the athlete is relevent, (participating in next olympics, this case 2024 Paris), if this medalists even just one from this team had won)
                        # we can check data if he/she has a chance to win another based on cross referencing data from age observation of peak athleticism
                        # make note or a special mention, no reason to include on the bar graph though
                        # to build on this, we would comb through the current data on this sport and see the relevence on the age incase he has a higher chance to compete for a medal
                        # thinking about it, this is a dataset to 2014, 2024 Paris would be too far away to be relevent, for future implementation and datasets I guess
                        otherCountriesMaleUnder25 = otherCountriesMaleUnder25 + maleUnder25
                        otherCountriesMale25To30 = otherCountriesMale25To30 + male25To30
                        otherCountriesMaleOver30 = otherCountriesMaleOver30 + maleOver30

                    # printout the total participants that won medals as a whole that did not meet the threshold

                    femaleUnder25 = len(athleteData.query("Team == '" + newWord + "' & Age < 25 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))
                    female25To30 = len(athleteData.query("Team == '" + newWord + "' & Age >= 25 & Sex == 'F' & Age <= 30 & Sport == '" + listOfSports[i] + "'"))
                    femaleOver30 = len(athleteData.query("Team == '" + newWord + "' & Age > 30 & Sex == 'F' & Sport == '" + listOfSports[i] + "'"))

                    totalFemaleMedalists = femaleUnder25 + female25To30 + femaleOver30

                    # this is used to clean up the data, we don't want a dataset where it is too spread across
                    # TODO must create a dataset for 'others' where the rest of the data gets accumulated here to show client TODO
                    if (totalFemaleMedalists >= minimumMedalForData):
                        print("Country Team: " + newWord + ", Gender: Females")
                        print("Athletes age <= 25 that won a medal: ", femaleUnder25)
                        print("Athletes age 26 to 30 that won a medal: ", female25To30)
                        print("Athletes age > 31 that won a medal: ", femaleOver30, "\n")

                        writer.writerow([listOfSports[i], athleteCountry[j], "f", femaleUnder25, female25To30, femaleOver30])

                    else:
                        # TODO build off this if time is given TODO
                        # check if the athlete is relevent, (participating in next olympics, this case 2024 Paris), if this medalists even just one from this team had won)
                        # we can check data if he/she has a chance to win another based on cross referencing data from age observation of peak athleticism
                        # make note or a special mention, no reason to include on the bar graph though
                        # to build on this, we would comb through the current data on this sport and see the relevence on the age incase he has a higher chance to compete for a medal
                        # thinking about it, this is a dataset to 2014, 2024 Paris would be too far away to be relevent, for future implementation and datasets I guess
                        otherCountriesFemaleUnder25 = otherCountriesFemaleUnder25 + femaleUnder25
                        otherCountriesFemale25To30 = otherCountriesFemale25To30 + female25To30
                        otherCountriesFemaleOver30 = otherCountriesFemaleOver30 + femaleOver30

            # printing out the dataset for all the other countries as one that did not meet the minimum medals requirements here before moving onto the next sporting event
            print("Country Team: Other Countries, Gender: Male")
            print("Athletes age <= 25 that won a medal: ", otherCountriesMaleUnder25)
            print("Athletes age 26 to 30 that won a medal: ", otherCountriesMale25To30)
            print("Athletes age > 31 that won a medal: ", otherCountriesMaleOver30, "\n")

            writer.writerow([listOfSports[i], "OtherCountries", "m", otherCountriesMaleUnder25, otherCountriesMale25To30, otherCountriesMaleOver30])

            print("Country Team: Other Countries, Gender: Female")
            print("Athletes age <= 25 that won a medal: ", otherCountriesFemaleUnder25)
            print("Athletes age 26 to 30 that won a medal: ", otherCountriesFemale25To30)
            print("Athletes age > 31 that won a medal: ", otherCountriesFemaleOver30, "\n")

            writer.writerow([listOfSports[i], "OtherCountries", "f", otherCountriesFemaleUnder25, otherCountriesFemale25To30, otherCountriesFemaleOver30])

    # TODO, throw all the data into a csv file. Kills efficiency, learning opportunity
    # then create a horizontal bar graph
    # graph will show country, then define into 3 bars with 3 age groups
    # might have to take out country, might be too congested for the graph

    file.close()
    athleteDataFile.close()

    return

def makeGraph():
    # read the data in our local PC
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\PycharmProjects\Hackathon_Official\newAthleteData.csv')



    return