import json
from pathlib import Path
import statistics
import pandas as pd
import matplotlib.pyplot as plt

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

#Counter for number of sessions
counter = 0

#Loop through all training sessions that contain data for wanted sport and extract heart rate variables
for session in trainingsessions:
    countAerk = 0   #variable for tracking time above aerobic treshold
    countAnak = 0   #variable for tracking time above anaerobic treshold
    pathsession = path + '\\' + session
    f = open(pathsession)
    data = json.load(f)
    
    for exercise in data['exercises']:
        #check for wanted sport
        if exercise['sport'] == sport:
            heartRate = exercise['samples']['heartRate']
            for sample in heartRate:
                if 'value' in sample and sample['value'] >= aerk:
                    countAerk += 1
                if 'value' in sample and sample['value'] >= anak:
                    countAnak += 1
            counter += 1
            timeAboveAerk = countAerk / len(heartRate)
            timeAboveAnak = countAnak / len(heartRate)
    if counter > 1: break

print(timeAboveAerk)
print(timeAboveAnak)

'''
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
'''    


