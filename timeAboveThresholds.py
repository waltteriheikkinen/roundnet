import json
from pathlib import Path
import statistics

#This script analyses the time spent above aerobic and anaerobic thresholds during roundnet

#Add values depending on interest
sport = "TENNIS" #Roundnet games have been logged as Tennis in polar system
aerk = 150
anak = 175
hrMax = 195

# Directory path for dataset
path = r'C:\Users\Käyttäjä\Documents\generalData\roundnetanalyysipaketti'

directory = Path(path)
trainingsessions = []
# Loop through all files in the directory
for file in directory.iterdir():
    # Check if the file is a training file
    if file.is_file() and "training" in file.name:
        trainingsessions.append(file.name)

#Counter for number of sessions
counter = 0
aboveAerkList = []
aboveAnakList = []

#Loop through all training sessions that contain data for wanted sport and extract heart rate variables
for session in trainingsessions:
    countAerk = 0   #variable for tracking time above aerobic treshold
    countAnak = 0   #variable for tracking time above anaerobic treshold
    pathsession = path + '\\' + session
    f = open(pathsession)
    data = json.load(f)
    
    #Loop through selected data file
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
            timeAboveAerk = round(countAerk / len(heartRate) * 100, 1)
            timeAboveAnak = round(countAnak / len(heartRate) * 100, 1)
            aboveAerkList.append(timeAboveAerk)
            aboveAnakList.append(timeAboveAnak)
            #Print files with big values for closer examination
            #if timeAboveAerk > 10: 
                #print(session)
                #print(timeAboveAerk)
                #print(timeAboveAnak)


avgTimeAboveAerk = round(statistics.mean(aboveAerkList), 1)
stdTimeAboveAerk = round(statistics.stdev(aboveAerkList), 1)

avgTimeAboveAnak = round(statistics.mean(aboveAnakList), 1)
stdTimeAboveAnak = round(statistics.stdev(aboveAnakList), 1)

print("Number of sessions: ", counter)
print("")
print(f"Average time above aerobic threshold: {avgTimeAboveAerk} % sd: {stdTimeAboveAerk}")
print("")
print(f"Average time above anaerobic threshold: {avgTimeAboveAnak} % sd: {stdTimeAboveAnak}")
print("")
