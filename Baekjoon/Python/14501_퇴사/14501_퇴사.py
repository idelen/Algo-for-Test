import sys
sys.stdin = open('input.txt', 'r')


def find_max(day, dp, pay):
    if day == N:
        dp[N] = max(dp[N], pay)
        return

    if dp[day] > pay:
        return
    else:
        dp[day] = pay

    if day+T[day] <= N:
        find_max(day+T[day], dp, pay+P[day])

    if day+1 <= N:
        find_max(day+1, dp, pay)

    return


for problem in range(4):
    print(problem+1, "번 문제")
    N = int(input())
    T, P = [], []

    for i in range(N):
        ti, pi = map(int, input().split())
        T.append(ti)
        P.append(pi)

    dp = [0] * (N+1)

    find_max(0, dp, 0)

    print(max(dp))