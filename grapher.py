from collections import OrderedDict
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('ggplot')
file = 'musk_data_tester.csv'
file = 'musk_data.csv'
df = pd.read_csv(file, index_col=0)

## Daily Plot ##
x = np.array(df.Date)
y = np.array(df.Worth, dtype=float)
indexes = range(len(df))

p1 = plt.bar(indexes ,y)
p2 = plt.bar(indexes, 24-y, bottom=y)
p3 = plt.axhline(y=15, color='r', linestyle='--')

#display
plt.title('Hours usage per Day')
plt.ylabel('Worthy Hours')
plt.xticks(indexes, x, rotation='vertical')
plt.legend((p1[0], p2[0], p3),('Worthy', 'Waste', 'Musk_Line'))
plt.ylim(0,24)
plt.subplots_adjust(bottom=0.25)
plt.show()

## Monthly plot ##
dates = [ i.split('-') for i in x]
months = OrderedDict()
j=0
for i,j in zip(dates,y):
    tag = i[1]+'/'+i[2]
    if tag in months:
        months[tag].append(j)
    else:
        months[tag]=[j]
        

monthly_count = [sum(m) for m in months.values()]
monthly_std = [np.std(m) for m in months.values()]
indexes = range(len(monthly_count))
p1 = plt.bar(indexes,monthly_count, yerr=monthly_std)
p2 = plt.axhline(y=456.25, color='r', linestyle='--')

#display
plt.title('Monthly Worthy Hours')
plt.xticks(indexes, months.keys(), rotation='vertical')
plt.legend((p1[0],p2),('Worthy','Musk_Line'))
plt.ylabel('Hours')
plt.ylim(0,730)
plt.subplots_adjust(bottom=0.25)
plt.show() 


for i in df:
    print(i)
