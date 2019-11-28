# 2nd Plot: Separate items in 3 classes using Both X & Y axis:
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("data-3.csv")
x = df['var1']
y = df['var2']
class1x = []
class1y = []
class2x = []
class2y = []
class3x = []
class3y = []
for i in range(0, len(df)):
    if x[i] < 118:
        class1x.append(x[i])
        class1y.append(y[i])
    elif (x[i] > 118 and x[i] < 163):
        class2x.append(x[i])
        class2y.append(y[i])
    else:
        class3x.append(x[i])
        class3y.append(y[i])
        
plt.scatter(class1x, class1y, c = 'red')
plt.scatter(class2x, class2y, c = 'blue')
plt.scatter(class3x, class3y, c = 'green')
plt.show()
plt.close()  