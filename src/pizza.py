"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-2-12 15:52:44
Description: attempt the question
"""

import sys


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
    for i in range(1, n_item + 1):
        for j in range(1, max_value + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weight[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i - 1]] + weight[i - 1])

    j = max_value
    for i in range(n_item-1, -1, -1):
        if dp[i+1][j] == dp[i][j-weight[i]] + weight[i]:
            j -= weight[i]
            choose_item[i] = True

    return choose_item


def simulation(max_value, n_item, weight):
    best_solution = []

    score = 0
    i = n_item - 1
    test1 = True
    test2 = True
    while i >= 0 and test1:
        current_best_solution = []
        j = i
        cur_sum = 0

        while j >= 0 and test2:
            temp = weight[j]
            cur_try = cur_sum + temp
            if cur_try <= max_value:
                cur_sum += temp
                current_best_solution.append(j)
                if cur_try == max_value:
                    test1 = False
                    test2 = False

            j -= 1

        if score < cur_sum:
            score = cur_sum
            best_solution = current_best_solution
        if len(best_solution) == n_item:
            test1 = False

        i -= 1

        print(best_solution)

    return best_solution


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
    pizza_chosen = None
    try:
        pizza_chosen = backpack_plan(max_slices, n_types, type_slices)
    except MemoryError:
        pizza_chosen = simulation(max_slices, n_types, type_slices)
    write_output(sys.argv[1].split('.')[0][3:], pizza_chosen)
