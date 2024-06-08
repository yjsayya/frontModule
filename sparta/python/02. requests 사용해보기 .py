# 1. requests 라이브러리 설치하는 것 파이참에서 어떻게 하는지 한번 복습해보고
# 2. HTML에서 따릉이로 연습했던 것으로 파이참 문법 한번 더 복습하면 된다.
# 3. requests 어떻게 불러와서 사용하는지는 notion에 기록해두었다.
# 파이썬으로 HTTP 요청을 쓰기 위한 라이브러리 ㅇㅋ

import requests # requests 라이브러리 설치 필요

r = requests.get('https://www.naver.com')

# rjson = r.json()
print(r.text)
print(r.status_code)

# print(rjson)


# rows = rjson['RealtimeCityAir']['row']

# for i in rows:
#     gu_name = i['MSRSTE_NM']
#     gu_mise = i['IDEX_MVL']

#     if gu_mise > 40:
#         print("=========================")
#         print("미세먼지 ㅈㄴ 안 좋은 동네 ~")
#         print(f"이름 : {gu_name}")  
#         print(f"미세먼지 수치 : {gu_mise}")  
#         print("=========================")
#         print(" ")
