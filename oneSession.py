import pandas as pd
import json
import matplotlib.pyplot as plt

#This script analyzes one session of playing roundnet

#Open file and define file path
f = open(r'C:\Users\Käyttäjä\koodit\pyyttoni\roundnet\roundnet\spiketreeni.json')
data = json.load(f)

#Add subject information to a table
tiedotdata = data['physicalInformationSnapshot']
tiedot = pd.DataFrame.from_dict(tiedotdata, orient='index')
print(tiedot)

#Extract aerobic and anaerobic tresholds
aerk = tiedot.loc['aerobicThreshold'][0]
anak = tiedot.loc['anaerobicThreshold'][0]

#Read and plot heart rate for each session.
#Add horizontal lines to represent aerobic and anaerobic tresholds
syke = data['exercises'][0]['samples']['heartRate']
sykedf = pd.DataFrame(syke)
'''
plt.plot(sykedf['dateTime'], sykedf['value'])
plt.ylim(0,200)
plt.axhline(aerk)
plt.axhline(anak)
plt.show()
'''

# Extract heart rate samples
samples = data['exercises'][0]['samples']['heartRate']
heart_rates = [sample['value'] for sample in samples]

# Calculate average heart rate
average_heart_rate = sum(heart_rates) / len(samples)

print("Average heart rate:", average_heart_rate)
print("Max heart rate:", max(heart_rates))