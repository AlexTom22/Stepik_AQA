import requests
import urllib.request
import logging


def test_requests():
    city_name = "Minsk"
    api_key = "d87819d6535e372021cb731329f70bd5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    logging.info(f"{response.status_code} => {response.ok}")
    assert response.status_code == 200



def test_url_lib():
    pass
