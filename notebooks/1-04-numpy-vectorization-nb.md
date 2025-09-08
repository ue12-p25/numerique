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
  pygments_lexer: ipython3
  nbconvert_exporter: python
---

# vectorisation

+++ {"tags": ["framed_cell"]}

## contenu de ce notebook (sauter si déjà acquis)

* la **vectorisation** (appliquer une fonction à tout un tableau sans passer par un `for-python`)
* les `ufunc`
* `numpy.vectorize`

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

* ne **jamais** utiliser une boucle `for-python`  
* mais appliquer la fonction (ou l'opérateur) **directement au tableau** - de manière *vectorisée*
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

après ces corrections, qui permettent de mieux isoler la perte d'efficacité, on observe toujours un rapport de performance important !
alors qu'on ne garde même pas les résultats du calcul...
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
|   `%`   | `np.mod` |
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

si vous préférez, vous pouvez choisir d'implémenter une fonction définie par morceaux  
genre $x^2$ sur les nombres négatifs et $x^3$ sur les positifs
````

1. écrivez une fonction qui calcule la valeur absolue d'un scalaire x `absolute(x)`  
   on s'interdit donc, dans cet exercice, d'utiliser des fonctions de `numpy`, ni la fonction *builtin* `abs` de Python
1. testez votre fonction sur des scalaires
1. créez un `np.ndarray` de scalaires et appliquez-lui la fonction
1. que se passe-t-il ?

```{code-cell} ipython3
# votre code ici
```

+++ {"tags": ["framed_cell"]}

### problème de la fonction `absolute`

`````{admonition} que se passe-t-il ?

supposons que votre code soit:

````python
def absolute (x):
    if x >= 0:
        return x
    return -x

tab = np.array([10, -30, 56.5])

absolute(tab)                   # --> BOOM
````

alors vous obtenez

````python
----> if x >= 0:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
````

car l'expression `x >= 0` appliquée à `tab` rend le tableau `array([False, True, False])`

mais le `if`, appliqué au tableau de booléens `[False, True, False]`, ne sait pas quoi faire !  
alors il propose des solutions

* `if` est-il vrai quand tous les éléments sont vrais ? `np.all(x)`
* `if` est-il vrai quand au moins un élément du tableau est vrai ? `np.any(x)`
`````

+++ {"tags": ["framed_cell"]}

### la solution

`````{admonition} mais vous ne voulez rien de tout cela !

* vous voulez que `numpy` applique le `if` à-chaque-élément
* i.e. que la fonction s'exécute de manière vectorisée

la **solution**:

* demander à  `numpy` de **vectoriser** la fonction avec `np.vectorize`
* il considérera l'argument comme un tableau
* sur lequel le code Python "normal" sera appelé de manière vectorisée

```python
@np.vectorize
def absolute (x):
    if x >= 0:
        return x
    return -x

absolute(tab)
-> array([10. , 30. , 56.5])
```

````{admonition} c'est quoi cette syntaxe ?
:class: admonition-small dropdown info

le `@np.vectorize` en première ligne, c'est ce qu'en Python on appelle **un décorateur**  
c'est comme si on avait fait ceci:

```python
def absolute(x):
    if x >= 0:
        return x
    return -x

# et le décorateur produit une fonction (vectorisée) 
# à partir de votre fonction "naive"

absolute = np.vectorize(absolute)
```
````
`````

```{code-cell} ipython3
:tags: [raises-exception]

# le code
@np.vectorize
def absolute (x):
    if x >= 0:
        return x
    return -x
```

```{code-cell} ipython3
:tags: [raises-exception]

# le code

tab = np.array([10, -30, 56.5])
absolute(tab)
```

```{code-cell} ipython3
:tags: [raises-exception]

# et d'ailleurs à titre anecdotique:
# elle fonctionne aussi sur une `list` `python`

absolute([-10, -20, 30])
```

**exercice**

1. la fonction `numpy.abs` est-elle une `ufunc` ?

2. la fonction `abs` de Python est-elle une `ufunc` ?

```{code-cell} ipython3
# votre code
```

## pour les avancés ou les rapides

+++

### résultats intermédiaires lors de calculs

````{admonition} →
nous appliquons des opérations vectorisées les unes à la suite des autres à des tableaux...

des **espaces mémoire intermédiaires** sont créés pour recevoir les résultats des calculs  
par exemple la fonction trigonométrique $4(e^{cos(x)})^2$

```python
def trigo (x):
    return 4*np.exp(np.cos(x))**2
```

de combien de tableaux intermédiaires avons-nous besoin dans ce calcul ?  
(un par calcul unitaire)

on développe le code pour montrer les tableaux intermédiaires

```python
def trigo_function_developpee (x):
    int_1 = np.cos(x)
    int_2 = np.exp(int_1)
    int_3 = np.power(int_2, 2)   # idem **
    return np.multiply(4, int_3) # idem *
```

ici trois tableaux intermédiaires créés inutilement (`3 * x.nbytes` octets)

le calcul vectoriel crée de nombreux tableaux intermédiaires  
qui peuvent coûter très **cher en mémoire**
````

+++

***

+++ {"tags": ["framed_cell"]}

### une solution aux tableaux intermédiaires

````{admonition} →
```python
def trigo (x):
    return 4*np.exp(np.cos(x))**2
```

code montrant les tableaux intermédiaires

```python
def trigo_function_developpee (x):
    int_1 = np.cos(x)
    int_2 = np.exp(int_1)
    int_3 = np.power(int_2, 2)
    return np.multiply(4, int_3)
```

la **solution** ?

* utiliser le paramètre optionnel `out=` des opérateurs `numpy`  
avec `out` on spécifie le tableau où ranger le résultat

```python
def trigo_function_developpee_out (x):
    result = np.cos(x)        # un pour le résultat
    np.exp(result, out=result)
    np.power(result, 2, out=result)
    np.multiply(4, result, out=result)
    return result
```

**mais** ce code est

* beaucoup plus compliqué à écrire que dans sa version compacte, simple et *directe*
* il sera donc plus propice à des erreurs
* il est franchement très difficile à lire !

**en conclusion** ne faites surtout pas cela systématiquement

* vous savez que ça existe
* vous y penserez le jour où la création de tableaux intermédiaires prendra une place bien trop importante
````

+++

le code ci-dessous

```{code-cell} ipython3
def trigo_function_compact (x):
    return 4*np.exp(np.cos(x))**2
```

```{code-cell} ipython3
plt.plot(trigo_function_compact(np.linspace(0, 2*np.pi, 1000)));
```

```{code-cell} ipython3
def trigo_function_developpee (x):
    int_1 = np.cos(x)
    int_2 = np.exp(int_1)
    int_3 = np.power(int_2, 2)
    result = 4*int_3
    return result
```

```{code-cell} ipython3
def trigo_function_developpee_out (x):
    result = np.cos(x)      # il m'en faut bien un pour le résultat !
    np.exp(result, out=result)
    np.power(result, 2, out=result)
    np.multiply(4, result, out=result)
    return result
```

```{code-cell} ipython3
plt.plot(trigo_function_developpee_out(np.linspace(0, 2*np.pi, 1000)));
```

### temps d'exécution de l'élévation d'un tableau au carré - avancé ou rapide

+++

**exercice**

1. créez un tableau `numpy` des 10000 premiers entiers avec `numpy.arange`

```{code-cell} ipython3
# votre code
```

2. calculez le temps d'exécution de l'élévation au carré des éléments  

    * a. avec un for-python
    * b. avec une compréhension Python
    * c. de manière vectorisée avec `**2`
    * d. de manière vectorisée avec `np.power`
    * e. de manière vectorisée avec `np.square`

```{code-cell} ipython3
# votre code
```

3. quelles sont les manières de faire les plus rapides ?

```{code-cell} ipython3
# votre code
```

4. utilisez `np.vectorize` pour décorer votre fonction 2.c; que constatez-vous ?

```{code-cell} ipython3
# votre code
```
