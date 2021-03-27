from rest_framework.views import APIView
from rest_framework.response import Response
import requests


def OpenWeather(cityname):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=ddff737555fe75aaf6f86bc5077a1913')
    api_data = response.json()
    return api_data

def TempConvertor(kelvin):
    celcius = kelvin - 273.15
    return str(round(celcius,2))

class WeatherApiView(APIView):
    def post(self,request):
        data = request.data
        city_name = data['city']
        api_data = OpenWeather(city_name)
        return Response({
    'success':True,
    'result': {
        'condition' : api_data['weather'][0]['main'],
        'condition_description':api_data['weather'][0]['description'],
        'currentTemp' : TempConvertor(api_data['main']['temp']),
        'minTemp' : TempConvertor(api_data['main']['temp_min']),
        'maxTemp' : TempConvertor(api_data['main']['temp_max'])
    },
    'resetList' : [],
    'errorMessageKey' : 'Error_Response'
})
