"""Реализовать функцию get_ranges которая получает
на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9" """

lst = [1, 2, 3, 4, 7, 8, 9, 12]
i = 0
while lst:
    if lst[i + 1] - lst[i] != 1:
        new_lst = lst[:i+1]
        i += 1
    else:
        lst = lst[i:]
        i = 0
        print(lst)

