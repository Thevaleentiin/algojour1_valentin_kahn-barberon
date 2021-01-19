import sys
import timeit


def selection_sort(data):
    comparison = 0
    iteration = 0

    tab_data = data.split(";")
    for i in range(len(tab_data)):
        iteration = iteration + 1
        minimum_index = i
        for j in range(i + 1, len(tab_data)):
            iteration = iteration + 1
            comparison = comparison + 1
            if tab_data[minimum_index] > tab_data[j]:
                minimum_index = j

        storage = tab_data[i]
        tab_data[i] = tab_data[minimum_index]
        tab_data[minimum_index] = storage

    return tab_data, comparison, iteration


result = selection_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: selection_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
