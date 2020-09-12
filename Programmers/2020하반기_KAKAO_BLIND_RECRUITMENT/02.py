SAMPLE = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]],
    [["XYZ", "XWY", "WXA"], [2,3,4]]
]

import copy
def create_comb(order, count, cur, menu):
    global combi
    if len(menu) == count:
        combi.append(copy.deepcopy(menu))
    else:
        for idx in range(cur, len(order)):
            menu.append(order[idx])
            create_comb(order, count, idx+1, menu)
            menu.pop()


def solution(orders, course):
    global combi
    answer = []


    for count in course:
        check = {}

        for order in orders:
            if len(orders) < count:
                continue

            temp = []
            for word in order:
                temp.append(word)
            temp.sort()

            combi = []
            create_comb(temp, count, 0, [])

            for cc in range(len(combi)):
                com = tuple(combi[cc])

                if check.get(com) == None:
                    check[com] = 1
                else:
                    check[com] += 1
        tmp_answer = []
        tmp_max = 0
        for key, value in check.items():
            if value < 2:
                continue

            if value > tmp_max:
                tmp_answer = [''.join(key)]
                tmp_max = value
            elif value == tmp_max:
                tmp_answer += [''.join(key)]

        answer += tmp_answer

    answer.sort()

    return answer


for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    orders, course = SAMPLE[i]
    print(orders, course)
    print(solution(orders, course))