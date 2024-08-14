import pandas as pd
import csv
import plotly.express as px

# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results Dataset from 1896-2014

def remakeCSVFileByGender():
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\athlete_Dataset.csv')
    athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

    pd.set_option('display.max_rows', None)
    parisSports = ['Archery','Gymnastics','Athletics','Badminton','Basketball','Beach Volleyball','Boxing',
                    'Diving','Fencing','Football','Golf','Handball','Hockey','Judo','Modern Pentathlon',
                    'Rhythmic Gymnastics','Rowing','Rugby Sevens','Sailing','Shooting','Swimming','Table Tennis',
                    'Taekwondo','Tennis','Triathlon','Volleyball','Water Polo','Weightlifting','Wrestling']
    medalTypes = ['Gold', 'Silver', 'Bronze']

    # create a new csv file with data that is organized the way we want it
    with open('AthleteDataByGender.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Sport", "Gender", "Age<21", "Age(21-25)","Age(26-30)", "Age>30", "Medal"]
        writer.writerow(field)

        for sport in parisSports:
            for medal in medalTypes:
                maleUnder21 = len(athleteData.query("Age < 21 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                male21To25 = len(athleteData.query("Age > 20 & Age < 26 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                male26To30 = len(athleteData.query("Age > 25 & Age < 31 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleOver30 = len(athleteData.query("Age > 30 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport, "M", maleUnder21, male21To25, male26To30, maleOver30, medal])

                femaleUnder21 = len(athleteData.query("Age < 21 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                female21To25 = len(athleteData.query("Age > 20 & Age < 26 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                female26To30 = len(athleteData.query("Age > 25 & Age < 31 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleOver30 = len(athleteData.query("Age > 30 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport, "F", femaleUnder21, female21To25, female26To30, femaleOver30, medal])

    return
def remakeCSVFileByWeight():
    pd.set_option('display.max_rows', None)
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\athlete_Dataset.csv')
    athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

    parisSports = ['Archery','Gymnastics','Athletics','Badminton','Basketball','Beach Volleyball','Boxing',
                    'Diving','Fencing','Football','Golf','Handball','Hockey','Judo','Modern Pentathlon',
                    'Rhythmic Gymnastics','Rowing','Rugby Sevens','Sailing','Shooting','Swimming','Table Tennis',
                    'Taekwondo','Tennis','Triathlon','Volleyball','Water Polo','Weightlifting','Wrestling']
    medalTypes = ['Gold', 'Silver', 'Bronze']

    with open('AthleteDataByWeight.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Sport","Gender","Weight<60","Weight(60-70)","Weight(71-80)","Weight(81-90)","Weight>91","Medal"]
        writer.writerow(field)

        for sport in parisSports:
            for medal in medalTypes:
                maleWeightUnder60 = len(athleteData.query("Weight < 60 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleWeight60To70 = len(athleteData.query("Weight >= 60 & Weight <= 70 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleWeight71To80 = len(athleteData.query("Weight > 70 & Weight <= 80 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleWeight81To90 = len(athleteData.query("Weight > 80 & Weight <= 90 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleWeightOver90 = len(athleteData.query("Weight > 90 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport, "M", maleWeightUnder60, maleWeight60To70, maleWeight71To80, maleWeight81To90,maleWeightOver90,medal])

                femaleWeightUnder60 = len(athleteData.query("Weight < 60 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleWeight60To70 = len(athleteData.query("Weight >= 60 & Weight <= 70 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleWeight71To80 = len(athleteData.query("Weight > 70 & Weight <= 80 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleWeight81To90 = len(athleteData.query("Weight > 80 & Weight <= 90 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleWeightOver90 = len(athleteData.query("Weight > 90 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport,"F",femaleWeightUnder60,femaleWeight60To70,femaleWeight71To80,femaleWeight81To90,femaleWeightOver90,medal])
    return
def remakeCSVFileByHeight():
    pd.set_option('display.max_rows', None)
    athleteDataFile = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\athlete_Dataset.csv')
    athleteData = athleteDataFile.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

    parisSports = ['Archery','Gymnastics','Athletics','Badminton','Basketball','Beach Volleyball','Boxing',
                    'Diving','Fencing','Football','Golf','Handball','Hockey','Judo','Modern Pentathlon',
                    'Rhythmic Gymnastics','Rowing','Rugby Sevens','Sailing','Shooting','Swimming','Table Tennis',
                    'Taekwondo','Tennis','Triathlon','Volleyball','Water Polo','Weightlifting','Wrestling']
    medalTypes = ['Gold', 'Silver', 'Bronze']

    with open('AthleteDataByHeight.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Sport","Gender","Height<160","Height(160-170)","Height(171-180)","Height(181-190)","Height>190","Medal"]
        writer.writerow(field)

        for sport in parisSports:
            for medal in medalTypes:
                maleHeightUnder160 = len(athleteData.query("Height < 160 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleHeight160To170 = len(athleteData.query("Height >= 160 & Height <= 170 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleHeight171To180 = len(athleteData.query("Height > 170 & Height <= 180 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleHeight180To190 = len(athleteData.query("Height > 180 & Height <= 190 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                maleHeightOver190 = len(athleteData.query("Height > 190 & Sex == 'M' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport, "M", maleHeightUnder160, maleHeight160To170, maleHeight171To180, maleHeight180To190,maleHeightOver190,medal])

                femaleHeightUnder160 = len(athleteData.query("Height < 160 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleHeight160To170 = len(athleteData.query("Height >= 160 & Height <= 170 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleHeight171To180 = len(athleteData.query("Height > 170 & Height <= 180 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleHeight180To190 = len(athleteData.query("Height > 180 & Height <= 190 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))
                femaleHeightOver190 = len(athleteData.query("Height > 190 & Sex == 'F' & Sport == '" + sport + "' & Medal == '" + medal + "'"))

                writer.writerow([sport,"F",femaleHeightUnder160,femaleHeight160To170,femaleHeight171To180,femaleHeight180To190,femaleHeightOver190,medal])
    return

def barGraphByGender(gender):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\AthleteDataByGender.csv')
    df = df[df['Gender'] == gender.upper()]

    fig = px.histogram(df, x=df["Sport"],
                       y=[df["Age<21"],df["Age(21-25)"],df["Age(26-30)"],df["Age>30"]],
                       barmode='group')
    fig.update_layout(
        title='Number of Athletes that Won Medals by Age, Gender:(' + gender.upper() + ')',
        xaxis_title="Sports",
        yaxis_title="Number of Athletes",
        legend_title="Age Group")
    fig.show()
    return

def barGraphByHeight(gender):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\AthleteDataByHeight.csv')
    df = df[df['Gender'] == gender.upper()]

    fig = px.histogram(df, x=df["Sport"],
                       y=[df["Height<160"],df["Height(160-170)"],df["Height(171-180)"],df["Height(181-190)"],df["Height>190"]],
                       barmode='group')
    fig.update_layout(
        title='Number of Athletes that Won Medals by Height (Cm), Gender:(' + gender.upper() + ')',
        xaxis_title="Sports",
        yaxis_title="Number of Athletes",
        legend_title="Height Group in Cm")
    fig.show()
    return

def barGraphByWeight(gender):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\AthleteDataByWeight.csv')
    df = df[df['Gender'] == gender.upper()]
    fig = px.histogram(df, x=df["Sport"],
                       y=[df["Weight<60"],df["Weight(60-70)"],df["Weight(71-80)"],df["Weight(81-90)"],df["Weight>91"]],
                       barmode='group')
    fig.update_layout(
        title='Number of Athletes that Won Medals by Weight (Kg), Gender:(' + gender.upper() + ')',
        xaxis_title="Sports",
        yaxis_title="Number of Athletes",
        legend_title="Weight Group in Kg")
    fig.show()
    return

def scatterGraphBySport(activity,gender):
    pd.set_option('display.max_rows', None)
    df = pd.read_csv(r'C:\Users\Jae\Documents\GitHub\Olmypics_data_2021\athlete_Dataset.csv')

    df = df.query("Medal.notnull() & Season == 'Summer' & Year >= 1990")

    df = df.query("Sport == '" + activity + "' & Sex == '" + gender.upper() + "'")
    fig = px.scatter(df,x=df["Height"],
                        y=df["Age"],
                        color='Medal',
                        category_orders = {'Medal': ["Gold", "Silver", "Bronze"]},
                        color_discrete_sequence=["Gold","Silver","Brown"],
                        opacity=0.25)
    fig.update_layout(
        title= activity + " Medals Won, Age vs Height (Cm), Gender:(" + gender.upper() + ")",
        xaxis_title="Height (Cm)",
        yaxis_title="Age",
        legend_title="Medals")
    fig.show()
    return

def main():
    remakeCSVFileByGender()
    barGraphByGender("m")
    barGraphByGender("f")

    remakeCSVFileByHeight()
    barGraphByHeight("m")
    barGraphByHeight("f")

    remakeCSVFileByWeight()
    barGraphByWeight("m")
    barGraphByWeight("f")

    scatterGraphBySport("Swimming","m")
    scatterGraphBySport("Swimming","f")
    
    # parisSports = ['Archery','Gymnastics','Athletics','Badminton','Basketball','Beach Volleyball','Boxing',
    #                 'Diving','Fencing','Football','Golf','Handball','Hockey','Judo','Modern Pentathlon',
    #                 'Rhythmic Gymnastics','Rowing','Rugby Sevens','Sailing','Shooting','Swimming','Table Tennis',
    #                 'Taekwondo','Tennis','Triathlon','Volleyball','Water Polo','Weightlifting','Wrestling']
    # for sports in parisSports:
    #     scatterGraphBySport(sports, "m")
    #     scatterGraphBySport(sports, "f")


    return

if __name__ == "__main__":
    main()