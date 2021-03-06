import re
import numpy as np


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data = sorted(data)


currId = -1
sleep = 0
wake = 0

analytics={}

def newrow():
    return np.array([0]*60)

for line in data:
    timestamp = re.match(r'\[\d{4}-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)', line)
    month, date, hour, minutes, description = timestamp.groups()
    minutes = int(minutes)
    
    if 'Guard' in description:
        m = re.match(r'Guard #(\d*) begins shift', description)
        currId = m.groups()[0]
        analytics.setdefault(currId, newrow())
    elif 'sleep' in description:
        sleep = minutes
    elif 'wakes' in description:
        analytics[currId][sleep:minutes] += 1


s=sorted(analytics, key=lambda x: sum(analytics[x]))
print(s[-10:])
sleepy = max(analytics, key=lambda x: sum(analytics[x]))
print('Guard ID:', sleepy)
print(sum(analytics[sleepy]), analytics[sleepy])
m = max(range(60), key=lambda index: analytics[sleepy][index])
print('Minute:', m)

print('Product:', int(sleepy) * int(m))
        
    



