import sys
import timeit

comparison = 0
iteration = 0

def get_next_gap(gap):
    global comparison
    gap = (gap * 10) / 13
    comparison = comparison + 1
    if gap < 1: 
        return 1
    return gap 

def comb_sort(tab_data):
    global comparison
    global iteration
    length = len(tab_data) 
    gap = length 
    swapped = True
    comparison = comparison + 2
    while gap != 1 or swapped == 1: 
        iteration = iteration + 1
        gap = get_next_gap(gap) 
        swapped = False
        for i in range(0, int(length - gap)):
            iteration = iteration + 1
            comparison = comparison + 1
            if float(tab_data[i]) > float(tab_data[int(i + gap)]): 
                tab_data[i], tab_data[int(i + gap)] = tab_data[int(i + gap)], tab_data[i] 
                swapped = True
    return tab_data

data = sys.argv[1]
tab_data = str(data).split(";")
result = comb_sort(tab_data)

print("Serie : " + sys.argv[1])
print("Resultat : " + ";".join(result))
print("Nb d'iteration : " + str(iteration))
print("Nb de comparaison : " + str(comparison))

time = timeit.Timer(lambda: comb_sort(tab_data))
print("Temps (sec) : " + str(time.timeit(10000) / 10000))