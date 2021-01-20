import sys

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(tab_data, start, end):
    if start >= end:
        return

    p = partition(tab_data, start, end)
    quick_sort(tab_data, start, p-1)
    quick_sort(tab_data, p+1, end)
    return tab_data

data = sys.argv[1]
tab_data = str(data).split(";")
print(quick_sort(tab_data, 0, len(tab_data) - 1))