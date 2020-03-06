import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)


def quick_sorting_no_mem(array, fst, lst):
    print('array = ', array)
    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    print('pivot = ', pivot)
    i, j = fst, lst
    print('i, j = ', i, j)

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            print('arr_i, arr_j = ', array[i], array[j])
            i, j = i + 1, j - 1

    quick_sorting_no_mem(array, fst, j)
    quick_sorting_no_mem(array, i, lst)


quick_sorting_no_mem(array, 0, len(array) - 1)
print(array)