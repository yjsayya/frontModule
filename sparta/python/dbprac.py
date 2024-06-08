import pymysql
import requests # requests 쓸거임 ㅋ
from bs4 import BeautifulSoup # beautifulsoup도 쓸거임 ㅋㅋ

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
conn = pymysql.connect (host='127.0.0.1', user= 'root', password= 'wndehd', db = 'pythonDB', charset='utf8')

# ------------------------------------------------------------------------------------------------
def dbconnect():
    conn = pymysql.connect (host='127.0.0.1', user= 'root', password= 'wndehd', db = 'pythonDB', charset='utf8') 
    return conn


def main():
    conn = dbconnect()
    print("연결완료")
    conn.close()
    print('연결해제')


def search_data(conn):
    cur = conn.cursor()
    sql = 'SELECT * FROM 테이블이름'
    cur.execute(sql)
    results = cur.fetchall()
    print(results)


# 데이터 삽입하기 insert
def insert_data(conn, Rank, title, star):
    cur = conn.cursor()
    sql = f''' INSERT INTO movies (RANK, title, star) VALUES ('{Rank}', '{title}', '{star}') '''
    cur.execute(sql)
    conn.commit()
    # sql문 실행 메서드 + 커밋 메서드 



movies = soup.select('#old_content > table > tbody > tr')
# 뽑아내고 바로 DB에 넣어보자
for i in movies:
    Ranking = i.select_one('td > img')
    title = i.select_one('td.title > div > a')
    star = i.select_one('td.point')

    if title is not None:
        print(f'''{Ranking['alt']} {title.text} {star.text}''')
        insert_data(conn, Ranking['alt'], title.text, star.text)
        print(" ")

    