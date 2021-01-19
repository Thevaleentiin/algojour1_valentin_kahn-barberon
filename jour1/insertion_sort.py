import sys
import timeit


def insertion_sort(data):
    comparison = 0
    iteration = 0

    tab_data = data.split(";")
    for i in range(1, len(tab_data)):
        iteration = iteration + 1
        k = tab_data[i]
        j = i-1
        comparison = comparison + 2
        while j >= 0 and k < tab_data[j]:
            iteration = iteration + 1
            tab_data[j + 1] = tab_data[j]
            j -= 1
            comparison = comparison + 2
        tab_data[j + 1] = k

    return tab_data, comparison, iteration


result = insertion_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: insertion_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
