SAMPLE = [
    [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
    [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
    [6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]
]

def display(arr):
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end='\t')
        print()
    print()

#
# def find_root(maps, a, b, cur, visited, flag_a, flag_b):
#     visited[cur] = 1
#
#     if cur == a:
#         print("a 도착")
#         flag_a = True
#     elif cur == b:
#         print("b 도착")
#         flag_b = True
#
#     if flag_a and flag_b:
#         print("End")
#         return
#
#     next_root = []
#     for mdx in range(len(maps[cur])):
#         if maps[cur][mdx] and not visited[mdx]:
#             next_root.append(mdx)
#     print(next_root)
#
#     for nrt in next_root:
#         find_root(maps, a, b, nrt, visited, flag_a, flag_b)

import copy
def find_root(maps, start, end, cur, visited, cost, root):
    global min_value
    global temp_roots
    if cur == end:
        if min_value > cost:
            # print('도착')
            # print(root)
            min_value = cost
            temp_roots = copy.deepcopy(root)
    else:
        next_root = []
        for mdx in range(len(maps[cur])):
            if maps[cur][mdx] and not visited[mdx]:
                next_root.append(mdx)

        for nrt in next_root:
            visited[nrt] = 1
            cost += maps[cur][nrt]
            root.append(nrt)
            if min_value > cost:
                find_root(maps, start, end, nrt, visited, cost, root)
            root.pop()
            cost -= maps[cur][nrt]
            visited[nrt] = 0


import sys
def solution(n, s, a, b, fares):
    global min_value
    global temp_roots
    answer = 0
    roots = []
    maps = [[0]*(n+1) for _ in range(n+1)]

    for start, end, cost in fares:
        maps[start][end] = cost
        maps[end][start] = cost


    # 시작부터 A까지
    visited = [0] * (n+1)
    visited[s] = 1
    min_value = sys.maxsize
    find_root(maps, s, a, s, visited, 0, [s])
    min_A = min_value
    a_root = temp_roots

    # 시작부터 B까지
    visited = [0] * (n+1)
    visited[s] = 1
    min_value = sys.maxsize
    find_root(maps, s, b, s, visited, 0, [s])
    min_B = min_value
    b_root = temp_roots

    standard = min_A + min_B

    short = len(a_root) if len(a_root) < len(b_root) else len(b_root)

    for rrr in range(1, short):
        if a_root[rrr] == b_root[rrr]:
            standard -= maps[a_root[rrr-1]][a_root[rrr]]
        else:
            break


    total = standard

    for num in range(1, n+1):
        if num in (s, a, b):
            continue
        else:
            visited = [0] * (n + 1)
            visited[s] = 1
            min_value = standard
            find_root(maps, s, num, s, visited, 0, [s])
            front_price = min_value

            visited = [0] * (n + 1)
            visited[num] = 1
            min_value = standard
            find_root(maps, num, a, num, visited, 0, [num])
            a_price = min_value

            visited = [0] * (n + 1)
            visited[num] = 1
            min_value = standard
            find_root(maps, num, b, num, visited, 0, [num])
            b_price = min_value

            temp_total = front_price + a_price + b_price
            if total > temp_total:
                total = temp_total

    answer = total if total < standard else standard

    return answer



for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    n, s, a, b, fares = SAMPLE[i]
    print(n, s, a, b, fares)
    print(solution(n, s, a, b, fares))