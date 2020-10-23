import sys
sys.stdin = open('input.txt', 'r')


def findGreatSequence(a1, n):
    greatSequence.append(a1)
    greatSequence.append(a1)

    sampleSum = sum(greatSequence)

    for k in range(2, n):
        # greatSequence.append(findSumPowerset(greatSequence))
        greatSequence.append(sampleSum * pow(2, k - 1))
        sampleSum += greatSequence[-1]

def findSequence(a1, n, i):
    if i == 1:
        res = a1
    elif i == 2:
        res = a1 + a1

    s = a1 + a1
    sampleSum = a1 + a1
    for k in range(2, n):
        s = sampleSum * pow(2, k - 1)
        sampleSum += s

        if k == i-1:
           res = s

    return res, s

def findSequence2(a1, n):
    s = a1 + a1
    sampleSum = a1 + a1
    for k in range(2, n):
        s = sampleSum * pow(2, k - 1)
        sampleSum += s
    return s


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def find_lcm(x, y):
    return x * y // find_gcd(x, y)


Q = int(input())

for t in range(Q):
    query = list(map(int, input().split()))

    greatSequence = []

    if query[0] == 1:
        a1, i, j = query[1:]

        ai, aj = findSequence(a1, j, i)
        result = find_gcd(ai, aj) % 1000000007

    elif query[0] == 2:
        a1, i, j = query[1:]

        ai, aj = findSequence(a1, j, i)
        L = find_lcm(ai, aj)

        for i in range(L):
            if L % 2 != 0:
                result = i % 1000000007
                break
    elif query[0] == 3:
        a1, i, j = query[1:]
        findGreatSequence(a1, j)

        result = sum(greatSequence[i - 1:j]) % 1000000007

    elif query[0] == 4:
        a1, k = query[1:]

        result = findSequence2(a1, k) % 1000000007

    print(result)