SAMPLE = [
    [[14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]],
    [[5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]],
    [[5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]]],
    [[10, 10, 1, 1],[[3,2], [4,3], [1,4]]]
]

def is_complete(attend):
    for v in attend.values():
        if v == 0:
            return False
    return True

def find_member(sales, chart, team_check, attended_team, visited, mdx, price):
    global min_value

    if is_complete(attended_team):
        if min_value > price:
            # print(price, visited)
            # print(attended_team)
            min_value = price
        return
    elif mdx >= len(sales):
        return
    else:
        for cur in range(mdx, len(sales)):
            if not visited[cur]:
                team_numbers = team_check[cur]

                for team_number in team_numbers:
                    attended_team[team_number] += 1
                visited[cur] = 1
                price += sales[cur]
                if price < min_value:
                    find_member(sales, chart, team_check, attended_team, visited, cur+1, price)

                for team_number in team_numbers:
                    attended_team[team_number] -= 1

                visited[cur] = 0
                price -= sales[cur]


import sys

def solution(sales, links):
    answer = 0
    global min_value
    min_value = sys.maxsize

    # 1번부터 시작이기에 인덱스번호 맞추기용
    sales = [0] + sales
    links = [[]] + links

    chart = {}
    team_check = {}

    for idx in range(1, len(links)):
        a, b = links[idx]
        if chart.get(a) == None:
            chart[a] = [a, b]
        else:
            chart[a].append(b)

    attended_team = {}

    for key, value in chart.items():
        members = value
        attended_team[key] = 0
        for member in members:
            if team_check.get(member) == None:
                team_check[member] = [key]
            else:
                team_check[member].append(key)

    print("chart : ", chart)
    print("team_check : ", team_check)
    print("attended_team : ", attended_team)

    visited = [0] * len(sales)

    find_member(sales, chart, team_check, attended_team, visited, 1, 0)

    answer = min_value

    return answer


for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    sales, links = SAMPLE[i]
    print(sales, links)
    print(solution(sales, links))