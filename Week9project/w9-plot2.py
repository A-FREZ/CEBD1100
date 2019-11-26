# 2nd Plot: Separate items in 3 classes using Both X & Y axis:
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("data-2.csv")
var1 = df['var1']   # var1 contains observations of X axis
var2 = df['var2']   # var2 contains observations of Y axis
class1x = [] 
class1y = []
class2x = []
class2y = []
class3x = []
class3y = []
for i in range(0, len(var1)):
    if var2[i] < 10:                       # group by Y < 10
        class1x.append(var1[i])
        class1y.append(var2[i])
    elif ((var1[i] < 25) and (var2[i] > 10)): # elseif: X < 25
        class2x.append(var1[i])                #    and Y > 10
        class2y.append(var2[i])
    else:                                      # else: 
        class3x.append(var1[i])
        class3y.append(var2[i])       
plt.scatter(class1x, class1y)
plt.scatter(class2x, class2y)
plt.scatter(class3x, class3y)
plt.show()
  