import datetime as dt

someday =dt.date(2010, 1, 12)

someday.year
someday.month
someday.day

somedaytime = dt.datetime(2010,1,10,21,13,57)

str(someday)
str(somedaytime)

somedaytime.hour
somedaytime.second





print("--------------------------Timetamp-------------------------------")
# it's pandas version of python dateTime
import pandas as pd
import datetime as dt

pd.Timestamp("2015-01-31") # we don't give time so it take midnight the start of date time
# it also work same for 
pd.Timestamp("2015, 11, 1")
pd.Timestamp("2015/01/31")
pd.Timestamp("01-31-2015")
pd.Timestamp("28/01/2015")

# also we can do 
pd.Timestamp("2015-01-31 08:35:15") 
pd.Timestamp("2015-01-31 08:35:15 PM")


# we can aslo use python date or datetime module with pandas
someday =dt.date(2010, 1, 12)
pd.Timestamp(someday)

somedaytime = dt.datetime(2010,1,10,21,13,57)
pd.Timestamp(somedaytime)










print("--------------------------DateTimeIndex Object-------------------------------")

import pandas as pd
import datetime as dt

dates = ["2016/01/02","2016/04/02","2016/01/08","2017/01/02"]
dtIndex = pd.DatetimeIndex(dates)

values = [100, 200, 300, 400]
pd.Series(data = values, index = dtIndex)











print("--------------------------the pd.to_datetime() Method-------------------------------")

import pandas as pd
import datetime as dt

# we can use
pd.to_datetime("2010-04-19")
pd.to_datetime(dt.date(2015,1,1))
pd.to_datetime(dt.datetime(2015,1,1,14,35,20))
pd.to_datetime(["2015-01-03", "2014/02/08","2016", "July 4th, 1996"])

# using serise

time = pd.Series(["2015-01-03", "2014/02/08","2016", "July 4th, 1996"])
time
# now
pd.to_datetime(time)


# if we use wrong date as 31february then we face error and we need error="coerce"
time = pd.Series(["2015-01-03", "2014/02/31","2016", "Hello", "July 4th, 1996"])
time
# now
pd.to_datetime(time, errors = "coerce")


# work with unit time 
pd.to_datetime([1254896357, 5248967512, 4587961254],unit = "s")












print("------------------------- Create Range Of Date With pd.date_range() -------------------------------")

import pandas as pd
import datetime as dt

times = pd.date_range(start='2016', end='2018',freq='D') # frequency = Day
times
times[3]
timess = pd.date_range(start='2016', end='2018',freq='2D') # frequency 0difference 2Day
timess
timess = pd.date_range(start='2019-09-01', end='2019-10-01',freq='B') # frequency = BusinessDay(regular work day)
timess  # count without sat, sun


timesW = pd.date_range(start='2019-09-01', end='2019-10-01',freq='w') # frequency = week
timesW  # count only sun day

timesW = pd.date_range(start='2019-09-01', end='2019-10-01',freq='W-FRI') # frequency = week
timesW  # count only friday as week start day

timesH = pd.date_range(start='2019-09-01', end='2019-10-01',freq='H') # frequency = hour
timesH  # count every single hour

timesH = pd.date_range(start='2019-09-01', end='2019-10-01',freq='12H') # frequency = 12hour
timesH  # count every 12 hour

timesM = pd.date_range(start='2019-02-01', end='2019-12-01',freq='M') # frequency = Month End
timesM  # count lastday ofmonth


timesM = pd.date_range(start='2019-02-01', end='2019-12-01',freq='MS') # frequency = Month Start
timesM  # count lastday ofmonth

timesY = pd.date_range(start='2007-02-01', end='2019-12-01',freq='A') # frequency = Year End
timesY  # count lastday of year



#---------------------------- period define how many date-time can be store
pd.date_range(end = "1999-12-31", periods = 20, freq = "W-SUN") # total 20 sun days are store and finish at 1999-dc-31 last 















print("------------------------- The .dt Accessor -------------------------------")

import pandas as pd
import datetime as dt


dates = pd.date_range(start= "2000-01-01", end = "2010-12-31", freq = "24D")
dates

# create pandas series()
s = pd.Series(dates)
s.head()

s.dt.day.head()
s.dt.month
s.dt.weekday_name

# now see every quarter start  (1/4) in series
mask = s.dt.is_quarter_start
s[mask]

# now see the last day of month in series
mask = s.dt.is_month_end
s[mask]










print("------------------------- Import Financial data set with pandas_datareader Library -------------------------------")

import pandas as pd
import datetime as dt

from pandas_datareader import data

company = "MSFT"  # MicroSoft's stock syble "MSFT"  we need stock symble from net
start = "2017-01-01"
end = "2018-12-31"

d = data.DataReader(name = company, data_source= "yahoo", start = start, end = end)
d.head()

d.values
d.columns
d.index[0]    











print("------------------------- Selecting Row from a DataFrame with a DateTimeIndex -------------------------------")

import pandas as pd
import datetime as dt

from pandas_datareader import data


company = "MSFT"  # MicroSoft's stock syble "MSFT"  we need stock symble from net
start = "2017-01-01"
end = "2018-12-31"

d = data.DataReader(name = company, data_source= "yahoo", start = start, end = end)
d.head()

# we can use loc or iloc
d.loc["2017-03-10"]

d.iloc[300]

d.ix["2017-03-10"]
d.ix[300]


# using date_range

birthday = pd.date_range(start = "1995-09-26", end = "2019-09-18", freq = pd.DateOffset(years = 1))
birthday

# now compare my birthday date have any stock value
stock_bd = d.index.isin(birthday)
d[stock_bd]

d.loc[stock_bd]













print("------------------------- TimeStamp Object Attributes -------------------------------")

import pandas as pd
import datetime as dt

from pandas_datareader import data


company = "MSFT"  # MicroSoft's stock syble "MSFT"  we need stock symble from net
start = "2017-01-01"
end = "2018-12-31"

stock = data.DataReader(name = company, data_source= "yahoo", start = start, end = end)
stock.head()

# create new column with day name   using insert method
stock.insert(0, "Day of Week", stock.index.weekday_name)
stock.head()


# create new column with satrt month   using insert method
stock.insert(1, "Start of Month", stock.index.is_month_start)
stock.head()
stock[stock["Start of Month"]]













print("------------------------- The .truncate() Method -------------------------------")

import pandas as pd
import datetime as dt

from pandas_datareader import data


company = "MSFT"  # MicroSoft's stock syble "MSFT"  we need stock symble from net
start = "2017-01-01"
end = "2018-12-31"

stock = data.DataReader(name = company, data_source= "yahoo", start = start, end = end)
stock.head()

stock.truncate(before = "2017-03-01", after = "2017-05-01")











print("------------------------- pd.DateOffset Objects -------------------------------")  # define specific dateTime


import pandas as pd
import datetime as dt

from pandas_datareader import data


company = "MSFT"  # MicroSoft's stock syble "MSFT"  we need stock symble from net
start = "2017-01-01"
end = "2018-12-31"

stock = data.DataReader(name = company, data_source= "yahoo", start = start, end = end)
stock.head()

# now we add date with date
addD =  stock.index + pd.DateOffset(days = 5) # start 5 days +  stock's date index 1st date

# we can update permanetly by
#stock.index =  stock.index + pd.DateOffset(days = 5) # start 5 days after to stock's date index 1st date


#work with week in date
addW =  stock.index + pd.DateOffset(weeks = 2) # start 2 weeks after to stock's date index 1st date


#work with months in date
addM =  stock.index - pd.DateOffset(months = 3) # start 3 months before to stock's date index 1st date


#work with year in date
addY =  stock.index - pd.DateOffset(years = 1) # start 1 year before to stock's date index 1st date


#work with hours in date
addH =  stock.index - pd.DateOffset(hours = 1) # start 1 hours before to stock's date index 1st date


#work with multiple values in date
addMulti =  stock.index - pd.DateOffset(years = 1, months = 3, days = 5) # start multiple requement before to stock's date index 1st date








print("------------------------- pd.tseries.offsets -------------------------------")

# find month last date 
count_end_M_date = stock.index + pd.tseries.offsets.MonthEnd()


# find month first date 
count_start_M_date = stock.index + pd.tseries.offsets.MonthBegin()

# IMPORT ALL MODULE OF TSERIES.OFFSETS by
from pandas.tseries.offsets import *


# count_start_M_date = stock.index + pd.tseries.offsets.     # found more option
# now we don't need stock.index + pd.tseries.offsets.

# find month first date 
count_start_M_date_ = stock.index + MonthBegin()


# find first abailable quater date End
count_start_Q_date = stock.index + QuarterEnd()
 











print("------------------------- The Timedalta Object -------------------------------")   # work with difference of dateTime

import pandas as pd
import datetime as dt


timeA = pd.Timestamp("2016-03-31")
timeB = pd.Timestamp("2016-04-30")

print(timeA - timeB)



timeA = pd.Timestamp("2016-03-31 04:35:16 PM")
timeB = pd.Timestamp("2016-04-30 02:16:49 AM")

print(timeA - timeB)

print(type(timeA - timeB))    #  <class 'pandas._libs.tslibs.timedeltas.Timedelta'>
# not same type
print(type(timeB))    #  <class 'pandas._libs.tslibs.timestamps.Timestamp'>    





pd.Timedelta(days = 3 , minutes = 45, hours = 12, weeks = 8)   # today to after -> Timedelta('59 days 12:45:00')





shipping = pd.read_csv("ecommerce.csv", index_col = "ID", parse_dates = ["order_date", "delivery_date"])   # change formate / to -
shipping.head()


# see difference between every index date
shipping["delivery_date"] - shipping["order_date"]   


# added to our previous dataSet
shipping["Delivery Time"] = shipping["delivery_date"] - shipping["order_date"]   
shipping.head()


# now find double Date of Delevery date 
shipping["delivery_date"] + shipping["Delivery Time"]

# add as new column to data set
shipping["Twice As Long"] = shipping["delivery_date"] + shipping["Delivery Time"]
shipping.head()


# see all dataType on dataSet
shipping.dtypes



# find which index take more than 1 year to delivery 
shipping["Delivery Time"] > "365 days"

shipping[shipping["Delivery Time"] > "365 days"]



# now found the minimum delivery time 
shipping["Delivery Time"].min()


















