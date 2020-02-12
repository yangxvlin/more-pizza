"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-2-12 15:52:44
Description: attempt the question
"""

import sys


def backpack_plan(max_value, n_item, weight):
    dp = [0 for _ in range(0, max_value)]
    choose_item = [False for _ in range(0, n_item)]

    for i in range(0, n_item):
        for j in weight[:i]:
            if dp[j] < dp[j - weight[i]] + weight[i]:
                dp[j] = dp[j - weight[i]] + weight[i]
                choose_item[i] = True
    return choose_item


def read_input(file_path: str):
    with open(file_path) as file:
        input_lines = file.readlines()
        line0, line1 = tuple(input_lines)
        m, n = tuple(line0.split(' '))
        slices = list(map(lambda x: int(x), line1.split(' ')))

    return int(m), int(n), slices


def write_output(file_name: str, pizza_chosen):


if __name__ == "__main__":
    max_slices, n_types, type_slices = read_input(sys.argv[1])
    pizza_chosen = backpack_plan(max_slices, n_types, type_slices)



