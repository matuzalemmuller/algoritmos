# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint

def mergeSort(array):
    n = 0

    if len(array) > 1:
        half = len(array) // 2
        lArray = array[:half]
        rArray = array[half:]

        n += mergeSort(lArray)
        n += mergeSort(rArray)

        lMark, rMark, position = 0, 0, 0

        while lMark < len(lArray) and rMark < len(rArray):
            if lArray[lMark] < rArray[rMark]:
                array[position] = lArray[lMark]
                lMark += 1
            else:
                array[position] = rArray[rMark]
                rMark += 1
            position += 1
            n += 1

        while lMark < len(lArray):
            array[position] = lArray[lMark]
            lMark += 1
            position += 1
            n += 1
        while rMark < len(rArray):
            array[position] = rArray[rMark]
            rMark += 1
            position += 1
            n += 1

    return n


if __name__ == '__main__': 
    array = []
    number_of_elements = 10

    i = 0
    while i < number_of_elements:
        array.append(randint(1, 9_999_999_999))
        i+=1

    print(array)
    n = mergeSort(array)
    print(array)
    print(n)