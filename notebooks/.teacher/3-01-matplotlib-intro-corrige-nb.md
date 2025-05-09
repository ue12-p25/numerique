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
  title: "Python-num\xE9rique - visualisation des donn\xE9es"
---

# Python-numérique - visualisation des données

+++ {"tags": ["framed_cell"]}

## introduction

````{admonition} →
<https://matplotlib.org/api/pyplot_summary.html>

pour se familiariser avec des données, rien ne remplace - quand elle est possible - la **visualisation**

nous allons voir quelques fonctionnalités de la librairie `matplotlib.pyplot`  
ou `plt` par convention

pourquoi `matplotlib` ?  
parcequ'en en 2003, des développeurs veulent une alternative à la visu sous *matlab* pour l'écosystème Python

elle est devenue **la** librairie la plus populaire pour le dataviz en Python avec

* une communauté de développeurs/utilisateurs très active
* les autres librairies sont, le plus souvent, dérivées de `matplotlib`

la syntaxe se veut simple  
la librairie est très complète et très optimisée  
elle peut traiter de grandes quantités de données

les fonctions ont été *empaquetées* afin d'être utilisées facilement en `pandas`

vous allez y trouver toutes les fonctions classiques:

* courbes, histogrammes, box-plots, nuages de points, plot3D, grilles de figures ...
* que vous allez pouvoir les personnaliser avec des textes, titres, étiquettes, légendes ...
* dont vous allez pouvoir contrôler les couleurs, styles de ligne, propriétés de police ...
````

```{code-cell} ipython3
from matplotlib import pyplot as plt

# pour l'instant on va utiliser le mode par défaut
#%matplotlib inline

# pour changer la taille par défaut
plt.rcParams['figure.figsize'] = (4, 2)

import numpy as np
import pandas as pd
```

+++ {"tags": ["framed_cell"]}

## plusieurs *drivers*

````{admonition} →
dans ce premier notebook nous allons utiliser le driver `inline` - qui est le défaut

en fait il en existe plusieurs autres, et notamment pour les notebooks le driver notebook` - qui s'utilise en faisant

```python
%matplotlib notebook
```

et pour bien voir les différences je vous invite à consulter les deux notebooks suivants

* `4-01-matplotlib-z1-notebook.py`
* `4-01-matplotlib-z2-notebook.py`

à retenir principalement, c'est que si on voulait être complètement propre,
on ferait pour chaque figure

  * un appel à `plt.figure()` au début
  * un appel à `plt.show()` à la fin

toutefois c'est trop de *boilerplate*, surtout quand il s'agit simplement de plotter une fonction !

du coup il est fréquent qu'on élude tout ce qui est possible,
et là ça devient potentiellement confusant, car

* en mode `inline`, ce n'est pas nécessaire de créer les figures avec `plt.figure()`
  mais il faut utiliser `plt.show()` si on veut afficher plusieurs figures dans la même cellule

* mais en mode `notebook` c'est un peu le contraire,
  on est incité/obligé d'utiliser `plt.figure()` à chaque fois, et pas vraiment besoin de `plt.show()`

enfin, vous noterez que `df.plot()` fait un appel à `plt.figure()` ! bref c'est un peu le bazar...

````

+++ {"tags": ["framed_cell"]}

## tracer une courbe avec `plt.plot`

````{admonition} →
avec `matplotlib.pyplot.plot`  
(ou `plt.plot` puisqu'elle importée sous ce nom)

pour les abcisses, 50 nombres réels entre 0 et $2\pi$  
linéairement espacés

```python
x = np.linspace(0, 2*np.pi, 50)
```

pour les ordonnées, les sinus de ces points  
vous remarquez l'application de la fonction vectorisée `numpy.sin` au `numpy.ndarray`

```python
y = np.sin(x)
```

la fonction `plot` trace les 50 couples de points `(abscisse, ordonnée)`
et relie les points entre eux

```python
plt.plot(x, y)
```
```{image} media/sinus.png
:width: 300px
```

de nombreux *réglages* ont pris leurs valeurs par défaut  
(taille de la figure, tailles et polices des caractères, couleurs du fond et de la courbe...)

par exemple

* pour voir les points en plus des segments les reliant  
utilisez le paramètre `marker`
`'o'` ou `'^'` etc.

```python
plt.plot(x, y, marker='s')
```

*  pour modifier l'épaisseur du trait  
utilisez le paramètre `linewidth`

```python
plt.plot(x, y, linewidth=5)
```

* pour changer la couleur du trait  
utilisez le paramètre `color`

```python
plt.plot(x, y, color='red')
```

* pour changer le style du trait  
utilisez le paramètre `linestyle`  
`dotted`, `dashed`...

```python
plt.plot(x, y, linestyle='dashed')
```

une chaîne de caractères formattée permet de donner plus facilement ces paramètres:  

```python
plt.plot(x, y, 'r-') # ligne rouge continue
plt.show()
plt.plot(x, y, 'b.') # ligne bleue pointillée
plt.plot(x, y, 'g--') # ligne verte en traits
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y); # le ; est là afin que la dernière expression du notebook (celle qui est affichée) soit None
```

```{code-cell} ipython3
#le code
plt.plot(x, y, marker='s');
```

```{code-cell} ipython3
# le code
plt.plot(x, y, linewidth=5, color='red', linestyle='dotted');
```

```{code-cell} ipython3
:lines_to_next_cell: 2
:scrolled: true

plt.plot(x, y, 'r-') # ligne rouge continue
plt.show()
plt.plot(x, y, 'b.') # ligne bleue pointillée
plt.show()
plt.plot(x, y, 'g--'); # ligne verte pointillée
```

+++ {"tags": ["framed_cell"]}

## attention aux valeurs manquantes

````{admonition} →
on peut ne donner que deux points  
`plt.plot` les relie  
comme ici (10, 10) à (20, 20)

```python
plt.plot([10, 20], [10, 20])
```

```{image} media/plot-deux-points.png
:width: 300px
```

mais attention si on ne donne qu'un point  
`plt.plot` ne sait plus tracer de segment !

```python
plt.plot([10], [10])
-> figure toute vide
```

il en est de même si des points sont manquants

**exercice**

créez une liste de points en alternant entiers et `np.nan`  
par exemple
```python
l = [10, np.nan, 20, 30, np.nan, 40, np.nan]
```
affichez la en abscisse et en ordonnée  
que constatez-vous ?

`plt.plot` doit avoir des points à relier...  pour qu'on voit les segments

naturellement si vous utilisez le paramètre `marker`  
les points sont alors affichés  

**exercice**

affichez un `marker` de points  
(par exemple `'v'`),  
dans le `plt.plot` de l'exercice ci-dessus (avec les `np.nan`)
````

```{code-cell} ipython3
# le code
plt.plot([10, 20], [10, 20]);
```

```{code-cell} ipython3
# le code
plt.plot([10], [10]);
```

```{code-cell} ipython3
# prune-cell
l = [10, np.nan, 20, 30, np.nan, 40, np.nan]
plt.plot(l, l);
```

```{code-cell} ipython3
# prune-cell
l = [10, np.nan, 20, 30, np.nan, 40, np.nan]
plt.plot(l, l, marker='v');
```

+++ {"tags": ["framed_cell"]}

## ajouter un titre `plt.title`

````{admonition} →
avec la fonction `plt.title` on ajoute un titre à la figure

avec son paramètre `fontsize` on fixe la taille des caractères

avec son paramètre `loc` et ses valeurs `'center'`, `'left'` et `'right'`  
on positionne le titre


```python
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y)
plt.title('sinus(X)', fontsize=20, loc='left')
```

vous remarquez que `matplotlib` a la notion de **figure courante**  
i.e. celle sur laquelle s'appliquent les fonctions  
ici `plt.title` et `plt.plot` s'appliquent sur la même figure

pensez à utiliser le help

```python
plt.title?
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

plt.plot(x, y)
plt.title('sinus(X)', fontsize=20, loc='left');
```

+++ {"tags": ["framed_cell"]}

## donner une taille à une figure

````{admonition} →
la fonction `plt.figure` permet

* de créer une nouvelle figure ou d'en activer une existante
* et aussi de passer différents paramètres à la figure courante  
dont sa **taille**

```python
x = np.linspace(0, 2*np.pi, 50)
plt.figure(figsize=(10, 2)) # 10 pour les abscisses et 2 pour les ordonnées
plt.plot(x, np.sin(x))
```

```python
plt.figure?
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)
plt.figure(figsize=(10, 2)) # 10 pour les abscisses et 2 pour les ordonnées
plt.plot(x, np.sin(x));
```

```{code-cell} ipython3
#plt.figure?
```

+++ {"tags": ["framed_cell"]}

## ajouter des labels aux axes  `plt.xlabel` et `plt.ylabel`

````{admonition} →
avec la fonction `plt.xlabel` on ajoute un label aux abscisses de la figure

avec la fonction `plt.ylabel` on ajoute un label aux ordonnées de la figure

```python
plt.xlabel('X')
plt.xlabel('Y');
```

naturellement les paramètre `fontsize`, `loc`... s'appliquent  
et pour voir tous les paramètres

```python
plt.xlabel?
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X')
plt.xlabel('Y');
```

```{code-cell} ipython3
#le code
#plt.xlabel?
```

+++ {"tags": ["framed_cell"]}

## nuages de points (`plt.scatter`)

````{admonition} →
`plt.scatter` permet d'afficher des points dispersés  
(i.e. non reliés)

```python
x = np.linspace(0, 2*np.pi, 50)
z = np.cos(x)
plt.scatter(x, z)
```

help pour plus d'information sur tous les paramètres

```python
plt.scatter?
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)
z = np.cos(x)
plt.scatter(x, z);
```

+++ {"tags": ["framed_cell"]}

## donner une légende à plusieurs plots sur la même figure `label`

````{admonition} →
vous pouvez tracer plusieurs courbes sur la même figure

avec le paramètre `label`, vous indiquez le nom de chaque figure

avec la fonction `plt.legend` vous affichez la légende  
constituée des étiquettes  
le paramètre `loc` permet de positionner la légende `'upper right'`, `'best'`, `'center'`...

**note** le même effet est obtenu lorsqu'on plotte directement une dataframe plutôt que des tableaux `numpy` - on y reviendra
````

```{code-cell} ipython3
x = np.linspace(0, 2*np.pi, 50)
plt.scatter(x, np.sin(x), label='sinus')
plt.scatter(x, np.cos(x), label='cosinus')
plt.legend();
```

+++ {"tags": ["framed_cell"]}

## fixer la limite des axes (`plt.xlim` et `plt.ylim`)

````{admonition} →
avec `x = np.linspace(0, 2*np.pi, 50)`  
`y=sin(x)` est calculé entre $0$ et $2\pi$

quand on demande `plt.plot(x, y)`  
par défaut tous les couples de points $(x_i, y_i)$ sont tracés

on peut n'affiche qu'une partie des points

par exemple ici entre $0$ et $\pi$ en abscisse  
et `0` et `1` en ordonnées
```python
plt.xlim(0, np.pi)
plt.ylim(0,1)
plt.plot(x, np.sin(x))
```
````

```{code-cell} ipython3
# le code
plt.xlim(0, np.pi)
plt.ylim(0,1)
plt.plot(x, np.sin(x))
```

+++ {"tags": ["framed_cell"]}

## préciser les *ticks* des axes (`plt.xticks` et `plt.yticks`)

````{admonition} →
avec `plt.xtick` et `plt.ytick` on peut donner des listes de valeurs à afficher sur les axes  
ici les abscisses et les ordonnées

```python
x = np.linspace(0, 2*np.pi, 50)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])  
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.plot(x, np.sin(x))
```

les valeurs seront espacées régulièrement sur les axes

il est possible de donner des noms aux ticks indiqués  
et même d'utiliser `latex`
```python
x = np.linspace(0, 2*np.pi, 50)

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [0, 'pi/2', 'pi', '3pi/2', '2pi'])

plt.plot(x, np.sin(x), label='sinus');
```

il est possible d'utiliser des formules `latex`  
en markdown entre deux `$` :

```python
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [0, '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])

plt.title("$sin(x)$ entre $0$ et $2\pi$ ")
plt.plot(x, np.sin(x))
```
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.plot(x, np.sin(x));
```

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 50)

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [0, 'pi/2', 'pi', '3pi/2', '2pi'])

plt.plot(x, np.sin(x));
```

```{code-cell} ipython3
# le code
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           [0, '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])

plt.title("$sin(x)$ entre $0$ et $2\pi$ ")
plt.plot(x, np.sin(x));
```

```{code-cell} ipython3
x = np.linspace(0, 2*np.pi, 50)
plt.figure(figsize=(10, 2))
plt.plot(x, np.sin(x))
```

+++ {"tags": ["level_basic", "framed_cell"]}

## **exercice** de plot

````{admonition} →
**exercice**

en une seule figure:

1. construisez un tableau de `nb` valeurs entre `x_min` et `x_max` (non compris)  
par exemple `x_min` à 0 et `x_max` à 10 et `nb` à 50
1. afficher la courbe $x^3$ avec un label en latex genre $x^3$
1. afficher la courbe $3*x^2+1$ avec un label en latex  
1. afficher la légende de la courbe au centre
1. affichez un titre au plot à droite
1. affichez uniquement les deux valeurs extrêmes en abscisse et en ordonnée
1. indice `np.linspace` et `np.power`

on utilise ici le driver `matplotlib` pour s'entrainer un peu
````

```{code-cell} ipython3
%matplotlib notebook
```

```{code-cell} ipython3
# votre code ici
```

```{code-cell} ipython3
# prune-cell

plt.figure(figsize=(5, 3))
x_min, x_max, nb = 0, 10, 50
x = np.linspace(x_min, x_max, nb)
y = np.power(x, 3)
z = 3*np.power(x, 2)+1
plt.plot(x, y, label='$x^3$')
plt.plot(x, z, label='$3 x^2 + 1$')
plt.xticks([x_min, x_max])
plt.yticks([min(y.min(), z.min()), max(y.max(), z.max())])
plt.title('deux courbes', loc='right')
plt.legend(loc='center');
```

+++ {"tags": ["framed_cell"]}

## **exercice** sauver une figure dans un fichier

````{admonition} →
**exercice**

1. faites une figure quelconque  
par exemple $f(x) = x^2$ entre $-10$ et $10$
1. mettez lui un titre, des labels aux abscisses et aux ordonnées, une légende, des couleurs...
1. en utilisant `plt.savefig`  sauver la figure  dans un fichier  
dans un format au choix (*jpg*, *pdf*, *png*, *svg*...)
1. pour voir les résultats pour `jpg`, `png`, `svg`  
   mettez dans une cellule markdown de votre notebook `![](foo.ext)`  
   en remplaçant naturellement `foo.ext` par le bon nom de fichier
1. pour voir le pdf mettez dans une cellule markdown `[ma belle figure](foo.pdf)` et cliquez dessus...
````

```{code-cell} ipython3
# prune-cell

plt.figure(figsize=(4, 4))
x = np.linspace(-10, 10, 50)
y = np.power(x, 2)

plt.title('$f(x) = x^2$', fontsize=20)

plt.xlabel('x', fontsize=15)
plt.ylabel('$x^2$', fontsize=15)

plt.plot(x, y, label='$x^2$')

plt.legend(fontsize=12)

plt.savefig('foo.svg')
plt.savefig('foo.pdf')
```

prune-cell

```{image} foo.svg
```

+++

prune-cell

[ma belle figure](foo.pdf)

+++

***
