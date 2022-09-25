import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://www.eldorado.ru/cat/detail/igrovaya-pristavka-sony-playstation-5/"
user_agent = UserAgent()

headers = {"Accept": "*/*", "User-Agent": user_agent.random}

response = requests.get(url, headers=headers)
print(response.text)
