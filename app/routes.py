from fastapi import APIRouter, HTTPException, Request, status

from app import utilities

route = APIRouter(prefix='/api', tags=['Stage One Task'])

@route.get('/hello', status_code=status.HTTP_200_OK)
def get_user_weather_data(request: Request, visitor_name: str = ''):
    '''Endpoint for getting weather data for a user based on their location'''

    visitor_name = request.query_params.get('visitor_name', None)
    if visitor_name is None:
        raise HTTPException(detail='No visitor_name specified in query parameters', status_code=status.HTTP_400_BAD_REQUEST)
    
    ipinfo = utilities.get_ip_info()
    weather_data = utilities.get_weather_data(lat=ipinfo["loc"].split(",")[0], long=ipinfo["loc"].split(",")[1])

    if not ipinfo or not weather_data:
        raise HTTPException(detail='Unable to get IP info or weather data', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return {
        'client_ip': ipinfo['ip'],
        'location': ipinfo['city'],
        'greeting': f'Hello, {visitor_name}! the temperature is {round(weather_data['main']['temp'])} degrees Celsius in {ipinfo['city']}'
    }
