import sys
import timeit


def shell_sort(data):
    comparison = 0
    iteration = 0

    tab_data = data.split(";")

    n = len(tab_data)
    gap = n/2

    comparison = comparison + 1
    while gap > 0:
        iteration = iteration + 1
        for i in range(gap, n):
            iteration = iteration + 1
            temp = tab_data[i]
            j = i
            comparison = comparison + 2
            while j >= gap and tab_data[j-gap] > temp:
                iteration = iteration + 1
                tab_data[j] = tab_data[j-gap]
                j -= gap
                comparison = comparison + 2
            tab_data[j] = temp
        comparison = comparison + 1
        gap /= 2

    return tab_data, comparison, iteration


result = shell_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: shell_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
