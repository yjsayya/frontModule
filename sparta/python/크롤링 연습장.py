people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person['age'] > 20:
            print(person['name'])
    except:
        print(person['name'], "에러입니다.")

# 이건 너무 많이 쓰면 어디서 에러가 나오는지 참을 수가 없기 때문에 자주 사용하는 것은 추천하지 않는다 