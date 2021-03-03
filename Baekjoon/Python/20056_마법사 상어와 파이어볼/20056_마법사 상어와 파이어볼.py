import sys
sys.stdin = open('input.txt', 'r')

def display(arr):
    print()
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end=' ')
        print()
    print()

def simulation(K, fireballs):
    for k in range(K):
        new_field = [[-1] * (N) for _ in range(N)]
        new_fireballs = []

        # 1. 이동
        for idx in range(len(fireballs)):
            r, c, m, s, d = fireballs[idx]
            dx, dy = directions[d]

            nr, nc = r + s*dx, c + s*dy

            nr = nr if 0 <= nr < N else nr % N
            nc = nc if 0 <= nc < N else nc % N

            nc = nc if nc <= N else N

            if new_field[nr][nc] == -1:
                new_field[nr][nc] = [idx]
            else:
                new_field[nr][nc].append(idx)
        display(new_field)
        # 2. 중복검사
        for idx in range(N):
            for jdx in range(N):
                positions = new_field[idx][jdx]

                if positions != -1:
                    if len(positions) == 1:
                        cur = positions[0]
                        m, s, d = fireballs[cur][2:]

                        new_fireballs.append([idx, jdx, m, s, d])
                    else:
                        mass_sum, velocity_sum = 0, 0
                        d_flag1, d_flag2 = 0, 1
                        for cur in positions:
                            m, s, d = fireballs[cur][2:]

                            mass_sum += m
                            velocity_sum += s

                            d_flag1 = d_flag1 or (d % 2)    # 하나라도 홀수면 1
                            d_flag2 = d_flag2 and (d % 2)   # 하나라도 짝수면 0

                        new_m = mass_sum // 5
                        new_s = velocity_sum // len(positions)

                        if new_m != 0:
                            if d_flag1 == d_flag2:
                                [new_fireballs.append([idx, jdx, new_m, new_s, 2*dd]) for dd in range(4)]
                            else:
                                [new_fireballs.append([idx, jdx, new_m, new_s, 2*dd + 1]) for dd in range(4)]

        fireballs = new_fireballs
        print(fireballs)

    result = 0
    for r, c, m, s, d in fireballs:
        result += m
    return result



for t in range(4):
    print(t+1, "번 문제")
    N, M, K = map(int, input().split())
    fireballs = [list(map(int, input().split())) for _ in range(M)]

    for fireball in fireballs:
        fireball[1] -= 1
        fireball[0] -= 1

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    print(fireballs)
    print(simulation(K, fireballs))
