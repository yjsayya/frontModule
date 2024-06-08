import requests # requests 쓸거임 ㅋ
from bs4 import BeautifulSoup # beautifulsoup도 쓸거임 ㅋㅋ
import pymysql


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# headers는 우리가 마치 브라우저에서 콜을 날리는 것처럼 이용하기 위해서 쓰는거라고 한다.

data = requests.get('https://www.naver.com',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select('#NM_THEME_CATE_LIST > li')

for i in title:
    a = i.select_one('a')
    print(a['data-clk'])




# for i in title:
#     a = i.select_one('a')
#     print(a)


# '#old_content > table > tbody > tr:nth-child(2) > td.title > div > a'
# #NM_THEME_CATE_LIST > li:nth-child(1) > a


