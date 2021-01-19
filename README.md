# algojour1

#TD10 - Jérémy Blahak - Valentin Kahn - Hugo Pérard

## General

Pour chacun de nos algorithmes de tri, on commence par récupérer l'argument
sous forme de string de type "a;b;c;d", pour le convertir en tableau.
Pour nos explications, on estime qu'un tableau trié est un tableau 
rangé dans l'ordre croissant, et L sera la taille du tableau qu'on veut trier

## Bubble sort

Le tri a bulle compare les éléments consécutifs. Il est appelé ainsi
car on fait remonter les éléments au fur et à mesure dans le tableau pour
les trier, comme des bulles qui remontent à la surface.
* L'algorithme fonctionne de la manière suivante :
    * On prend le premier élément du tableau et on le compare au suivant :
        * Si notre élément est inférieur au suivant : 
            * on inverse les positions des deux éléments comparé
        * Sinon : 
            * on ne change pas les éléments de place
        * Puis on effectue la même chose avec le deuxième élément, jusqu'à
        être arrivé à la fin du tableau
    * On effectue L fois cette action

## Selection sort

Le tri par sélection est relativement simple. Il fonctionne de la
manière suivante :
* On parcourt le tableau pour trouver l'élément le plus petit
    * On extrait ce minimum du tableau et on l'ajoute dans le nouveau
    tableau (au début pour le premier élément, à la suite pour les suivants)
* On effectue L fois cette action

## Insertion sort

Le tri par insertion est un algorithme de comparaison, il fonctionne
de la manière suivante :
* On parcourt le tableau à partir du deuxième élément
    * Pour chaque élément, on le compare aux valeurs qui le précède 
    afin de déterminer à quel endroit il doit être placé
L'aspect important de ce tri, est que la partie à gauche de l'élément
qu'on veut trier est triée, et donc on ajoute l'élément de façon à ce
que cette partie reste bien triée

## Fusion sort
### Diviser pour régner

Le tri par fusion est un algorithme de tri par comparaison stable. Il
fonctionne de la manière suivante :
* L'algorithme se sépare en deux grandes étapes, la découpe puis la fusion :
    * La découpe consiste à découper le tableau en 2 de façon récursive
    jusqu'à ce qu'on arrive à des éléments seuls
    * La fusion consiste à rassembler les éléments puis les tableaux
    deux à deux en les triant lors de la fusion
    
## Quick sort


## Shell sort

Le tri de shell est une amélioration du tri par insertion, mais
en plus de cela, il exécute un tri par insertion sur tous les 
éléments dans un espacement défini afin de palier aux différents
points faibles du tri par insertion

