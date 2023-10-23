def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)// 2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


my_list = sorted([5, 7, 3, 67, 9])

print (binary_search(my_list, 78))