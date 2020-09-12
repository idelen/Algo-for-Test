SAMPLE = [
    [
        ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
        , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    ]
]

# language = [0: "cpp", 1: "java", 2: "python"]
# job = [0: "backend", 1: "frontend"]
# career = [0: "junior", 1: "senior"]
# food = [0: "chicken", 1: "pizza"]

class Applicant:
    def __init__(self, language, job, career, food, score):
        self.language = language
        self.job = job
        self.career = career
        self.food = food
        self.score = score



def solution(info, query):
    answer = []

    sample_condition = []

    language = {"cpp": [], "java": [], "python": []}
    job = {"backend": [], "frontend": []}
    career = {"junior": [], "senior": []}
    food = {"chicken": [], "pizza": []}

    sample_condition.append(language)
    sample_condition.append(job)
    sample_condition.append(career)
    sample_condition.append(food)

    applicant_list = []
    score_list = []

    for idx in range(len(info)):
        spec = info[idx].split(' ')
        print("spec: ", spec)

        applicant = Applicant(spec[0], spec[1], spec[2], spec[3], spec[4])

        applicant_list.append(applicant)
        score_list.append(int(spec[4]))

        for sdx in range(len(sample_condition)):
            sample_condition[sdx][spec[sdx]].append(idx)

        # language[spec[0]].append(idx)
        # job[spec[1]].append(idx)
        # career[spec[2]].append(idx)
        # food[spec[3]].append(idx)


    for idx in range(len(query)):
        conditions = query[idx].split(' and ')
        conditions = conditions[:3] + conditions[3].split(' ')

        is_right = [1] * len(info)

        for cdx in range(len(conditions)):
            print(conditions)
            condition = conditions[cdx]
            print(condition)

            if condition == '-':
                continue
            # 점수조건
            elif cdx == len(conditions) - 1:
                standard = int(condition)
                for score_idx in range(len(score_list)):
                    if score_list[score_idx] < standard:
                        is_right[score_idx] = 0
            else:
                match = sample_condition[cdx][condition]
                mdx = 0
                for rdx in range(len(is_right)):
                    if mdx == len(match):
                        break

                    if rdx == match[mdx]:
                        mdx += 1
                    else:
                        is_right[rdx] = 0

        answer.append(sum(is_right))

    return answer


for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    info, query = SAMPLE[i]
    print(solution(info, query))