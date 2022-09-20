from urllib.request import urlopen as open
import datetime as dt
import win32api

url='http://just-the-time.appspot.com/'
data=open(url).read().strip().decode()
utcTime=dt.datetime.strptime(data,'%Y-%m-%d %H:%M:%S')
win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
