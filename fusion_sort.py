import sys
import timeit

comparison = 0
iteration = 0


def fusion(tab1, tab2):
    global comparison
    l1 = len(tab1)
    l2 = len(tab2)
    complete_tab = [0] * (l1 + l2)
    i1 = 0
    i2 = 0
    i = 0
    comparison = comparison + 2
    while i1 < l1 and i2 < l2:
        comparison = comparison + 1
        if tab1[i1] < tab2[i2]:
            complete_tab[i] = tab1[i1]
            i1 += 1
        else:
            complete_tab[i] = tab2[i2]
            i2 += 1
        i += 1
        comparison = comparison + 2
    comparison = comparison + 1
    while i1 < l1:
        complete_tab[i] = tab1[i1]
        i1 += 1
        i += 1
        comparison = comparison + 1
    comparison = comparison + 1
    while i2 < l2:
        complete_tab[i] = tab2[i2]
        i2 += 1
        i += 1
        comparison = comparison + 1
    return complete_tab


def tri_fusion_recursif(tab_data):
    global comparison, iteration
    iteration = iteration + 1
    n = len(tab_data)
    comparison = comparison + 1
    if n > 1:
        p = int(n/2)
        tab1 = tab_data[0:p]
        tab2 = tab_data[p:n]
        tri_fusion_recursif(tab1)
        tri_fusion_recursif(tab2)
        tab_data[:] = fusion(tab1, tab2)

    return tab_data


def fusion_sort(data):
    tab_data = data.split(";")

    tri_fusion_recursif(tab_data)

    return tab_data, comparison, iteration


result = fusion_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(comparison))
print("Nb d'iteration : " + str(iteration))

time = timeit.Timer(lambda: fusion_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
