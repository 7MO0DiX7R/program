def bubble_sort(our_list):
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j + 1]:
                our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]

    return our_list


our_list = [113, 639, 103, 126, 899, 788, 665, 1]
our_list = bubble_sort(our_list)
print(our_list)
