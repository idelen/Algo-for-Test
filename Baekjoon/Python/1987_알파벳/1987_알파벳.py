import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_wall(x, y):
    return x < 0 or x >= R or y < 0 or y >= C

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        board[i][j] = 1 << (ord(board[i][j])-65)

que = deque()
que.append([0, 0, board[0][0], 1])
visited = [[0] * C for _ in range(R)]
visited[0][0] = board[0][0]

max_value = 0

while que:
    x, y, root, cnt = que.popleft()

    if cnt == 26:
        max_value = 26
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not is_wall(nx, ny) and not (root & board[nx][ny]) and visited[nx][ny] != root + board[nx][ny]:
            visited[nx][ny] = root + board[nx][ny]
            que.append([nx, ny, root + board[nx][ny], cnt + 1])

    max_value = max(max_value, cnt)

print(max_value)