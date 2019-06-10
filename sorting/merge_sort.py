# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
# Commented code is for calculating algorithm completixy and printing variables
from random import randint
import time
import sys

def merge_sort(array):
    # n = 0

    if len(array) > 1:
        half = len(array) // 2
        left_array = array[:half]
        right_array = array[half:]

        # n += merge_sort(left_array)
        # n += merge_sort(right_array)
        merge_sort(left_array)
        merge_sort(right_array)

        left_mark, right_mark, position = 0, 0, 0

        while left_mark < len(left_array) and right_mark < len(right_array):
            if left_array[left_mark] < right_array[right_mark]:
                array[position] = left_array[left_mark]
                left_mark += 1
            else:
                array[position] = right_array[right_mark]
                right_mark += 1
            position += 1
            # n += 1

        while left_mark < len(left_array):
            array[position] = left_array[left_mark]
            left_mark += 1
            position += 1
            # n += 1
        while right_mark < len(right_array):
            array[position] = right_array[right_mark]
            right_mark += 1
            position += 1
            # n += 1
    # return array, n
    return array


if __name__ == '__main__': 
    array = []
    random_number = 0
    try:
        number_of_elements = int(sys.argv[1])
    except:
        number_of_elements = 10

    for i in range(0, number_of_elements):
        random_number = randint(1, 9_999_999_999)
        array.append(random_number)
    # print(array)

    start_time = time.time()
    # array, n = merge_sort(array)
    array = merge_sort(array)
    running_time = time.time() - start_time

    # print(array)
    # print(n)
    print(running_time)