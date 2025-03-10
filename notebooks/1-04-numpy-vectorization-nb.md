---
jupytext:
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
  title: vectorisation
---

# vectorisation

+++ {"tags": ["framed_cell"]}

## contenu de ce notebook (sauter si déjà acquis)

la **vectorisation** (c'est-à-dire appliquer une fonction `numpy` à tout un tableau sans passer par un `for-python`)

les `ufunc`

`numpy.vectorize`

```{code-cell} ipython3
# on importe la librairie numpy
import numpy as np
from matplotlib import pyplot as plt
```

+++ {"tags": ["framed_cell"]}

## qu'est-ce que la vectorisation ?

`````{admonition} →

**l'idée**  
pour appliquer une fonction à tous les éléments d'un tableau `numpy`

* de ne **jamais** utiliser une boucle `for-python`  

* mais d'appliquer la fonction (ou l'opérateur)  
  **directement au tableau** - de manière *vectorisée*

* c'est plus concis à écrire, vos codes sont plus rapides, plus lisibles !
et pourront être optimisés en temps

````{admonition} la bonne façon 
:class: seealso

```python
n = 10000000
x = np.linspace(0, 2*np.pi, n)

y = np.sin(x)  # OUI c'est la bonne façon
```
````

````{admonition} la mauvaise façon
:class: danger

```python
n = 10000000
x = np.linspace(0, 2*np.pi, n)

y = []
for e in x:   # NON IL NE FAUT PAS FAIRE UN FOR !!`
    y.append(np.sin(e))
```
````

la vectorisation est **la seule manière** d'écrire du code en `numpy`  
pour avoir des **temps d'exécution acceptables**

**conclusion**  
sur des tableaux `numpy` utilisez **toujours** la **vectorisation**  
**vectorisation** = le `for` est fait dans `numpy`


vérifiez en comparant les temps d'exécution des deux codes `%%timeit`  
attention c'est très long...
`````

```{code-cell} ipython3
%%timeit
n = 1000000
x = np.linspace(0, 2*np.pi, n)

# la bonne façon
np.sin(x)         # np.sin appliquée au tableau x
```

```{code-cell} ipython3
# pour comparer les choses comparables
import math
```

```{code-cell} ipython3
%%timeit
n = 1000000
x = np.linspace(0, 2*np.pi, n)

# la mauvaise façon
for e in x:             # une boucle for sur un tableau numpy
                        # c'est toujours une mauvaise idée
    math.sin(e)
```

````{admonition} pourquoi math.sin et pas np.sin ?
:class: admonition-small

dans une première version de ce notebook, pour cette deuxième - et mauvaise - façon de faire on avait artificiellement forcé le trait car:

- on avait utilisé `np.sin` au lieu de `math.sin`; merci à Damien Corral qui a remarqué que `np.sin` appliqué à un scalaire Python ajoute une inefficacité !  
- et de plus on rangeait les résultats dans une liste, ce qui aggrave encore les écarts

après ces corrections, qui permettent de mieux isoler la perte d'efficacité, on observe toujours un rapport de 1 à 10 !
(et en plus on ne garde même pas les résultats du calcul)
````

+++

### dessiner un cercle de rayon `r`

+++

**exercice**

Dessinez un cercle de rayon `r`  

indices

1. $x = r\, sin(\theta)$  
   $y = r\, cos(\theta)$  
   avec $\theta$ variant de $0$ à $2\pi$
1. si votre cercle apparaît elliptique, c'est que les échelles de vos axes diffèrent  
   demandez à ce qu'elles soient égales avec `plt.axis('equal')`

```{code-cell} ipython3
# votre code
```

### calculer une fonction polynomiale

+++

**exercice**

1. faites une fonction qui retourne le calcul d'un polynome  
   par exemple $x^3 + 2x^2 -5x +1$  
   (puissance: `**` ou `np.power`)

2. appliquez la directement à un `np.ndarray` (sans faire de `for`)
   qu'obtenez-vous en retour ?

4. tracez la courbe de la fonction

```{code-cell} ipython3
:lines_to_next_cell: 1

# votre code ici
def scalar_function(x):
    pass
```

## les `ufunc`

+++ {"tags": ["framed_cell"]}

### qu'est-ce qu'une `ufunc`

````{admonition} →
Le mécanisme général qui applique une fonction à un tableau  
est connu sous le terme de *Universal function* - ou encore `ufunc`  

En conclusion, vous **devez** toujours utiliser les `ufunc` et plus jamais les `for-python`

* même si ça vous paraît plus difficile
* même si vous utilisiez des `for-python` en prépa
* par souci de la **performance en temps**, et de propreté de votre code, vous ne pouvez plus y échapper

Une habitude à prendre:

* c'est juste une autre manière de penser le code  
* vos codes seront compacts et lisibles (élégants)

```{admonition} utile pour les recherches
:class: tip

Souvenez-vous du terme `ufunc` car c'est utile pour des recherches sur Internet

````

+++

***

+++ {"tags": ["framed_cell"]}

### quelles sont les fonctions vectorisées ?

````{admonition} →
**les opérateurs arithmétiques classiques**  
et leur contre-partie `numpy` (*Ufuncs*)


| opérateur | `numpy` fonction    |
|----------:|-------------------|
|   `+`    | `np.add` |
|   `-`    | `np.substract`|
|   `*`    | `np.multiply` |
|   `/`    | `np.divide` |
|   `//`   | `np.floor_divide` |
|   `\%`   | `np.mod` |
|   `**`   | `np.power` |

**les fonctions de comparaison, trigonométriques...**

| fonction         | `numpy` fonction    |
|-----------------:|-------------------|
| comparaison      | `np.greater`, `np.less`, `np.equal`, ...|
|   valeur absolue | `np.absolute` or `np.abs` |
|   trigonometrie  | `np.sin`, `np.cos`, ... |
|   exponentielle  | `np.exp`, `np.exp2`, .. |
|   logarithme     | `np.log`, `np.log2`, `np.log10` |

vous allez les utiliser sans même vous en rendre compte !
````

+++

***

+++ {"tags": ["framed_cell"]}

### savoir si une fonction est une `ufunc`

````{admonition} →
 demandez-le lui

```python
np.add
<ufunc 'add'>
```

`numpy.add` en est !
````

```{code-cell} ipython3
# essayez !
np.power
```

## pour vectoriser une fonction

+++

**exercice**

````{admonition} consigne
:class: admonition-small

le but du jeu ici c'est de voir comment vectoriser une fonction **que vous écrivez vous**  
on s'interdit donc, dans cet exercice, d'utiliser des fonctions de `numpy`, ni la fonction *builtin* `abs` de Python

si vous préférez, vous pouvez choisir d'implémenter une fonction définie par morceaux  
genre $x**2$ sur les nombres négatifs et $x^3$ sur les positifs
````

1. écrivez une fonction qui calcule la valeur absolue d'un scalaire x  `absolute(x)`
2. testez votre fonction sur des scalaires
3. créez un `np.ndarray` de scalaires et appliquez-lui la fonction
4. que se passe-t-il ?

```{code-cell} ipython3
# votre code ici
```
