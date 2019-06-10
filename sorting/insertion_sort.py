# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
# Commented code is for calculating algorithm completixy and printing variables
from random import randint
import time
import sys

def insertion_sort(array): 
    # n = 1
    
    for i in range(1, len(array)): 
        # n += 1
        key = array[i] 
        j = i-1
        while j >= 0 and key < array[j]: 
                # n += 1
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = key
    
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
    # array, n = insertion_sort(array)
    array = insertion_sort(array)
    running_time = time.time() - start_time

    # print(array)
    # print(n)
    print(running_time)