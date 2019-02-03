'''
ref at https://github.com/aakankshaws/Python/blob/master/weather_data_bs4.py
https://medium.com/@aakankshaws/using-beautifulsoup-requests-to-scrape-weather-data-9c6e9d317800
Using BeautifulSoup, requests to scrape weather data, then save it into a timestamped cvs file
'''

import requests
from bs4 import BeautifulSoup

# SF next 10 day weather
page = requests.get("https://weather.com/weather/tenday/l/USCA0987:1:US")

content = page.content
soup = BeautifulSoup(content, "html.parser")
l = []
all = soup.find("div", {"class": "locations-title ten-day-page-title"}).find("h1").text

table = soup.find_all("table", {"class": "twc-table"})
for items in table:
    for i in range(len(items.find_all("tr")) - 1):
        d = {}
        try:
            d["day"] = items.find_all("span", {"class": "date-time"})[i].text
            d["date"] = items.find_all("span", {"class": "day-detail"})[i].text
            d["desc"] = items.find_all("td", {"class": "description"})[i].text
            d["temp"] = items.find_all("td", {"class": "temp"})[i].text
            d["precip"] = items.find_all("td", {"class": "precip"})[i].text
            d["wind"] = items.find_all("td", {"class": "wind"})[i].text
            d["humidity"] = items.find_all("td", {"class": "humidity"})[i].text
        except:
            d["day"] = "None"
            d["date"] = "None"
            d["desc"] = "None"
            d["temp"] = "None"
            d["precip"] = "None"
            d["wind"] = "None"
            d["humidity"] = "None"
        # print("")
        l.append(d)

import pandas
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

df = pandas.DataFrame(l)
print(df)
# filename = SF_weather20190202-211748.csv
cvs_filename="D:\\github\\walter-repo\\coding\\python\\SF_weather-"+timestr+".csv"
df.to_csv(cvs_filename)

'''      date      day              desc     ...      precip    temp         wind
0    FEB 2  Tonight   Rain/Wind Early     ...        100%   --50°  SSE 28 mph 
1    FEB 3      Sun         Rain/Wind     ...         80%  53°47°  WSW 22 mph 
2    FEB 4      Mon         Rain/Wind     ...         90%  49°43°  WSW 20 mph 
3    FEB 5      Tue     AM Light Rain     ...         70%  49°40°  WNW 11 mph 
4    FEB 6      Wed  AM Clouds/PM Sun     ...          0%  51°42°     N 8 mph 
5    FEB 7      Thu     Mostly Cloudy     ...         10%  52°43°   SSW 6 mph 
6    FEB 8      Fri        PM Showers     ...         40%  51°45°   SSW 9 mph 
7    FEB 9      Sat           Showers     ...         40%  52°44°   SW 13 mph 
8   FEB 10      Sun        AM Showers     ...         40%  52°43°   SW 11 mph 
9   FEB 11      Mon     Partly Cloudy     ...         10%  52°44°  NNE 11 mph 
10  FEB 12      Tue           Showers     ...         40%  54°44°    SE 9 mph 
11  FEB 13      Wed           Showers     ...         50%  54°45°    S 11 mph 
12  FEB 14      Thu           Showers     ...         50%  54°45°  SSW 11 mph 
13  FEB 15      Fri           Showers     ...         40%  54°45°   SW 12 mph 
14  FEB 16      Sat           Showers     ...         60%  54°44°   SW 13 mph 

[15 rows x 7 columns]

Process finished with exit code 0
'''
