def merge_lists(list1, list2):
    merged = []
    for order in list1:
        while order > list2[0]:
            merged.append(list2[0])
            list2 = list2[1:]
        merged.append(order)
    return merged

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
