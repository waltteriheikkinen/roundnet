import pandas as pd
import json
import matplotlib.pyplot as plt
from pathlib import Path
import statistics

#Add values depending on interest
sport = "TENNIS"
aerk = 150
anak = 175
hrMax = 195

# Directory path for dataset
path = r'C:\Users\Käyttäjä\Documents\generalData\polar-user-data-export_923497a7-d67d-4c58-a451-cc9d6c40244b'

directory = Path(path)
trainingsessions = []
# Loop through all files in the directory
for file in directory.iterdir():
    # Check if the file is a training file
    if file.is_file() and "training" in file.name:
        trainingsessions.append(file.name)


counter = 0
heartRatesMin = []
heartRatesAvg = []
heartRatesMax = []

#Loop through all training sessions that contain data for wanted sport and extract heart rate variables
for session in trainingsessions:
    pathsession = path + '\\' + session
    f = open(pathsession)
    data = json.load(f)
    
    for exercise in data['exercises']:
        #check for wanted sport
        if exercise['sport'] == sport:
            heartRatesMin.append(exercise['heartRate']['min'])
            heartRatesAvg.append(exercise['heartRate']['avg'])
            heartRatesMax.append(exercise['heartRate']['max'])
            counter += 1


avgMin = round(statistics.mean(heartRatesMin))
stdMin = round(statistics.stdev(heartRatesMin))

avgAvg = round(statistics.mean(heartRatesAvg))
stdAvg = round(statistics.stdev(heartRatesAvg))

avgMax = round(statistics.mean(heartRatesMax))
stdMax = round(statistics.stdev(heartRatesMax))

print("")
print("subject aerobic treshold: ", aerk)
print("subject anaerobic treshold: ", anak)
print("subject maximum heart rate: ", hrMax)
print("")
print("Number of sessions: ", counter)
print("")
print(f"Average minimum heart rate: {avgMin}, sd: {stdMin}")
print("")
print(f"Average heart rate: {avgAvg}, sd: {stdAvg}")
print("")
print(f"Average maximum heart rate: {avgMax}, sd: {stdMax}")
print("")
    


