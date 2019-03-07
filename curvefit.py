import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


data = []
time = []


filename = 'testinlab11plasticwNABTandPLUG.txt'
with open(filename,'r') as f:
    for line in f:
        if(line[0] is not '='):
            line_split = line.replace("\n", "").replace(" ","").split(',')
            if (len(line_split) != 4):
                continue
            if ((float(line_split[3]) > 0.5) and (float(line_split[3]) < 2)):
                time.append(float(line_split[1]))
                data.append(float(line_split[3]))
            if (float(line_split[3]) > 2):
                break

data = np.array(data)
time = np.array(time)

def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, time, data)

[a, b] = params[0]
print ("a is,", a)
print ("b is,", b)

label = str(round(a,4))+"*x"+str(round(b,4))

plt.plot(time, a*time+b, "ro", markersize=1, label=label)
plt.legend(loc='lower right')
plt.show()
