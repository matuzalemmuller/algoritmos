# UFSC - Campus Trindade
# PPGEAS - Introducao a Algoritmos
# Matuzalem Muller dos Santos
# 2019/1
from random import randint

def radix_sort(array):
    position = 1
    max_number = max(array)

    n = 0

    while position < max_number:
        queue_list = [list() for _ in range(10)]

        for num in array:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        index = 0
        for numbers in queue_list:
            for num in numbers:
                array[index] = num
                index += 1

        n += 1

        position *= 10
    return n


if __name__ == '__main__': 
    array = []
    number_of_elements = 20
    random_number = 0

    i = 0
    while i < number_of_elements:
        array.append(randint(1, 9_999_999_999))
        i+=1

    print(array)
    n = radix_sort(array)
    print(array)
    print(n)