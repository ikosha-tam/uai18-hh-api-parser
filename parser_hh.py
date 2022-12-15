# import json
import pprint
import requests


DOMAIN = "https://api.hh.ru/"

url_vacancies = f"{DOMAIN}vacancies"
# Название искомой вакансии
name_vacanie = 'junior Python developer'
# Параметры запроса
params = {
    'text': name_vacanie,
    # Страница
    'page': 1
}
# Получаем вакансии
try:
    result = requests.get(url_vacancies, params=params)
    result.raise_for_status()
    vacancies = result.json()
except (requests.RequestException, ValueError):
    print('Ошибка получения данных!!!')
# Сохраняем вакансии в файл json
with open('vacancies.json', 'w') as f:
    f.write(result.text)
# Число найденных вакансий
number_vacancies = vacancies['found']
print(f'Найдено вакансий: {number_vacancies}')

items = vacancies['items']
print(type(items))
first = items[0]
pprint.pprint(first)
print()
print('Вакансия: ', first['name'])
print('url hh: ', first['alternate_url'])
print('url api: ', first['url'])
print('-' * 30)

one_vacancie_url = first['url']
result = requests.get(one_vacancie_url, params=params).json()
pprint.pprint(result)
