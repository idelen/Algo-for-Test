import sys
sys.stdin = open('input.txt', 'r')

T = 3

def calculator(used_op, cur, answer):
    global first, second
    if cur == N:
        if first < answer:
            first = answer

        if second > answer:
            second = answer
    else:
        for op_idx in range(4):
            if used_op[op_idx] < operations[op_idx]:
                used_op[op_idx] += 1

                if op_idx == 0:
                    calculator(used_op, cur+1, answer + numbers[cur])
                elif op_idx == 1:
                    calculator(used_op, cur+1, answer - numbers[cur])
                elif op_idx == 2:
                    calculator(used_op, cur+1, answer * numbers[cur])
                elif op_idx == 3:
                    is_adjust = 1 if answer >= 0 else -1
                    calculator(used_op, cur+1, abs(answer) // numbers[cur] * is_adjust)

                used_op[op_idx] -= 1
            else:
                continue

for t in range(T):
    print(t, "번 문제 : ")

    N = int(input())
    numbers = list(map(int, input().split()))
    operations = list(map(int, input().split()))

    first, second = -(10**10), 10**10
    used_op = [0, 0, 0, 0]

    calculator(used_op, 1, numbers[0])

    print(first)
    print(second)