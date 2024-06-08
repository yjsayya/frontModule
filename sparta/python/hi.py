def solution(polynomial):
    li = list(polynomial.split(' + '))
    x = 0
    const = 0

    for i in li:
        if 'x' in i and i != 'x':
            x += int(i[0])
        elif i == 'x':
            x += 1
        else:
            const += int(i)

    if const != 0 and x != 0:
        answer = str(x) + 'x' + ' + ' + str(const)
    elif const == 0 and x != 0:
        answer = str(x) + 'x'
    elif const != 0 and x == 0:
        answer = str(const)
    else:
        answer = '0'

    return answer


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
