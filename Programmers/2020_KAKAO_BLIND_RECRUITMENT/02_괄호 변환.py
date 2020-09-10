SAMPLE = ["(()())()", ")(", "()))((()"]


def split(sample):
    open_count = 0
    close_count = 0
    for word in sample:
        if word == '(':
            open_count += 1
        elif word == ')':
            close_count += 1

        if open_count == close_count:
            cut = open_count + close_count
            u = sample[:cut]
            v = sample[cut:]

            # print(u, v)

            #3. u 가 "올바른 괄호 문자열"인지 검증
            if verify(u):
                #3-1. v에 대해 1단계부터 시행 후 u에 이어 붙임
                # print("올바른 괄호 문자열")
                u = u + solution(v)
                return u

            #4. u 가 "올바른 괄호 문자열이 아닐 때
            else:
                # print("올바르지 않은 괄호 문자열")
                empty = '(' + solution(v) + ')'
                u = u[1:-1]
                new_u = ''
                for word in u:
                    if word == '(':
                        new_u += ')'
                    elif word == ')':
                        new_u += '('

                empty += new_u
                return empty



def verify(u):
    open_count = 0
    close_count = 0

    for word in u:
        if word == '(':
            open_count += 1
        elif word == ')':
            close_count += 1

        if open_count < close_count:
            return False

    return True



def solution(p):
    answer = ''

    #1. 입력이 빈~~
    if len(p) == 0:
        return p

    #2. 문자열을 u, v로 분리
    answer = split(p)

    return answer



for i in range(len(SAMPLE)):
    p = SAMPLE[i]
    print(i+1, " 번 케이스 : ", p)
    print(solution(p))