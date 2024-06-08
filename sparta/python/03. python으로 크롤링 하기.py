# 크롤링을 하기 위해서 두 가지를 꼭해야한다.
# 1. 특정 API에서 requests 패키지를 이용하여 - 특정 사이트의 HTML을 가져오는 것!! : 이건 앞에서 연습했지 ㅇㅇ
# 2. 가져온 HTML에서 원하는 특정 정보를 찾아내야하는데 이 것은 beautifulSoup4 라는 패키지를 통해서 할 수 있다.

import requests # requests 쓸거임 ㅋ
from bs4 import BeautifulSoup # beautifulsoup도 쓸거임 ㅋㅋ

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# headers는 우리가 마치 브라우저에서 콜을 날리는 것처럼 이용하기 위해서 쓰는거라고 한다.

data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# tilte = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

movies = soup.select('#old_content > table > tbody > tr')

print(movies)


for i in movies:
    rank = i.select_one('td > img')
    title = i.select_one('td.title > div > a')
    star = i.select_one('td.point')

    if title is not None:
        print(rank['alt'] + title.text + star.text)
        


# 제목's selector 
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a

# 순위
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

# 평점's selector
#old_content > table > tbody > tr:nth-child(2) > td.point





























for i in movies:
    title = i.select_one('td.title > div > a')
    rank = i.select_one('td > img')
    star = i.select_one('td.point')

    if title is not None:
        print(f'''{rank['alt']} {title.text} {star.text}''')
