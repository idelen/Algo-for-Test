SAMPLE = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

def solution(s):
    answer = 0

    min_string_length = 10000

    for length in range(1, len(s)+1):
        # print("new length : ", length)
        now_iterator = s[:length]
        count = 1

        temp_answer = ""
        for tdx in range(length, len(s), length):
            text = s[tdx:tdx+length]
            # print(now_iterator, text, count)
            # print(temp_answer)
            if now_iterator == text:
                count += 1
            elif count == 1:
                temp_answer = temp_answer + now_iterator
                now_iterator = text
                count = 1
            else:
                temp_answer = temp_answer + now_iterator + str(count)
                now_iterator = text
                count = 1
        else:
            if count == 1:
                temp_answer = temp_answer + now_iterator
            else:
                temp_answer = temp_answer + now_iterator + str(count)

            temp_string_length = len(temp_answer)

            if min_string_length > temp_string_length:
                # print(temp_answer)
                min_string_length = temp_string_length

    answer = min_string_length


    return answer





for i in range(len(SAMPLE)):
    s = SAMPLE[i]
    print(i+1, " 번 케이스 : ", s)
    print(solution(s))