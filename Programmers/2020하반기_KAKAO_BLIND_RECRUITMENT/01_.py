SAMPLE = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]


def solution(new_id):
    answer = ''
    replace_id = ''
    count = 0
    #1. 대문자를 소문자로 (A : 65, Z: 90 // a : 97, z : 122)
    for idx in range(len(new_id)):
        text = new_id[idx]

        # 1. 대문자를 소문자로 (A : 65, Z: 90 // a : 97, z : 122)
        if 65 <= ord(text) <= 90:
            if count:
                count = 0
                replace_id += '.'
            replace_id += chr(ord(text) + 32)

        #2. 소문자, 숫자, 빼기, 밑줄, 마침표는 그대로
        elif 97 <= ord(text) <= 122 or 48 <= ord(text) <= 57 or text in ['-', '_', '.']:
            # 3 : 마침표 2번 이상이면 한 개만
            if text == '.':
                count += 1
            elif count == 0:
                replace_id += text
            else:
                replace_id += '.' + text
                count = 0

    new_id = replace_id

    #4 : 앞 뒤의 마침표 삭제
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    #5 : 빈 문자열이면 'a'를 대입
    if len(new_id) == 0:
        new_id = 'a'

    #6 : 16자 이상이면 15개의 문자를 제외한 나머지 문자 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        #6-1: 마지막이 마침표이면 제거
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        add_num = 3 - len(new_id)
        new_id = new_id + new_id[-1] * add_num
    answer = new_id

    return answer

for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    new_id = SAMPLE[i]
    print(solution(new_id))