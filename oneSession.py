import pandas as pd
import json
import matplotlib.pyplot as plt

#This script analyzes one session of playing roundnet from data extracted from Polar Flow

#Define path 
session = r"spiketreeni2.json"
path = r'C:\Users\Käyttäjä\koodit\pyyttoni\roundnet\roundnet'

#Open file
f = open(path + "\\" + session)
data = json.load(f)

#Add subject and session information to a table
tiedotdata = data['physicalInformationSnapshot']
tiedot = pd.DataFrame.from_dict(tiedotdata, orient='index')
tiedot = tiedot.drop('sleepGoal')
tiedot = tiedot.drop('functionalThresholdPower')
print(tiedot)
print("")

#Extract aerobic and anaerobic tresholds
aerk = tiedot.loc['aerobicThreshold'][0]
anak = tiedot.loc['anaerobicThreshold'][0]

#Create variables for calculating time above aerobic and anaerobic tresholds
countAerk = 0
countAnak = 0
heartRates = []
times = []
#Loop through datafile, extract heart rates and times, count time above aerobic and anaerobic tresholds
for exercise in data['exercises']:
    heartRate = exercise['samples']['heartRate']
    for sample in heartRate:
        if 'value' in sample:
            heartRates.append(sample['value'])
            times.append(sample['dateTime'])
            if sample['value'] >= aerk:
                countAerk += 1
            if sample['value'] >= anak:
                countAnak += 1
    timeAboveAerk = round(countAerk / len(heartRate) * 100, 1)
    timeAboveAnak = round(countAnak / len(heartRate) * 100, 1)


#print time above tresholds as percentage
print("Time above aerobic treshold: ", timeAboveAerk, "%")
print("Time above anaerobic treshold: ", timeAboveAnak, "%")


# Calculate average heart rate
average_heart_rate = sum(heartRates) / len(heartRates)

#Print results
print("Average heart rate:", round(average_heart_rate))
print("Session max heart rate:", max(heartRates))

#Plot heart rate for session
#Add horizontal lines to represent aerobic and anaerobic tresholds
plt.plot(times, heartRates)
plt.ylim(0,200)
plt.axhline(aerk)
plt.axhline(anak)
plt.show()


