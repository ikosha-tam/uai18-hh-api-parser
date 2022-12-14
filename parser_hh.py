import pprint
import requests


DOMAIN = "https://api.hh.ru/"
result = requests.get(DOMAIN)
print(result.status_code)
url_vacancies = f"{DOMAIN}vacancies"
params = {
    'text': 'junior Python developer',
    'page': 1
}
result = requests.get(url_vacancies, params=params)
print(result.status_code)
pprint.pprint(result.json())
