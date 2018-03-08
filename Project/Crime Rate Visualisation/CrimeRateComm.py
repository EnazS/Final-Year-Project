import numpy as np
import csv
import matplotlib.pyplot as plt

f = open('/home/zanesx/Desktop/CrimeRateInferenceWithBigData-master/CrimeRateInference_SourceCode/CrimeRateInference_python/data/demographics.csv')
reader_demo = csv.DictReader(f)
x = []
y = []  # y is crime rate vector
flag = 0
for row in reader_demo:
    x.append(int(row['Community #']))
    if int(row['Community #']) > flag:
        y.append(row['crime_rate'])
        flag += 1
y = np.asarray(y, dtype=np.float)
new_y = np.round(y, decimals=3)

plt.figure()
plt.ylim(0, 0.5)
plt.xlim(1, 77)
plt.xlabel('Communities')
plt.ylabel('Rate')
#plt.plot(x,y)
#plt.scatter(x, y, s=y*100, color="red", alpha=0.5)
plt.plot(x, y, "-o")

for i, txt in enumerate(new_y):
    plt.annotate(txt, (x[i],y[i]))

plt.show()
