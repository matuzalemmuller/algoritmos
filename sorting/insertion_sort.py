# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint

def insertionSort(array): 
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
    
    return n
  

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
    n = insertionSort(array) 
    print(array)
    print(n)