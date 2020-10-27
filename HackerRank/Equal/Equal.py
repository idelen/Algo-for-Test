#!/bin/python3

import math
import os
import random
import re
import sys

delta_count = {}


# Complete the equal function below.
def equal(arr):
    count = 0

    while 1:
        n = len(arr)

        max_value = max(arr)
        max_idx = arr.index(max_value)
        min_value = min(arr)

        delta = max_value - min_value

        for i in range(n):
            if i != max_idx:
                arr[i] += delta

        if delta_count.get(delta) == None:
            tmp_cnt = 0

            while 1:
                if delta >= 5:
                    share = delta // 5
                    delta = delta % 5
                    tmp_cnt += share
                elif delta >= 2:
                    share = delta // 2
                    delta = delta % 2
                    tmp_cnt += share
                elif delta >= 1:
                    delta -= 1
                    tmp_cnt += 1
                else:
                    delta_count[delta] = tmp_cnt
                    break

        count += delta_count[delta]

        for i in range(n - 1):
            if arr[i] != arr[i + 1]:
                break
        else:
            break
    return count


sys.stdin = open("input.txt", "r")

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        print(t_itr+1, "번 케이스 : ", result)