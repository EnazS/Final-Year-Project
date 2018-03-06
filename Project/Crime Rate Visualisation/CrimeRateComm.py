import numpy as np
import csv
import matplotlib.pyplot as plt

f = open('/home/zanesx/Desktop/CrimeRateInferenceWithBigData-master/CrimeRateInference_SourceCode/CrimeRateInference_python/data/demographics.csv')
reader_demo = csv.DictReader(f)
x = []
y = []  # y is crime rate vecctor
flag = 0
for row in reader_demo:
    x.append(int(row['Community #']))
    if int(row['Community #']) > flag:
        y.append(row['crime_rate'])
        flag += 1
y = np.asarray(y, dtype=np.float)

plt.ylim(0,0.5)
plt.xlim(1,77)
plt.xlabel('Communities')
plt.ylabel('Rate')
plt.plot(x,y)
plt.show()
