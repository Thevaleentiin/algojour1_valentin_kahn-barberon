import sys
import timeit

comparison = 0
iteration = 0

def partition(array, start, end):
    global comparison
    global iteration
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        iteration = iteration + 1
        comparison = comparison + 2
        while low <= high and float(array[high]) >= float(pivot):
            iteration = iteration + 1
            high = high - 1
            comparison = comparison + 2

        comparison = comparison + 2
        while low <= high and float(array[low]) <= float(pivot):
            iteration = iteration + 1
            low = low + 1
            comparison = comparison + 2

        comparison = comparison + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(tab_data, start, end):
    global comparison
    comparison = comparison + 1
    if start >= end:
        return

    p = partition(tab_data, start, end)
    quick_sort(tab_data, start, p-1)
    quick_sort(tab_data, p+1, end)
    return tab_data

data = sys.argv[1]
tab_data = str(data).split(";")
result = quick_sort(tab_data, 0, len(tab_data) - 1)

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result))
print("Nb d'iteration : " + str(iteration))
print("Nb de comparaison : " + str(comparison))
time = timeit.Timer(lambda: quick_sort(tab_data, 0, len(tab_data) - 1))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))