import sys
import timeit


def tri_insertion(data):
    comparison = 0
    iteration = 0

    tabData = data.split(";")
    # Parcour de 1 à la taille du tabData
    for i in range(1, len(tabData)): 
        iteration = iteration + 1
        k = tabData[i] 
        j = i-1
        comparison = comparison + 2
        while j >= 0 and k < tabData[j] :
            iteration = iteration + 1
            tabData[j + 1] = tabData[j] 
            j -= 1
        tabData[j + 1] = k

    return tabData, comparison, iteration


result = tri_insertion(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))
print("Nb d'iteration : " + str(result[2]))

time = timeit.Timer(lambda: tri_insertion(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))