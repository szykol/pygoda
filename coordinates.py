# Plik utworzony przez Rafał

import requests
import sys
#Google api geolocation:

class Geolocation:
  # klucze na tą chwilę pozostają puste
  __google_key = ''
  
  def __init__(self):
    if self.__google_key:
      geolocation_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
      self.r = requests.post(geolocation_url + self.__google_key)

      self.lat = self.r.json()["location"]["lat"]
      self.lng = self.r.json()["location"]["lng"]

      status = self.r.status_code
      if status == 200:
        print("OK geolocation")
      else:
        if status == 403:
          print("Przekroczyłeś limit dzienny zapytań do API Google!")
          sys.exit(0)
        if status == 400:
          print("Twój klucz API Geolocation Google jest nieprawidłowy!")
          sys.exit(0)
        if status == 404:
          print("Error 404! NOT FOUND!")
          sys.exit(0)

  def print(self):
    print("My geolocation is: ", self.lat, self.lng)
    # print(self.lat, self.lng)

  def get_geolocation(self):
      return self.lat, self.lng
      
  def get_city_name(self, lat=None, lng=None):
    if lat is None:
      lat = self.lat
    else:
      lat = str(lat).replace(',', '.')
    if lng is None:
      lng = self.lng
    else:
      lng = str(lng).replace(',', '.')

    geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(lat) + ',' + str(lng) + '&key=' + str(self.__google_key)
    #print(geocoding_url)
    r_geocoding = requests.post(geocoding_url)
    
    succes = False
    try:
      name_town = r_geocoding.json()["results"][2]["address_components"][3]["long_name"]
      succes = True
    except IndexError:
      name_town = f'{lat} {lng}'.replace(',', '.')
    return {"status": succes, "data":name_town}
  @staticmethod
  def api_key_specified():
    return bool(Geolocation.__google_key)
