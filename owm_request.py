import requests


#translate degrees to directions
def get_wind_direction(deg):
    l = ['N ','NE',' E','SE','S ','SW',' W','NW']
    for i in range(0,8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

# get city_id with given name
def get_city_id(s_city_name, appid):
    try:
        res = requests.get(
            "http://api.openweathermap.org/data/2.5/find",
                     params={
                         'q': s_city_name,
                         'type': 'like',
                         'units': 'metric',
                         'lang': 'ru',
                         'APPID': appid
                         }
                     )
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
        assert isinstance(city_id, int)
        return city_id
    except Exception as e:
        print("Exception (find):", e)
        pass


# Forecast output
def request_forecast(city_id, appid):
    try:
        res = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast",
                           params={
                               'id': city_id,
                               'units': 'metric',
                               'lang': 'ru',
                               'APPID': appid
                               }
                           )
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        for i in data['list']:
            print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                   '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                   get_wind_direction(i['wind']['deg']),
                   str(i['main']['humidity'])+ " %",
                   i['weather'][0]['description']
                    )
    except Exception as e:
        print("Exception (forecast):", e)
        pass


# Forecast json
def request_forecast_json(city_id, appid):
    try:
        res = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast",
                           params={
                               'id': city_id,
                               'units': 'metric',
                               'lang': 'ru',
                               'APPID': appid
                               }
                           )
        data = res.json()
    except Exception as e:
        print("Exception (forecast):", e)
        pass
    return data
