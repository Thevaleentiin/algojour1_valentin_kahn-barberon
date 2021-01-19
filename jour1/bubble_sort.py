import sys
import timeit


def bubble_sort(data):
    comparison = 0
    iteration = 0

    tab_data = data.split(";")
    l = len(tab_data)
    for i in range(l):
        iteration = iteration + 1
        for j in range(0, l - i - 1):
            iteration = iteration + 1
            comparison = comparison + 1
            if tab_data[j] > tab_data[j + 1]:
                tab_data[j], tab_data[j + 1] = tab_data[j + 1], tab_data[j]

    return tab_data, comparison, iteration


result = bubble_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: bubble_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
