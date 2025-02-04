import requests

API_KEY = ''


def get_city_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    return content


def write_to_file(data):
    for day in data['list']:
        with open('weather_data.txt', 'a') as f:
            f.write(f"Dublin,{day['dt_txt']},{str(day['main']['temp'])},{day['weather'][0]['description']}\n")

def main():
    data = get_city_weather_data('Dublin')
    write_to_file(data)


if __name__ == '__main__':
    main()
