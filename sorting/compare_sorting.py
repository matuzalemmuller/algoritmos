# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
# Performance comparison of sorting algorithms
import bucket_sort
import insertion_sort
import merge_sort
import radix_sort
import time
import sys
from random import randint

if __name__ == '__main__': 
    random_number = 0
    size_of_arrays = 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536
    array = [list() for _ in range(len(size_of_arrays))]

    for i in range(0, len(size_of_arrays)):
        for j in range(0, size_of_arrays[i]):
            random_number = randint(1, 9_999_999_999)
            array[i].append(random_number)

    # Runs all sorting algorithms and measures running time
    for i in range(0, len(array)):
        print("-------------------------------------")
        print("N = " + str(size_of_arrays[i]))

        # Radix Sort
        array_copy = array[i].copy()
        start_time = time.time()
        radix_sort.radix_sort(array_copy)
        running_time = time.time() - start_time
        print("Radix sort: " + str(running_time))

        # Merge Sort
        array_copy = array[i].copy()
        start_time = time.time()
        merge_sort.merge_sort(array_copy)
        running_time = time.time() - start_time
        print("Merge sort: " + str(running_time))

        # Bucket Sort
        array_copy = array[i].copy()
        start_time = time.time()
        bucket_sort.bucket_sort(array_copy)
        running_time = time.time() - start_time
        print("Bucket sort: " + str(running_time))

        # Insertion Sort
        array_copy = array[i].copy()
        start_time = time.time()
        insertion_sort.insertion_sort(array_copy)
        running_time = time.time() - start_time
        print("Insertion sort: " + str(running_time) + "\n")