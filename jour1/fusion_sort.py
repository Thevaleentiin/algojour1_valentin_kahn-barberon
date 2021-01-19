import sys
import timeit


def fusion(tab1, tab2):
    comparison = 0
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


def tri_fusion_recursif(tab_data, comparison):
    n = len(tab_data)
    comparison = comparison + 1
    recusive_result1 = [0, 0]
    recusive_result2 = [0, 0]
    if n > 1:
        p = int(n/2)
        tab1 = tab_data[0:p]
        tab2 = tab_data[p:n]
        recusive_result1 = tri_fusion_recursif(tab1, comparison)
        recusive_result2 = tri_fusion_recursif(tab2, comparison)
        tab_data[:] = fusion(tab1, tab2)

    return tab_data, recusive_result1[1] + recusive_result2[1] + comparison


def fusion_sort(data):
    comparison = 0
    tab_data = data.split(";")

    recusive_result = tri_fusion_recursif(tab_data, comparison)

    return tab_data, recusive_result[1]


result = fusion_sort(sys.argv[1])

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result[0]))
print("Nb de comparaison : " + str(result[1]))

time = timeit.Timer(lambda: fusion_sort(sys.argv[1]))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))
