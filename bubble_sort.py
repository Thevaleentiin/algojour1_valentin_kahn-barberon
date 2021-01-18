import sys
import timeit

def bubble_sort(data):
    comparison = 0
    iteration = 0

    tabData = data.split(";")
    l = len(tabData)
    for i in range(l):
        iteration = iteration+1
        for j in range(0, l-i-1):
            comparison = comparison+1
            iteration = iteration+1
            if tabData[j] > tabData[j+1]:
                tabData[j], tabData[j+1] = tabData[j+1], tabData[j]

    return tabData, comparison, iteration

result = bubble_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: bubble_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))