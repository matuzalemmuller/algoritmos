# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
# Commented code is for calculating algorithm completixy and printing variables
from random import randint
import time
import sys

def radix_sort(array):
    # n = 0
    position = 1
    max_number = max(array)

    while position < max_number:
        queue_list = [list() for _ in range(10)]

        # Gets row of digits from arrays
        for num in array:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        # Sorts arrays according to radix
        index = 0
        for numbers in queue_list:
            for num in numbers:
                array[index] = num
                index += 1
                # n += 1

        position *= 10
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
    # array, n = radix_sort(array)
    array = radix_sort(array)
    running_time = time.time() - start_time

    # print(array)
    # print(n)
    print(running_time)