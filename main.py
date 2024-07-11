import pandas as pd
import csv
import numpy as np
import plotly.express as px
import json as jn

# algorithm, lets find all the necessary data I need from past olympics and find a pattern
# find data of atheletes that win multiple events back to back (swimming 100m and 200m, etc) believe strong swimmers have won multiple events
# AND through olympic history, how long can they stay in shape and win again for the next olympics
# at what age do athletes drop off and have a very low chance of winning
# is there a correlation to winning between the coach and player? Does the coach have a history of training multiple winning atheletes?
# does origin play a significant role in the types of sports they win constantly

# then use this data to compare to the data in paris 2024 summer olympics

# sports being play in paris 2024 find relevent data
# Archery
# Artistic Gymnastics
# Artistic Swimming
# Athletics
# Badminton
# Basketball
# Basketball 3x3
# Beach Volleyball
# Boxing
# Breaking
# Canoe Slalom
# Canoe Sprint
# Cycling BMX Freestyle
# Cycling BMX Racing
# Cycling Mountain Bike
# Cycling Road
# Cycling Track
# Diving
# Equestrian
# Fencing
# Football
# Golf
# Handball
# Hockey
# Judo
# Marathon Swimming
# Modern Pentathlon
# Rhythmic Gymnastics
# Rowing
# Rugby Sevens
# Sailing
# Shooting
# Skateboarding
# Sport Climbing
# Surfing
# Swimming
# Table Tennis
# Taekwondo
# Tennis
# Trampoline
# Triathlon
# Volleyball
# Water Polo
# Weightlifting
# Wrestling

# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
# Dataset from 1896-2014, use this data to find athletes that won medals, and extract what we need

athleteDataFile = pd.read_csv(r'C:\Users\Jae\Desktop\Olympic_Dataset\athlete_Dataset.csv')

athleteDataFile.info()

# drop tables if needed, improves efficiency, placeholder
athleteData = athleteDataFile

# find athletes that won Gold
#athleteData=athleteData[(athleteData['Medal'] == 'Gold')]

# find athletes that won any medal and games that are in the summer
#athleteData=athleteData[(athleteData['Medal'].notnull())]
#athleteData=athleteData[(athleteData['Season'] == 'Summer')]

# find athletes that won any medal and games that are in the summer, using query
athleteData = athleteData.query("Medal.notnull() & Season == 'Summer'")

#pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#print(athleteData[['Name', 'Games', 'Medal', 'Sport']])

listOfSports = ['Archery','Artistic Gymnastics','Artistic Swimming','Athletics','Badminton',
                'Basketball','Basketball 3x3','Beach Volleyball','Boxing','Breaking','Canoe Slalom',
                'Canoe Sprint','Cycling BMX Freestyle','Cycling BMX Racing','Cycling Mountain Bike',
                'Cycling Road','Cycling Track', 'Diving','Equestrian','Fencing','Football','Golf',
                'Handball','Hockey','Judo','Marathon Swimming','Modern Pentathlon','Rhythmic Gymnastics',
                'Rowing','Rugby Sevens','Sailing','Shooting','Skateboarding','Sport Climbing','Surfing',
                'Swimming','Table Tennis','Taekwondo','Tennis','Trampoline','Triathlon','Volleyball',
                'Water Polo','Weightlifting','Wrestling']

# adjust as needed, find the relevant data here through the sports, ex. find % of difference in ages
relevantAthleteData = []
# Creates a list of lists and organizes the data into sports categories (inefficient, change later)
for i in range(len(listOfSports)):
    relevantAthleteData = [listOfSports[i]]
    relevantAthleteData.append(athleteData.query("Age <= 25 & Sport == listOfSport[i]"))




    #relevantAthleteData.append([athleteData[(athleteData['Sport'] == listOfSports[i])]])









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