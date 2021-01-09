import sys
sys.stdin = open('input.txt', 'r')

def display_arr(arr):
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end=" ")
        print()
    print()

from collections import deque, defaultdict

def find_usado(k, v):
    queue = deque()
    queue.append((v, float('inf')))
    visited = [0] * (N+1)
    visited[v] = 1
    count = 0

    while queue:
        cur, min_value = queue.popleft()

        for idx, usado in graph_dict[cur]:
            if not visited[idx]:
                visited[idx] = 1

                nx_usado = usado if min_value > usado else min_value
                queue.append((idx, nx_usado))

                if nx_usado >= k:
                    count += 1
    return count

N, Q = list(map(int, input().split()))
USADO = [list(map(int, input().split())) for _ in range(N-1)]
questions = [list(map(int, input().split())) for _ in range(Q)]

graph_dict = defaultdict(list)

for p, q, r in USADO:
    graph_dict[p].append((q, r))
    graph_dict[q].append((p, r))

for k, v in questions:
    print(find_usado(k, v))

    # for i in range(1, len(adj_arr[v])):
    #     if i == v:
    #         continue
    #
    #     if adj_arr[v][i] == 0:
    #         tmp = find_usado(v, i)
    #         adj_arr[v][i] = tmp
    #         adj_arr[i][v] = tmp
    #
    #         graph_dict[v].append(i)
    #         graph_dict[i].append(v)
    #
    #     if adj_arr[v][i] >= k:
    #         count += 1
    # print(count)

