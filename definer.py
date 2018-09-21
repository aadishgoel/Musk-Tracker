import pandas as pd

df = pd.DataFrame([['30-12-17',4,'Sat',''],['31-12-17',4,'Sun','']], columns=['Date', 'Worth', 'Day', 'Label'])

## WARNING: IT WILL MAKE NEW FILE DELETING ORIGINAL
#df.to_csv('musk_data.csv')
##

df.to_csv('musk_data_tester.csv')
