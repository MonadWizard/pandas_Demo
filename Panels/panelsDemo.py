import pandas as pd
from pandas_datareader import data        # datareader import data to load

companies = ["MSFT", "GOOG", "AAPL", "AMZN", "TSLA"]
source = "yahoo" 
access="sk_"
begning = "2014-01-01"
last = "2017-12-31"

p = data.DataReader(name = companies, data_source= source,start = begning , end = last)

p











































































