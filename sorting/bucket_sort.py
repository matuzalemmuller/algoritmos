# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint

def bucket_sort(array):
    num_buckets = len(array)
    buckets = [[] for bucket in range(num_buckets)]

    for value in array:
        index = value * num_buckets // (max(array) + 1)
        buckets[index].append(value)

    sorted_list = []
    n = 1

    for i in range(num_buckets):
        next, m = insertion_sort(buckets[i])
        sorted_list.extend(next)
        n += m + 1              # Cost of insertion sort + extend list

    return sorted_list, n

def insertion_sort(array): 
    n = 1
    
    for i in range(1, len(array)): 
        n += 1
        key = array[i] 
        j = i-1
        while j >= 0 and key < array[j]: 
                n += 1
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = key
    
    return array, n
  

if __name__ == '__main__': 
    array = []
    number_of_elements = 10
    random_number = 0

    i = 0
    while i < number_of_elements:
        random_number = randint(1, 9_999_999_999)
        array.append(random_number)
        i+=1

    print(array)
    array, n = bucket_sort(array)
    print(array)
    print(n)