import sys
import pandas as pd

# Input from file
file = 'musk_data.csv'
df = pd.read_csv(file,index_col=0)
last = df.tail(1)
old_date = tuple(map(int, last.Date.to_string().split()[1].split('-')))
old_day = last['Day'].to_string().split()[1]

# Input through command line
ilen = len(sys.argv)
if ilen==4:
    *rest,idate,iworth,ilabel = sys.argv
elif ilen==3:
    *rest,idate,iworth = sys.argv
    ilabel=''


# Utility Functions
def is_leap(year):
    '''Checking if it is a leap year or not'''
    if (year%4==0 and year%100!=0) or year%400==0 :
        return True
    return False

def month_dater(year):
    '''Returns Sequence of total number of days in months of a year'''
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        months[2]=29
    return months

def next_date(old):
    '''Returns Next date from the input Date'''
    d,m,y = old
    months = month_dater(y)
    if d<months[m]:
        return((d+1,m,y))
    elif m<12:
        return((1,m+1,y))
    else:
        return((1,1,y+1))

def next_day(old):
    '''Returns Next day from the input Day'''
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    i = 0
    for i in range(7):
        if days[i]==old:
            break
    i+=1
    i%=7
    return days[i]

def success():
    print('Done')

def failure():
    print('Attempt Failed')

def worth_fixer(inp, position):
    if inp[-1] in ['+', '-', '*', '/']:
        old = str(df.loc[position].Worth)
        symbol = inp[-1]
        inp = inp[:-1]
        ans = eval(old+symbol+inp)
        return ans
    return inp
    
def update(position):
    worth = worth_fixer(iworth, position)
    date = '-'.join(map(str, c_date))
    df.loc[position]=[date,worth,new_day,ilabel]
    success()
    
# Input Date Correction
for i in ['\\', '/', ':', ',', '.', ';']:
    idate = idate.replace(i,'-')
c_date = tuple(map(int, idate.split('-')))
if c_date[2]<100:
    c_date = (c_date[0], c_date[1], c_date[2]+2000)


# Data Frame Computation
new_date = next_date(old_date)
new_day = next_day(old_day)

if c_date == new_date:
    update(len(df))
else:
    all_dates = [tuple(map(int,i.split('-'))) for i in df.Date]
    if c_date in all_dates:
        position = all_dates.index(c_date)
        if ilabel=='':
            ilabel= str(df.loc[position].Label)
        update(position)
    else:
        failure()

# Update     
df.to_csv(file)

