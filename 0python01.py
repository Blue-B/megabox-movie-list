import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A9%94%EA%B0%80%EB%B0%95%EC%8A%A4+%EC%B2%9C%EC%95%88+%EC%83%81%EC%98%81%EC%8B%9C%EA%B0%84%ED%91%9C'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movie_section = soup.find_all("th", attrs={"scope":"row"})
timeinfo = soup.find_all("td", attrs={"class":"time"} ) #상영시간표들 timeinfo변수에넣음
for idx,sections in enumerate(movie_section,start=0):
    print(sections.a.get_text()) #영화제목
    print('>'+sections.find("span").get_text()) #영화등급
    print(timeinfo[idx].get_text()) #상영시간표
    print(' ')#공백