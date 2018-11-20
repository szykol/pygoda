import requests

class WeatherApi:
    # klucze na ten moment pozostają puste
    __api_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather?'

    def city_weather(self, city):
        url = f'{self.url}q={city}&appid={self.__api_key}&units=metric&lang=pl'

        return self.validate_request(url)

    def coord_weather(self, lon, lat):
        url = f'{self.url}lat={lat}&lon={lon}&appid={self.__api_key}&units=metric&lang=pl'.replace(',','.')

        return self.validate_request(url)

    def validate_request(self, url):
        r = requests.get(url)

        if(r.status_code != 200):
            print('An error has ocurred')
            return {"status": "wrong"}
        else:
            #print(r.json())
            main_weather = r.json()['weather'][0]['description']
            temp = f"{r.json()['main']['temp']} °C"
            icon = r.json()['weather'][0]['icon']
            return {
                "status": "ok",
                "main": main_weather,
                "temp": temp,
                "icon": icon
            }