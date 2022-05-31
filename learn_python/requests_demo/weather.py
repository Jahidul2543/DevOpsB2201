import requests

url = "https://www.google.com"

open_weatehr_url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={New York}&appid={87af3508c443016e851bee3ba091fd3c}'


def get_people_info():
    response = requests.get(open_weatehr_url)
    print(response.text)
    print(type(response))


if __name__ == "__main__":
    get_people_info()