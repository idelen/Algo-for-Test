import sys
sys.stdin = open('input.txt', 'r')

import sys
sys.setrecursionlimit(5000)

def hanoi(n, start, mid, end):
    pass

n = int(input())
current = list(map(int, input().split()))
disks = [list(map(int, input().split())) for _ in range(3)]
end = -1

for i in range(3):
    if max(disks[i]) == n:
        end = i

