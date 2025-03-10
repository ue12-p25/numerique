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
  title: "fonctions d'agr\xE9gation"
---

# fonctions d'agrégation

```{code-cell} ipython3
import numpy as np
```

## contenu de ce notebook (sauter si déjà acquis)

ce notebook détaille les fonctions `numpy` qui combinent les éléments d'un tableau  
comme `numpy.sum`, `numpy.var`...

comment on utilise leur paramètre `axis`

+++ {"tags": ["framed_cell"]}

## introduction

````{admonition} →
nous avons vu des opérations `numpy` qui s'appliquent à un ou plusieurs tableaux  
et retournent un tableau de la même dimension

```python
tab1 = np.arange(10).reshape(2, 5)
np.power(tab1, 2) + tab1
-> array([[ 0,  2,  6, 12, 20],
          [30, 42, 56, 72, 90]])
```

les fonctions d'agrégation vont permettre de combiner les valeurs d'un même tableau  
et de retourner des sous-tableaux

* somme des lignes
* max d'une matrice
* ...

vous devrez spécifier la dimension `axis` dans laquelle vous désirez appliquer l'opération

exemples de fonctions d'agrégation

| fonction | comportement|
|---------:|-----|
| `np.sum` | somme les éléments sur un axe|
| `np.min` | retourne le plus petit élément|
| `np.max` | retourne le plus grand|
| `np.argmin` | retourne l'indice du plus petit élément|
| `np.argmax` | retourne l'indice du plus grand élément|
| `np.mean`| calcule la moyenne des éléments|
| `np.std`  | calcule l'écart type des éléments |
| `np.var`  | calcule la variance des éléments |
| `np.all`  | vrai si aucun élément n'est nul |
| `np.any`  | vrai si au moins un élément n'est pas nul |
| `np.where`  | une condition ternaire |
| .../...| .../... |

```{admonition} aussi comme une méthode
souvent ces fonctions sont aussi une méthode des `numpy.ndarray`  
c'est-à-dire que `np.sum(myarray)` est équivalent à `myarray.sum()`
```
````

```{code-cell} ipython3
# le code
tab1 = np.arange(10).reshape(2, 5)

np.mean(tab1)
```

```{code-cell} ipython3
tab1.mean()
```

## agrégation en dimension 1

+++ {"tags": ["framed_cell"]}

### exemple avec des vecteurs d'entiers

````{admonition} →
il n'y a qu'une dimension, qu'un `axe`  
c'est l'axe d'indice `0`  
il est donc optionnel

il suffit d'appliquer la fonction d'agrégation désirée au tableau  
elle s'applique à tous les éléments

fonction globale de `numpy`

```python
vec = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
np.min(vec, axis=0) # l'axis est optionnel
np.min(vec)
np.max(vec) # 9
np.sum(vec) # 45
np.std(vec) # 2.87
```

méthode de `numpy.ndarray`

```python
vec = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
vec.min() # 0
vec.max() # 9
vec.sum() # 45
vec.std()  # 2.87
```

le type de la valeur retournée, en général `int64` ou`float64`  
peut ne pas coincider avec le type des éléments du tableau  


là oui
```python
vec = np.array([0., 1]) # 0.
type(np.sum(vec))
-> numpy.float64
```

là non
```python
vec = np.array([0, 1], dtype=np.int8)
type(np.sum(vec))
-> numpy.int64
```


là oui
```python
vec = np.array([0, 1], dtype=np.int8)
type(np.min(vec))
-> numpy.int8
```
````

```{code-cell} ipython3
# le code
vec = np.random.randint(1, 10, size=(10,))
print(vec)
print(np.min(vec, axis=0), np.max(vec), np.sum(vec), np.std(vec))
print(vec.min(), vec.max(), vec.sum(), vec.std())
```

```{code-cell} ipython3
# le code
vec = np.array([0, 1], dtype=np.int8)
type(np.min(vec))
```

+++ {"tags": ["framed_cell"]}

### exemple avec un vecteur de booléens

````{admonition} →
Comment tester si tous les éléments de votre tableau sont vrais ?  
Comment tester si l'un au moins des éléments de votre tableau est vrai ?

**version pédestre** ... on fait la somme  
(`True` devient `1` et `False` `0`)

* si le résultat est la longueur du tableau... ils sont tous vrais
* si le résultat est 0... ils sont tous faux

**version `numpy`** avec les fonction `np.all` et `np.any`  
soit fonction globale soit méthode de `numpy.ndarray`

pour générer des booléens, générer aléatoirement des entiers entre `0` et `2` non-compris  
et demander un `dtype` `bool` (le type `np.bool` existe mais il est *deprecated*)

```python
tab = np.random.randint(0, 2, size=(10), dtype=bool)
```

```python
np.all(tab)
np.any(tab)
tab.all()
tab.any()
tab.sum() == len(tab) # all
tab.sum() != 0 # any
```

`np.all`  et `np.any` s'appliquent sur des valeurs de types autres que booléen  
les zéros des types seront `False` et le reste `True`
````

```{code-cell} ipython3
# le code
tab = np.random.randint(0, 2, size=(10), dtype=bool)
print(np.all(tab), np.any(tab))
print(tab.all(), tab.any())
print(tab.sum() == len(tab), tab.sum() != 0)
print(np.all(np.random.randint(1, 2, size=(10), dtype=bool))) # tous des 1
```

**exercice : programmer la version "pédestre"**

1. créez une fonction manuelle (sans utiliser `np.all`  et `np.any`) qui prend un tableau numpy de booléens en paramètre et détermine si tous les éléments du tableau sont vrais.

2. créez une fonction manuelle (sans utiliser `np.all`  et `np.any`) qui prend un tableau numpy de booléens en paramètre et détermine si tous les éléments du tableau sont faux.

```{code-cell} ipython3
# votre code
def fake_all(tab):
    pass
def fake_none(tab):
    pass
```

## agrégation en dimension > 1

+++ {"tags": ["framed_cell"]}

### exemple de tableau en dim 4

````{admonition} →
```python
tab = np.arange(120).reshape(2, 3, 4, 5)
tab ->[[[[  0,   1,   2,   3,   4],
         [  5,   6,   7,   8,   9],
         [ 10,  11,  12,  13,  14],
         [ 15,  16,  17,  18,  19]],

        [[ 20,  21,  22,  23,  24],
         [ 25,  26,  27,  28,  29],
         [ 30,  31,  32,  33,  34],
         [ 35,  36,  37,  38,  39]],

        [[ 40,  41,  42,  43,  44],
         [ 45,  46,  47,  48,  49],
         [ 50,  51,  52,  53,  54],
         [ 55,  56,  57,  58,  59]]],


       [[[ 60,  61,  62,  63,  64],
         [ 65,  66,  67,  68,  69],
         [ 70,  71,  72,  73,  74],
         [ 75,  76,  77,  78,  79]],

        [[ 80,  81,  82,  83,  84],
         [ 85,  86,  87,  88,  89],
         [ 90,  91,  92,  93,  94],
         [ 95,  96,  97,  98,  99]],

        [[100, 101, 102, 103, 104],
         [105, 106, 107, 108, 109],
         [110, 111, 112, 113, 114],
         [115, 116, 117, 118, 119]]]]
```
````

+++

***

+++ {"tags": ["framed_cell"]}

### somme en dimension 4

````{admonition} →
par défaut `numpy` appliquera l'opération sur tous les éléments du tableau  
et renverra une unique valeur

```python
tab = np.arange(120).reshape(2, 3, 4, 5)
tab.sum()
-> 7140
```

on peut préciser un axe avec `axis=i`

* quand on va appliquer une opération suivant un axe  
cette dimension va disparaître dans le résultat  

on considère `tab` formé de 2 groupes de 3 matrices de 4 lignes et 5 colonnes  
donc de forme `(2, 3, 4, 5)`

**sommons dans l'axe des groupes**

```python
tab.sum(axis=0).shape # on rend la forme obtenue
-> (3, 4, 5)
```

**sommons suivant l'axe des matrices**

```python
tab.sum(axis=1).shape
-> (2, 4, 5)
```

**sommons suivant l'axe des lignes**

```python
tab.sum(axis=2).shape
-> (2, 3, 5)
```

**sommons suivant l'axe des colonnes**

```python
tab.sum(axis=3).shape
-> (2, 3, 4)
```
````

```{code-cell} ipython3
tab = np.arange(120).reshape(2, 3, 4, 5)

(tab.sum(axis=0).shape == (3, 4, 5),
 tab.sum(axis=1).shape == (2, 4, 5),
 tab.sum(axis=2).shape == (2, 3, 5),
 tab.sum(axis=3).shape == (2, 3, 4))
```

```{code-cell} ipython3
:lines_to_next_cell: 0

tab.sum(axis=0)
```

+++ {"tags": ["level_advanced"]}

pour les usages (trés) avancés, remarquons qu'on pourrait même passer comme `axis` *plusieurs* dimensions

par exemple

```python
tab.sum(axis=(1, 2))
```

on généralise simplement: au lieu de faire la somme le long d'une droite, ici on va faire la somme sur un plan

et de la même façon qu'en faisant `sum(axis=0)` on était passé
d'une entrée de *shape* (2, 3, 4, 5) à une sortie de *shape* (3, 4, 5)

eh bien la shape de `tab.sum(axis=(1, 2))` va être (2, 5); les deux dimensions centrales, puisqu'on les a 'consommées' pour faire la somme, ont disparu du résultat

```{code-cell} ipython3
:tags: [level_advanced]

# le code
tab.sum(axis=(1, 2))
```

+++ {"tags": ["framed_cell"]}

### min et max globaux en dimension 4

````{admonition} →
on recherche l'indice (l'emplacement, pas la valeur) du plus grand élément du tableau

c'est la méthode `argmax` qu'il nous faut

```python
tab = np.arange(120).reshape(2, 3, 4, 5)
tab.argmax()
-> 119
```

**attention**  
il nous donne l'indice dans le tableau *aplati*

la fonction `numpy.unravel_index`  
re-calcule les coordonnées  
à partir de l'indice absolu et de la forme du tableau  


```python
tab = np.arange(120).reshape(2, 3, 4, 5)
tab.argmax() # 119
np.unravel_index(tab.argmax(), tab.shape) # (1, 2, 3, 4)
```
````

```{code-cell} ipython3
:lines_to_next_cell: 1

# le code
tab = np.arange(120).reshape(2, 3, 4, 5)
print(    tab.argmax()    )

print(    np.unravel_index(tab.argmax(), tab.shape)    )
```

+++ {"tags": ["level_advanced"]}

**exercice avancé**
1. proposez le code de la fonction `np.unravel_index`

```{code-cell} ipython3
:tags: [level_advanced]

# votre code ici
def unravel_index(index, shape):
    pass
```

```{code-cell} ipython3
:tags: [level_advanced]

# devrait retourner [1, 2, 0, 4]
unravel_index(104, (2, 3, 4, 5))
```
