import requests
from bs4 import BeautifulSoup
import datetime #오늘의 날짜를 구하기위해 모듈을 가져옴
import telegram


bot=telegram.Bot(token ='5018080837:AAE1EautykTPYAagjCJAUXbtQodzTkjNNoI')
chat_id = '5096740218'


url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A9%94%EA%B0%80%EB%B0%95%EC%8A%A4+%EC%B2%9C%EC%95%88+%EC%83%81%EC%98%81%EC%8B%9C%EA%B0%84%ED%91%9C'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
movie_section = soup.find_all("th", attrs={"scope":"row"})
timeinfo = soup.find_all("td", attrs={"class":"time"} ) 

today = str(datetime.date.today()) #오늘의 날자를 년월일 으로 나타냄
bot.send_message(chat_id=chat_id, text=today+' 메가박스 상영시간표')
for idx,sections in enumerate(movie_section,start=0):
    bot.sendMessage(chat_id=chat_id, text=sections.a.get_text()) 
    bot.sendMessage(chat_id=chat_id, text='>'+sections.find("span").get_text()) 
    bot.sendMessage(chat_id=chat_id, text=timeinfo[idx].get_text())
    bot.sendMessage(chat_id=chat_id, text='ㅤ') #' '공백입력시 오류가 남으로 공백 문자를 사용함