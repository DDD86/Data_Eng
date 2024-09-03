import requests

def get_weather(city):
    api_key = 'b9b6956905ca8e6fe5d8a2fdb23286b8'  
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'  
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f'Погода в {city}: {weather}, температура: {temperature}°C')
    except requests.exceptions.HTTPError as http_err:
        print(f'Ошибка HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Ошибка запроса: {err}')
    except KeyError:
        print('Ошибка обработки данных. Проверьте правильность названия города.')
    except Exception as err:
        print(f'Произошла ошибка: {err}')

def main():   
    city = input('Введите название города: ').strip()
    if city:
        get_weather(city)
    else:
        print('Название города не может быть пустым.')


if __name__ == '__main__':
    main()
