#Search for a new API or use the climate or geocode API
#request its info and parse it using json
#send it to the data base counting how many times the location was retrieved and updating with the last date of retrieval
#Try to use twitter API
import requests
import json
import sqlite3
from datetime import datetime
import string

conn = sqlite3.connect("OWNdatabase.sqlite3")
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS Cities")
cur.execute('''CREATE TABLE IF NOT EXISTS
            Cities (Name TEXT, Country TEXT, ID INTEGER, Retrieved INTEGER, Long FLOAT, Lat FLOAT, Dateandtime TEXT,
            TempMax FLOAT, TempMin FLOAT, FeelsLike FLOAT, Humidity FLOAT)''')


print("Thats the program to compare the weather from cities of your interest. Hit enter to finish. ")
while True:
    APIKey = str(input("Enter your API Key: "))
    Citiesstr = input("Enter the cities you want to check separated by comma: \n")
    if len(APIKey) < 1 or len(Citiesstr) < 1 or not isinstance(Citiesstr, str):
        print('You finished the program')
        break
    Cities = Citiesstr.strip().split(",")
    date = datetime.now()
    now = date.strftime('%d/%m/%Y %H:%M:%S')
    for city in Cities:
        city = city.strip().upper()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(city,APIKey)
        r = requests.get(url)
        js = json.loads(r.text)
        attrlist = (js["name"], js["sys"]["country"], js["id"], 1, js['coord']['lon'], js['coord']['lat'], now, js['main']['temp_max'], js['main']['temp_min'], js['main']['feels_like'], js['main']['humidity'])
        # cur.executemany("INSERT INTO Cities Values (?,?,?,?,?,?,?,?,?,?,?)", (attrlist,))
        x = js['name']
        cur.execute('''SELECT * FROM Cities WHERE Name = ? LIMIT 1''', (x,))
        try:
            count = cur.fetchone()[3]
            cur.execute('''UPDATE Cities SET Retrieved = ?, Dateandtime = ?, TempMax= ?, TempMin = ?, FeelsLike = ?, Humidity = ? WHERE Name = ?''', (count + 1, now, js['main']['temp_max'], js['main']['temp_min'], js['main']['feels_like'], js['main']['humidity'], x))
        except:
            cur.executemany("INSERT INTO Cities Values (?,?,?,?,?,?,?,?,?,?,?)", (attrlist,))
        conn.commit()

cur.close()



#Name TEXT, Country TEXT, ID INTEGER, Retrieved INTEGER, Long FLOAT, Lat FLOAT, TempMax FLOAT, TempMin FLOAT, FeelsLike FLOAT, Humidiy FLOAT
