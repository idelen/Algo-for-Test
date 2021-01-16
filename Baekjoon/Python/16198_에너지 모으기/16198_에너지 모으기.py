import sys
sys.stdin = open('input.txt', 'r')

def dfs(numbers, result, N):
    global max_value
    if N == 3:
        result += numbers[0] * numbers[2]
        max_value = max(max_value, result)
        return 0

    for idx in range(1, N-1):
        dfs(numbers[:idx] + numbers[idx+1:], result + numbers[idx-1] * numbers[idx + 1], N-1)

N = int(input())
numbers = list(map(int, input().split()))
max_value = float('-inf')
dfs(numbers, 0, N)
print(max_value)