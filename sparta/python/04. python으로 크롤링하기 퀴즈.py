import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movie_rank = soup.select('#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img')
movie_title = soup.select('#old_content > table > tbody > tr')
movie_star = soup.select('#old_content > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > div > img')

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

#old_content > table > tbody > tr:nth-child(13) > td.title > div > a

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > div > img
#old_content > table > tbody > tr:nth-child(7) > td:nth-child(3) > div > div > img

for movie in movie_title:
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('img')
    c = movie.select_one('div > div > img')
    if a is not None:
        print(b.text + a.text + c.text)

        # 정말로 이렇게 될줄은 몰라씁니ㅏㄷ. ㅎㅎㅎ