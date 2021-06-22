from pyowm import OWM

owm = OWM('key')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')
w = observation.weather
print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = mgr.weather_around_coords(-22.57, -43.12)