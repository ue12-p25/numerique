---
jupytext:
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: tests et masques sur tableaux
---

(label-numpy-mask)=

# tests et masques sur tableaux

```{code-cell} ipython3
import numpy as np
```

## contenu de ce notebook (sauter si déjà acquis)

tests sur les tableaux multi-dimensionnels `numpy` par fonctions vectorisées `ufunc`

masques/filtres booléens

composition des conditions  
opérateurs logiques *bit-à-bit* `&` `|`  `~`  
équivalent `numpy` `np.logical_and` `np.logical_or` `np.logical_not`  

obtenir une vue sur les éléments du tableau initial  
`numpy.argwhere`, `numpy.nonzero` et `numpy.putmask`

+++ {"tags": ["framed_cell"]}

## tests sur tableaux multi-dimensionnels

````{admonition} →
l'idée est de tester en une opération **tous les éléments** d'un tableau

**prenons un exemple**

générons aléatoirement un tableau d'entiers  
(ici entre `0` et `9`)

```python
tab = np.random.randint(10, size=(2, 3))
-> tab [[1 8 5]
        [7 0 2]]
```

testons la parité des éléments

```python
tab%2 == 0
```
ou encore - équivalent mais en appelant une fonction plutôt que l'opérateur `==`

```python
np.equal(tab%2, 0)
```

les résultats des comparaisons élément-par-élément  
sont rangés dans un tableau `np.ndarray`  
de même taille que le tableau initial

```python
tab%2 == 0
-> [[False,  True,  False],
    [False,  True,  True]]
```


**remarquez**

* dans l'expression `tab%2 == 0` et `np.equal(tab % 2, 0)`
* le broadcast de `0` en un tableau de `0` de la même taille que `tab`
````

```{code-cell} ipython3
# le code
tab = np.random.randint(10, size=(2, 3))
print(tab)
print(tab % 2 == 0)
print(np.equal(tab % 2, 0))
res = tab % 2 == 0
print(res.shape)
```

+++ {"tags": ["framed_cell"]}

## n'utilisez pas de for-python: utilisez les `ufunc`

````{admonition} →
les opérations de comparaison s'appliquent à tous les éléments d'un tableau en une seule fois  

* il ne faut **jamais** utiliser de **for-python**
* les fonctions sont vectorisées (les *UFuncs*)

```python
type(np.greater)
-> numpy.ufunc
```
````

```{code-cell} ipython3
:cell_style: split

# > est une ufunc

# on peut écrire indifféremment
tab > 5
```

```{code-cell} ipython3
:cell_style: split

# ou bien
np.greater(tab, 5)
```

+++ {"tags": ["framed_cell"]}

## combiner les résultats

````{admonition} →

**les résultats** peuvent être combinés

* en un résultat **global**
* en des **sous-tableaux** de résultats

un tableau
```python
tab = np.random.randint(10, size=(2, 3))
-> tab [[1 8 5]
        [7 0 2]]
```

regardons si il existe au moins une valeur paire dans le tableau des résultats

```python
res = np.equal(tab%2, 0)
np.any(res)
-> True
```


regardons si toutes les valeurs sont paires

```python
res = np.equal(tab%2, 0)
np.all(res)
-> False
```

comptons le nombre global de valeurs paires

```python
res = tab%2 == 0
print(np.sum(res))
-> 3
```

il existe une fonction dédiée  
(elle compte le nombre d'éléments non nuls)  
```python
np.count_nonzero(tab%2==0)
-> 3
```


comptons le nombre de valeurs paires dans l'axe des lignes du tableau

```python
res = tab %2 == 0
print(np.sum(res, axis=0)) # axe des lignes
-> [0, 2, 1]
```

avec la fonction dédiée  
(elle compte sur les axes)  
```python
np.count_nonzero(tab%2==0, axis=0)
-> [0, 2, 1]
```
````

```{code-cell} ipython3
# le code
tab = np.random.randint(10, size=(2, 3))
res = np.equal(tab%2, 0)
print(np.any(res))
print(np.all(res))
print(np.sum(res))
print(np.count_nonzero(tab%2==0))
print(np.sum(res, axis=0))
np.count_nonzero(tab%2==0, axis=0)
```

+++ {"tags": ["framed_cell"]}

## les masques/filtres booléens

`````{admonition} →
le tableau des résultats des tests est un **masque booléen**  

* il a la **même forme** que le tableau initial
* il va servir de **filtre** sur le tableau initial

il va permettre de sélectionner dans le tableau initial  
les éléments pour lesquels le test est vrai

générons un `numpy.ndarray` de forme `(2, 3, 4)` d'entiers entre -10 et 10

```python
tab = np.random.randint(-10, 10, size=(2, 3, 4))
```


* filtrons les entiers strictement positifs
```python
tab[tab > 0]
```

* ou encore
```python
tab[np.greater(tab, 0)]
```

on peut modifier tous les éléments filtrés d'un seul coup  
lors de l'application du filtre

```python
tab[tab > 0] = 0
tab # n'a plus que des éléments négatifs ou nuls
```

````{admonition} pour trouver les indices: np.argwhere()

un peu plus avancé, mais si vous avez besoin de construire **les indices** des éléments sélectionnés, pour les repérer dans le tableau original, utilisez `np.argwhere()`

par exemple pour trouver les indices des cases nulles dans le tableau (on vient de mettre tous les positifs à 0):
```python
# renvoie un tableau contenant les triplets d'indices
# qui correspondent aux éléments nuls dans tab

np.argwhere(tab == 0)
```
````
`````

```{code-cell} ipython3
# le code
tab = np.random.randint(-10, 10, size=(2, 3, 4))
tab
```

```{code-cell} ipython3
:scrolled: true

# le code
print(tab[np.greater(tab, 0)])
print(tab[tab > 0])
```

```{code-cell} ipython3
# le code
tab [tab > 0] = 0
tab
```

```{code-cell} ipython3
# le code
np.argwhere(tab==0)
```

+++ {"tags": ["framed_cell"]}

## composition des conditions

````{admonition} →
4 règles

* vous ne pouvez **pas** utiliser les opérateurs logiques Python `and`, `or`, `not`  
  (ils ne sont **pas** vectorisés)

* vous devez utiliser les opérateurs logiques *bit-à-bit* `&` `|`  `~`
* ou leur équivalent en fonction `numpy`  
  `np.logical_and` `np.logical_or` `np.logical_not`  
  (qui sont binaires)

* vous devez parenthéser les sous-termes de vos expressions

on crée un tableau d'entiers aléatoires entre 0 et 100

```python
tab = np.random.randint(100, size=(3, 4))
```


masque pour sélectionner les éléments entre 25 et 75

```python
(tab >= 25) & (tab < 75)
```


masque pour sélectionner les éléments non-pairs entre 25 et 75


```python
(tab >= 25) & (tab < 75) & ~(tab%2==0)
```

et donc en version `numpy`

```python
np.logical_and(tab >= 25, tab < 75)
```

```python
np.logical_and(tab >= 25, np.logical_and(tab < 75, np.logical_not(tab%2==0)))
```
````

```{code-cell} ipython3
# le code
tab = np.random.randint(100, size=(3, 4))
print(tab)
print((tab >= 25) & (tab < 75))
print((tab >= 25) & (tab < 75) & ~(tab%2==0))
```

```{code-cell} ipython3
# le code
print(np.logical_and(tab >= 25, tab < 75))
print(np.logical_and(tab >= 25, np.logical_and(tab < 75, np.logical_not(tab%2==0))))
```

```{code-cell} ipython3
:tags: [level_intermediate]

# ATTENTION
# en Python pur on a le droit d'écrire un test comme
# 25 <= tab < 75
# MAIS comme ça va implicitement faire un 'and'
# ça ne fonctionne pas avec les tableaux numpy
try:
    25 <= tab < 75
except Exception as exc:
    print("OOPS - ne marche pas avec numpy\n", exc)
```

## modifier les éléments dans tableau d'origine

+++ {"tags": ["framed_cell"]}

### affecter une sélection

````{admonition} →
avec une expression de *sélection* de cette forme `tab[mask]`  
on peut **aussi modifier** (ces emplacements dans) le tableau de départ  
en affectant directement une valeur  
remarquez que la sélection se trouve à gauche du signe `=`

```python
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab % 2 == 0] = 100
print(tab)
[[  1 100   3]
 [100   5 100]]
```
````

```{code-cell} ipython3
# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab % 2 == 0] = 100
print(tab)
```

+++ {"tags": ["framed_cell", "level_intermediate"]}

### c'est fragile (1)

````{admonition} →
par contre il faut être un peu prudent; certaines formes, pourtant voisines en apparence, ne vont pas fonctionner

**1er cas**

maladroitement, je range la sélection dans une variable  
la sélection ne se trouve plus à gauche du `=`  
dans cette forme l'affectation va en fait modifier un tableau temporaire  
bref, ça **ne fonctionne plus** !  


```python
tab = np.array([[1, 2, 3], [4, 5, 6]])
view = tab[tab%2==0]
view[...] = 100
print(tab)
-> ([[1, 2, 3], # et non [1, 100, 3],...
     [4, 5, 6]])
print(view)
-> [100 100 100]
```
````

```{code-cell} ipython3
:tags: [level_intermediate]

# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
view = tab[tab%2==0]
view[...] = 100
print(tab)
print(view)
```

+++ {"tags": ["framed_cell", "level_intermediate"]}

### c'est fragile (2)

````{admonition} →
**2ème cas**

imaginons que je ne veux modifier **que le premier** des éléments pair  
je vais essayer en *indexant* ma sélection  
mais ça **ne fonctionne pas** comme espéré  
ici encore l'effet de bord se perd dans la nature  
et le tableau original n'est pas modifié


```python
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab%2==0][0] = 100
print(tab)
-> ([[1, 2, 3], # et non [1, 100, 3],...
     [4, 5, 6]])
```
````

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [level_intermediate]

# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
tab[tab%2==0][0] = 100
print(tab)
```

+++ {"tags": ["framed_cell", "level_intermediate"]}

### repérer les éléments par leurs indices

````{admonition} →
dans ce genre de situation, pour modifier les éléments sélectionnés dans le tableau d'origine, on peut repèrer les éléments par leur indice dans le tableau d'origine

et pour calculer ces indices, deux fonctions:

* la fonction `numpy.nonzero`
* la fonction `numpy.argwhere` (avancé)
````

+++ {"tags": ["level_intermediate"]}

***

+++ {"tags": ["framed_cell", "level_intermediate"]}

### la fonction `numpy.nonzero`

````{admonition} →
`numpy.nonzero`

* renvoie un tuple de même dimension que le tableau d'origine
* dans chaque dimension, on a la liste des indices

exemple

```python
tab = np.array([[1, 2, 3], [4, 5, 6]])
np.nonzero(~(tab%2==0))
-> ([0, 0, 1], [0, 2, 1])
```

la première liste contient les indices des lignes  `[0, 0, 1]`

la seconde liste contient les indices des colonnes `[0, 2, 1]`


`tab[0, 0]` `tab[0, 2]` et `tab[1, 1]` sont les 3 éléments

```python
print(tab[0, 0], tab[0, 2], tab[1, 1])
-> 1, 3, 5
```

la **magie**: vous pouvez indicer le tableau d'origine avec ce tuple  
pour obtenir une vue sur le tableau d'origine


```python
tab[np.nonzero(~(tab%2==0))]
-> 1, 3, 5
```

et donc vous pouvez modifier les éléments du tableau original

```python
tab[np.nonzero(~(tab%2==0))] = 1000
tab
-> [[1000,    2, 1000],
    [   4, 1000,    6]]
```
````

```{code-cell} ipython3
:tags: [level_intermediate]

tab = np.array([[1, 2, 3], [4, 5, 6]])
print("non zero", np.nonzero(~(tab%2==0)))
print("elements", tab[0, 0], tab[0, 2], tab[1, 1])
print("filter", tab[np.nonzero(~(tab%2==0))])
tab[np.nonzero(~(tab%2==0))] = 0
print("edited tab", tab)
```

+++ {"tags": ["framed_cell", "level_intermediate"]}

###  la fonction `numpy.argwhere`

````{admonition} →
`numpy.argwhere`

* renvoie un tableau de dimension 2
* autant de lignes que d'éléments filtrés
* chaque ligne donne l'index d'un élément  
dans chacune des dimensions du tableau d'origine


exemple

```python
tab = np.array([[1, 2, 3], [4, 5, 6]])
np.argwhere(~(tab%2==0))
-> [[0, 0],
    [0, 2],
    [1, 1]]
```

la première ligne contient les indices du premier élément  `[0, 0]`

la seconde ligne contient les indices du second élément `[0, 2]`

la troisième ligne contient les indices du troisième élément `[1, 1]`

vous ne pouvez **pas**  indicer directement le tableau d'origine par ce tableau  
et non on ne fait pas de `for-python`


on remarque

* que les résultats de `numpy.nonzero` et  `numpy.argwhere` sont très proches
* à une transposée et un type `tuple` près

```python
cond = ~(tab%2==0)
np.nonzero(cond)            # ([0, 0, 1], [0, 2, 1])
np.argwhere(cond)           # [[0 0] [0 2] [1 1]]
np.argwhere(cond).T         # [[0 0 1] [0 2 1]]
tuple(np.argwhere(cond).T)  # ([0, 0, 1], [0, 2, 1])
tab[tuple(np.argwhere(cond).T)]
-> array([1, 3, 5])
```
````

```{code-cell} ipython3
:tags: [level_intermediate]

# le code
tab = np.array([[1, 2, 3], [4, 5, 6]])
cond = ~(tab%2==0)
print(np.argwhere(cond).T)
print(np.nonzero(cond))
print(tuple(np.argwhere(cond).T))
tab[tuple(np.argwhere(cond).T)]
```

+++ {"tags": ["framed_cell", "level_advanced"]}

### modifier avec `array.putmask()`

````{admonition} →
**avancés**

la fonction `numpy.putmask(tab, cond, value)` remplace dans un `numpy.ndarray`  
les éléments obéissant à une condition, par une valeur donnée en argument

la modification est effectuée dans le tableau (en place)

```python
tab = np.arange(12).reshape(3, 4)
np.putmask(tab, tab%2==1, 0)
tab -> ([[ 0,  0,  2,  0],
        [ 4,  0,  6,  0],
        [ 8,  0, 10,  0]])
```
````

```{code-cell} ipython3
:tags: [level_advanced]

# le code
tab = np.arange(12).reshape(3, 4)
np.putmask(tab, tab%2==1, 0)
tab
```
