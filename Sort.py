def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


list = [113, 639, 103, 126, 899, 788, 665, 1]
list = bubble_sort(list)
print(list)
