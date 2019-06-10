# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint
import insertion_sort
import time
import sys

def bucket_sort(array):
    # n = 0
    largest = max(array)
    length = len(array)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(array[i]/size)
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])
        # n += 1
 
    for i in range(length):
        # buckets[i], m = insertion_sort.insertion_sort(buckets[i])
        # n += m
        insertion_sort.insertion_sort(buckets[i])
 
    array = []
    for i in range(length):
        array = array + buckets[i]
 
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
    # array, n = bucket_sort(array)
    array = bucket_sort(array)
    running_time = time.time() - start_time

    # print(array)
    # print(n)
    print(running_time)