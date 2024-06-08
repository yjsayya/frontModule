import pymysql
import requests # requests 쓸거임 ㅋ
from bs4 import BeautifulSoup # beautifulsoup도 쓸거임 ㅋㅋ

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://bnzn2426.tistory.com/115',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
conn = pymysql.connect (host='127.0.0.1', user= 'root', password= 'wndehd', db = 'pythonDB', charset='utf8')

# DB에 넣기
def insert_data(conn):
    cur = conn.cursor()
    sql = f'''INSERT INTO movies (RANK, title, star) VALUES ('{Rank}', '{title}', '{star}') '''
    cur.execute(sql)
    conn.commit()

array1 = soup.select('#mArticle > div > div.area_view > div.contents_style > h3')

for i in array1:
    print(i.select_one('b').text)
    print(" ")

#mArticle > div > div.area_view > div.contents_style > h3:nth-child(49) > b
#mArticle > div > div.area_view > div.contents_style > h3:nth-child(56) > b