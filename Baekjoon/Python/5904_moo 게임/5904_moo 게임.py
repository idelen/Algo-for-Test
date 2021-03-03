import sys
sys.stdin = open('input.txt', 'r')

def findTarget(N, k):
    mdx = (sum_k_list[k] - (k + 3)) // 2 + 1

    if k == 0:
        if N == 1:
            return "m"
        else:
            return "o"
    else:
        if N < mdx:
            return findTarget(N, k-1)
        elif mdx <= N < mdx + (k+3):
            if N == mdx:
                return "m"
            else:
                return "o"
        else:
            return findTarget(N - sum_k_list[k-1] - (k+3), k-1)


N = int(input())
k = 0
sum_k_list = [3]
while N > sum_k_list[k]:
    k += 1
    nx_sum_k = 2 * sum_k_list[k-1] + (k+3)
    sum_k_list.append(nx_sum_k)

print(findTarget(N, k))
