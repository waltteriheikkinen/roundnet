import json
from pathlib import Path
import statistics

'''
This script analyses the time spent above aerobic and anaerobic thresholds during roundnet
by iterating through a data dump from polar flow. Script goes through all files in the dump
and collects the files which have been specified by certain sport.
'''

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
heartRatesMin = []
heartRatesAvg = []
heartRatesMax = []
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
            #Add heart rate data to lists
            heartRatesMin.append(exercise['heartRate']['min'])
            heartRatesAvg.append(exercise['heartRate']['avg'])
            heartRatesMax.append(exercise['heartRate']['max'])

            #Add single datapoints to lists to calculate percentages
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


avgMin = round(statistics.mean(heartRatesMin))
stdMin = round(statistics.stdev(heartRatesMin))

avgAvg = round(statistics.mean(heartRatesAvg))
stdAvg = round(statistics.stdev(heartRatesAvg))

avgMax = round(statistics.mean(heartRatesMax))
stdMax = round(statistics.stdev(heartRatesMax))

avgTimeAboveAerk = round(statistics.mean(aboveAerkList), 1)
stdTimeAboveAerk = round(statistics.stdev(aboveAerkList), 1)

avgTimeAboveAnak = round(statistics.mean(aboveAnakList), 1)
stdTimeAboveAnak = round(statistics.stdev(aboveAnakList), 1)


print(f"{'Subject aerobic threshold:':<45} {aerk}")
print(f"{'Subject anaerobic threshold:':<45} {anak}")
print(f"{'Subject maximum heart rate:':<45} {hrMax}")
print("")
print(f"{'Number of sessions:':<45} {counter}")
print("")
print(f"{'Average minimum heart rate:':<45} {avgMin}{",":<4} sd: {stdMin}")
print(f"{'Average heart rate:':<45} {avgAvg}{",":<3} sd: {stdAvg}")
print(f"{'Average maximum heart rate:':<45} {avgMax}{",":<3} sd: {stdMax}")
print("")
print(f"{'Average time above aerobic threshold:':<45} {avgTimeAboveAerk} %, sd: {stdTimeAboveAerk}")
print(f"{'Average time above anaerobic threshold:':<45} {avgTimeAboveAnak} %, sd: {stdTimeAboveAnak}")
print("")

