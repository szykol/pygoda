# Plik utworzony przez Rafał

import requests
import sys
#Google api geolocation:

class Geolocation:
  # klucze na ten moment pozostają puste
  __google_key = ''
  geolocation_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
  r = requests.post(geolocation_url + __google_key)

  def __init__(self):
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
   
    self.lat = self.r.json()["location"]["lat"]
    self.lng = self.r.json()["location"]["lng"]

  def print(self):
    print("My geolocation is: ", self.lat, self.lng)
    # print(self.lat, self.lng)

  def get_geolocation(self):
      return self.lat, self.lng
      
  def get_city_name(self):
      geocoding_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(self.lat) + ',' + str(self.lng) + '&key=' + str(self.__google_key)
      print(geocoding_url)
      r_geocoding = requests.post(geocoding_url)

      # print(r_geocoding.text)
      #print(r_geocoding.json())
      name_town = r_geocoding.json()["results"][1]["address_components"][1]["long_name"]
      # print(name_town)
      return name_town


geo = Geolocation()
print(geo.get_city_name())

lat, lng = geo.get_geolocation()

print(lat, lng)