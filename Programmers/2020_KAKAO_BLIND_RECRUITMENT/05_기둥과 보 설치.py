BUILD_FRAMES = [
                [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
                [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
               ]

# 해당 위치에 설치 가능한지 검증
def is_check(columns, beams, x, y, a):
    #print(x, y, a)
    # 기둥인 경우
    if a == 0:
        # 바닥이면 바로 설치 가능
        if y == 0:
            return True
        else:
            # 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위
            if beams[x-1][y] or beams[x][y] or columns[x][y-1] == 1:
                return True
            else:
                return False
    # 보인 경우
    elif a == 1:
        # 한쪽 끝 부분이 기둥 위
        if columns[x][y-1] == 1 or columns[x+1][y-1] == 1:
            return True
        # 쪽 끝 부분이 다른 보와 동시에 연결되어 있음
        elif beams[x-1][y] == 1 and beams[x+1][y] == 1:
            return True
        else:
            return False

def solution(n, build_frame):
    answer = []

    columns = [[0] * (n + 1) for _ in range(n + 1)]
    beams = [[0] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        if b == 1:
            if is_check(columns, beams, x, y, a):
                if a == 0:
                    columns[x][y] = 1
                elif a == 1:
                    beams[x][y] = 1
        elif b == 0:
            if a == 0:
                columns[x][y] = 0
                flag = False
                for idx in range(n+1):
                    for jdx in range(n+1):
                        if columns[idx][jdx] == 1 and not is_check(columns, beams, idx, jdx, 0):
                            flag = True
                            break

                        if beams[idx][jdx] == 1 and not is_check(columns, beams, idx, jdx, 1):
                            flag = True
                            break

                    if flag:
                        columns[x][y] = 1
                        break

            elif a == 1:
                beams[x][y] = 0
                flag = False
                for idx in range(n + 1):
                    for jdx in range(n + 1):
                        if columns[idx][jdx] == 1 and not is_check(columns, beams, idx, jdx, 0):
                            flag = True
                            break

                        if beams[idx][jdx] == 1 and not is_check(columns, beams, idx, jdx, 1):
                            flag = True
                            break

                    if flag:
                        beams[x][y] = 1
                        break

    # columns 와 beams 를 돌며 현재 설치된 구조물 찾아서 answer에 저장
    for idx in range(n+1):
        for jdx in range(n+1):
            if columns[idx][jdx] == 1:
                answer.append([idx, jdx, 0])
            if beams[idx][jdx] == 1:
                answer.append([idx, jdx, 1])


    answer.sort()
    return answer




for i in range(len(BUILD_FRAMES)):
    print(i + 1, " 번 케이스!!")
    print(solution(5, BUILD_FRAMES[i]))
