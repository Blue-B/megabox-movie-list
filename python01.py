import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A9%94%EA%B0%80%EB%B0%95%EC%8A%A4+%EC%B2%9C%EC%95%88+%EC%83%81%EC%98%81%EC%8B%9C%EA%B0%84%ED%91%9C'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movie_section = soup.find_all("th", attrs={"scope":"row"})

for movie_list in movie_section: 
    print(movie_list.a.get_text())