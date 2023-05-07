from fastapi import FastAPI
import requests


app = FastAPI()


@app.post('/')
async def weather_forecast(city: str):
    try:
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=24cbe48a48d8bf0610dcd03339c6919a'
        response = requests.get(URL)
        response.raise_for_status()  # Raise an exception if the HTTP status code is not successful (e.g., 404, 500, etc.)
        data = response.json()
        temp = data['main']['temp']
        if temp < 283:
            return {'outfit': 'Thermal underwear, long-sleeve t-shirts, leggings, Fleece jackets, down vests, wool sweaters',
                    'image_url': 'https://media.istockphoto.com/id/1085234602/photo/knitted-sweater-isolated-on-white-background.jpg?s=1024x1024&w=is&k=20&c=uUITjkitqEQQaqFIxr0r2HsJAORmrWuzSRlmuwmxqyQ='}
        else:
            return {'outfit': 'Cotton t-shirts, linen shirts, rayon dresses, Flowy skirts, sundresses, relaxed-fit shorts',
                    'image_url': 'https://media.istockphoto.com/id/607505108/photo/hanging-t-shirts.jpg?s=1024x1024&w=is&k=20&c=aA1y9trLMikUJRotEs8pBh6_M1cDS5fzZLKRSaQIU0g='}
    except requests.exceptions.HTTPError as e:
        return {'error': f'HTTP Error: {e}'}
    except (KeyError, ValueError) as e:
        return {'error': f'JSON parsing error: {e}'}
