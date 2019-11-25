# 1st Plot: Separate observations in 3 classes using X axis
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("data-1.csv")
var1 = df['var1']    # var1 contains observations of X axis
var2 = df['var2']
class1x = [] 
class1y = []
class2x = []
class2y = []
class3x = []
class3y = []
for i in range(0, len(var1)):
    if var1[i] < -8:                           # group by X < -8
        class1x.append(var1[i])
        class1y.append(var2[i])
    elif ((var1[i] > -8) and (var1[i] < -4)):  # elseif: -8 < X < -4
        class2x.append(var1[i])
        class2y.append(var2[i])
    else:                                      # else: -4 < X
        class3x.append(var1[i])
        class3y.append(var2[i])       
plt.scatter(class1x, class1y)
plt.scatter(class2x, class2y)
plt.scatter(class3x, class3y)
plt.show()
  