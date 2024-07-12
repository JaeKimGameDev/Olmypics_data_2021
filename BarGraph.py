import pandas as pd
import numpy as np
import plotly.express as px
import csv
import plotly.graph_objects as go

# read the data in our local PC
athleteDataFile = pd.read_csv(r'C:\Users\Jae\PycharmProjects\Hackathon_Official\newAthleteData2.csv')

y = [athleteDataFile["age<25"],athleteDataFile["age(25-30)"],athleteDataFile["age>30"]]
x = [athleteDataFile["sport"],athleteDataFile["gender"]]
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
	legend_title_text = "Age Group")
fig.show()



