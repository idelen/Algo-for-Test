SAMPLE = [[[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]]]
#SAMPLE = [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]]]



def display(arr):
    for ii in range(len(arr)):
        for jj in range(len(arr[ii])):
            print(arr[ii][jj], end=' ')
        print()
    print()


def is_open(key, check_box, dx, dy, N):
    temp_box = [[check_box[idx][jdx] for jdx in range(len(check_box))] for idx in range(len(check_box))]

    for idx in range(len(key)):
        for jdx in range(len(key)):
            temp_box[idx+dx][jdx+dy] += key[idx][jdx]

    # print(dx, dy)
    # display(temp_box)

    for idx in range(len(key), len(key) + N):
        for jdx in range(len(key), len(key) + N):
            if temp_box[idx][jdx] != 1:
                return False

    return True


def solution(key, lock):
    answer = True

    M, N = len(key), len(lock)
    K = M + N + M
    check_box = [[0] * K for _ in range(K)]


    # check_box 에 lock을 복사
    for idx in range(M, M+N):
        for jdx in range(M, M+N):
            check_box[idx][jdx] = lock[idx-M][jdx-M]

    loop_count = 0
    while 1:
        # print("===== key =====")
        # display(key)
        for dx in range(K-M):
            for dy in range(K-M):
                if is_open(key, check_box, dx, dy, N):
                    return answer
                    pass

        # key 회전 (원래 모양은 제외하기에 3번)
        if loop_count == 3:
            answer = False
            break

        rotate_key = [[0] * M for _ in range(M)]

        for idx in range(M):
            temp = key[idx]

            for jdx in range(M):
                rotate_key[jdx][M-1-idx] = temp[jdx]

        key = rotate_key

        loop_count += 1

    return answer



for i in range(len(SAMPLE)):
    print(SAMPLE[i])
    key, lock = SAMPLE[i]
    print(i+1, "번 케이스 : ", key, lock)
    print(solution(key, lock))

# import random
#
# while 1:
#     N = random.randrange(4, 5)
#     M = random.randrange(4, N+1)
#
#     key = [[0] * M for _ in range(M)]
#     lock = [[0] * N for _ in range(N)]
#
#     for x in range(M):
#         for y in range(M):
#             key[x][y] = random.randrange(0, 2)
#
#     for x in range(N):
#         for y in range(N):
#             lock[x][y] = random.randrange(0, 2)
#
#     print("key")
#     display(key)
#     print("lock")
#     display(lock)
#
#     if solution(key, lock):
#         print("True")
#         break
#     break