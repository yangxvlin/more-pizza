"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-2-12 15:52:44
Description: attempt the question
"""

import sys
import numpy as np


OUTPUT_DIR = "out/"
OUTPUT_FILE_TYPE = ".out"


def backpack_plan(max_value, n_item, weight):
    choose_item = [False for _ in range(0, n_item)]
    # optimized memory use 1-dimensional version
    # dp = [0 for _ in range(0, max_value+1)]
    #
    # for i in range(1, n_item+1):
    #     j = max_value
    #     while j >= weight[i-1]:
    #         print(i, j)
    #         if dp[j] < dp[j - weight[i-1]] + weight[i-1]:
    #             dp[j] = dp[j - weight[i-1]] + weight[i-1]
    #             choose_item[i-1] = True
    #         j -= 1

    # 2-dimensional version
    dp = [[0 for _ in range(max_value + 1)] for _ in range(n_item + 1)]
    # print((n_item + 1) * (max_value + 1))
    # dp = np.zeros((n_item + 1, max_value + 1))
    # choose_item = [[False for _ in range(max_value + 1)] for _ in range(n_item + 1)]
    for i in range(1, n_item + 1):
        for j in range(1, max_value + 1):
            dp[i][j] = dp[i - 1][j]
            # choose_item[i][j] = False
            if j >= weight[i - 1]:
                # pre = dp[i][j]
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + weight[i - 1])
                # if dp[i-1][j - weight[i-1]] + weight[i-1] > pre:
                #     choose_item[i][j] = True

    j = max_value
    for i in range(n_item-1, -1, -1):
        # print(i, j, dp[i][j], dp[i-1][j-weight[i]] + weight[i])
        if dp[i+1][j] == dp[i][j-weight[i]] + weight[i]:
            j -= weight[i]
            choose_item[i] = True

    # print(dp[-1][-1])
    # print(choose_item)
    return choose_item


def read_input(file_path: str):
    with open(file_path) as file:
        input_lines = file.readlines()
        line0, line1 = tuple(input_lines)
        m, n = tuple(line0.split(' '))
        slices = list(map(lambda x: int(x), line1.split(' ')))

    return int(m), int(n), slices


def write_output(file_name: str, pizza_chosen_plan):
    file_path = OUTPUT_DIR + file_name + OUTPUT_FILE_TYPE

    n_chosen = 0
    chosen = []

    for i in range(0, len(pizza_chosen_plan)):
        if pizza_chosen_plan[i]:
            n_chosen += 1
            chosen.append(i)

    with open(file_path, "w") as file:
        file.write(str(n_chosen) + '\n')
        file.write(" ".join(map(str, chosen)) + '\n')


if __name__ == "__main__":
    max_slices, n_types, type_slices = read_input(sys.argv[1])
    # print(max_slices, n_types, type_slices)
    pizza_chosen = backpack_plan(max_slices, n_types, type_slices)
    write_output(sys.argv[1].split('.')[0][3:], pizza_chosen)
