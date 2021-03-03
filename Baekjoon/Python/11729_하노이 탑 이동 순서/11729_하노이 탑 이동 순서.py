import sys
sys.stdin = open('input.txt', 'r')

def hanoi(n, base, middle, target):
    if n == 1:
        print(base, target)
    else:
        hanoi(n - 1, base, target, middle)
        print(base, target)
        hanoi(n - 1, middle, base, target)

N = int(input())

move = []

print(2**N - 1)
hanoi(N, 1, 2, 3)