import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# *** THIS CODE CONTAINS THE curvefit.py CODE AS WELL ***

data = []
time = []

dataCF = []
timeCF = []

filename = 'testinlab35rigidNABTandPLUG.txt'
with open(filename,'r') as f:
    # creating data for overall plot
    for line in f:
        if(line[0] is not '='):
            line_split = line.replace("\n", "").replace(" ","").split(',')
            if (len(line_split) != 4):
                continue
            time.append(float(line_split[1]))
            data.append(float(line_split[3]))
    # creating data for curve fit
with open(filename,'r') as f:
    for line in f:
        if(line[0] is not '='):
            line_split = line.replace("\n", "").replace(" ","").split(',')
            if (len(line_split) != 4):
                continue

            # # ***** SLOW *****


            if ((float(line_split[3]) > 0.7) and (float(line_split[3]) < 2.5)):
                timeCF.append(float(line_split[1]))
                dataCF.append(float(line_split[3]))
            if (float(line_split[3]) > 2.5):
                break


            # # ***** for last pulse *****
            # if ((float(line_split[1]) > 1768) and (float(line_split[1]) < 1769)):
            #     if ((float(line_split[3]) > 0.55) and (float(line_split[3]) < max(data))):
            #         timeCF.append(float(line_split[1]))
            #         dataCF.append(float(line_split[3]))
            #     if (float(line_split[1]) > time[data.index(max(data))]):
            #         break


            # #***** FAST *****
            #
            # if ((float(line_split[3]) > 0.6) and (float(line_split[3]) < max(data))):
            #     timeCF.append(float(line_split[1]))
            #     dataCF.append(float(line_split[3]))
            # if (float(line_split[1]) > time[data.index(max(data))]):
            #     break

data = np.array(data)
time = np.array(time)
plt.plot(time, data, "go", markersize=1)
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (volts)")
plt.title("Compliant Run (plastic syringe, NABT)")


dataCF = np.array(dataCF)
timeCF = np.array(timeCF)

def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, timeCF, dataCF)

[a, b] = params[0]
print ("a is,", a)
print ("b is,", b)

label = str(round(a,4))+"*x"+str(round(b,4))

plt.plot(timeCF, a*timeCF+b, "ro", markersize=1, label=label)
plt.legend(loc='lower right')

plt.show()
