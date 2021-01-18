import sys
import timeit


def selection_sort(data):
    comparison = 0
    iteration = 0

    tabData = data.split(";")
    for i in range(len(tabData)):
        iteration = iteration + 1
        minimumIndex = i
        for j in range(i + 1, len(tabData)):
            iteration = iteration + 1
            comparison = comparison + 1
            if tabData[minimumIndex] > tabData[j]:
                minimumIndex = j

        storage = tabData[i]
        tabData[i] = tabData[minimumIndex]
        tabData[minimumIndex] = storage

    return tabData, comparison, iteration


result = selection_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: selection_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
