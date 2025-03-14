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
  title: grilles de figures
---

# grilles de figures

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
```

+++ {"tags": ["framed_cell"]}

## figures et sous-figures

````{admonition} →
nous allons construire des figures contenant plusieurs graphiques  
en positionnant les graphiques sur une grille

une terminologie `matplotlib` un peu particulière

* `fig` et `figure` désignent la figure globale
* `axis` désigne les sous-figures (et non les axes des figures)

`matplotlib` a aussi la notion de figure courante  
i.e. celle à laquelle les graphiques sont rattachés

on a vu qu'on peut dessiner plusieurs courbes sur la même figure dans le même repère  

```python
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
```

on a vu que `plt.show` permettait de terminer/clore la figure courante  
et ainsi pouvoir créer une nouvelle figure

```python
plt.figure(figsize=(4, 2))
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x))
plt.show()
plt.plot(x, np.cos(x))
```

remarquez que `plt.figure(figsize=(4, 2))` ne s'applique qu'à la première figure  
la seconde est une nouvelle figure (qui prend les paramètres de taille par défaut)

si vous utilisez `matplotlib` dans un programme `python` et non dans un notebook  
vous devrez appeler `plt.show()` pour que votre figure s'affiche
````

```{code-cell} ipython3
# le code
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));
```

```{code-cell} ipython3
# le code
plt.figure(figsize=(4, 2))
x = np.linspace(0, 2*np.pi, 500)
plt.plot(x, np.sin(x))
plt.show()
plt.plot(x, np.cos(x));
```

+++ {"tags": ["framed_cell"]}

## par vecteur de sous-figures (`plt.subplots`)

````{admonition} →
pour créer une figure, contenant plusieurs graphiques différents  
il faut positionner ces **sous-figures** dans la figure courante

ls notion de sous-figure correspond à un repère  
(d'où la terminologie `axis` dans le code qui peut perturber les débutants)

la fonction `plt.subplots(n, m)`

* crée une grille virtuelle de `n` lignes et `m` colonnes à l'intérieur de la figure courante  
* elle renvoie la figure courante et un tableau `numpy` de sous-figures
* où vous positionnez vos sous-figures
* remarquez le **s** dans `subplots`

par convention la figure courante s'appelle `fig`  
et le tableau `numpy` pour la grille s'appelle `axes`

```python
fig, axes = plt.subplots(2, 3) # une grille de 2 lignes et 3 colonnes
axes.shape
```

ensuite vous positionnez des sous-figures dans la figure

```python
x = np.linspace(0, 2*np.pi, 50)
axes[0, 0].plot(x, np.sin(x))
axes[-1, -1].plot(x, np.cos(x))
```
````

```{code-cell} ipython3
# le code
fig, axes = plt.subplots(2, 3)
axes.shape

x = np.linspace(0, 2*np.pi, 50)
axes[0, 0].plot(x, np.sin(x))
axes[-1, -1].plot(x, np.cos(x));
```

+++ {"cell_style": "center", "tags": ["framed_cell"]}

## par tailles/positions dans une grille (`plt.subplot`)

````{admonition} →
la fonction `plt.subplot` rajoute une sous-figure à la figure courante

on indique 3 entiers `n`, `m` et `i` à la fonction `plt.subplot`

* soit en les séparant par des ',' soit en les donnant sous la forme d'un entier des 3 digit `nmi`
* `n` et `m` donnent la manière de considérer la grille

`plt.subplot(n, m, i)` ou `plt.subplot(nmi)`

* la sous-figure prendra la position `i`  
    1 est la figure en haut à gauche, 2 la suivante...

on ajoute dexs sous-figures à une grille `1` `2`

```python
ax1 = plt.subplot(121) # grille 1 ligne, 2 colonnes
                       # création de la première sous-figure

ax1.plot(x, np.sin(x)) # affichage de la courbe sinus

ax2 = plt.subplot(122) # grille 1 ligne, 2 colonnes
                       # création de la deuxième sous-figure

ax2.plot(x, np.cos(x)) # affichage de la courbe cosinus
```
````

```{code-cell} ipython3
ax1 = plt.subplot(121) # grille 1 ligne, 2 colonnes
                       # création de la première sous-figure

ax1.plot(x, np.sin(x)) # affichage de la courbe sinus

ax2 = plt.subplot(122) # grille 1 ligne, 2 colonnes
                       # création de la deuxième sous-figure

ax2.plot(x, np.cos(x)) # affichage de la courbe cosinus
;
```

+++ {"cell_style": "center", "tags": ["framed_cell"]}

## sous-figure sur plusieurs lignes/colonnes

````{admonition} →
les sous-figures peuvent occuper plusieurs lignes et/ou plusieurs colonnes

l'index est remplacé par un couple `(j, k)`  
où `j` et `k` sont le premier et le dernier index  
sur lesquels la sous-figure s'étend

```python
ax1 = plt.subplot(2, 3, 1) # la première case
ax1.plot(x, y, 'b') # bleu

ax2 = plt.subplot(2, 3, 2) # la seconde case
ax2.plot(x, y, 'r') # rouge

ax3 = plt.subplot(2, 3, (3, 6)) # de la case 3 à la case 6
ax3.plot(x, y, 'g') # vert

ax4 = plt.subplot(2, 3, (4, 5)) # de la case 4 à la case 5
ax4.plot(x, y, 'y') # jaune
```

```{image} media/subplot1.png
```

ou encore

```python
ax1 = plt.subplot(2, 3, (1, 5)) # les cases de 1 à 5
ax1.plot(x, y, 'm') # majenta

ax3 = plt.subplot(2, 3, 3) # la case 3
ax3.plot(x, y, 'k') # noir

ax3 = plt.subplot(2, 3, 6) # la case 6
ax3.plot(x, y, 'y'); # jaune
```

```{image} media/subplot2.png
```

remarquez que ce code est assez peu lisible  
pour les figures composées sur une grille régulière  
préférez `plt.subplots` et son tableau de sous-figures
````

```{code-cell} ipython3
# le code
ax1 = plt.subplot(2, 3, 1) # la première case
y = np.sin(x)
ax1.plot(x, y, 'b') # bleu

ax2 = plt.subplot(2, 3, 2) # la seconde case
ax2.plot(x, y, 'r') # rouge

ax3 = plt.subplot(2, 3, (3, 6)) # de la case 3 à la case 6
ax3.plot(x, y, 'g') # vert

ax4 = plt.subplot(2, 3, (4, 5)) # de la case 4 à la case 5
ax4.plot(x, y, 'y'); # jaune
```

+++ {"tags": ["framed_cell"]}

## améliorer les figures composées

````{admonition} →
on peut faire un peu de cosmétique  
sachant que quand on commence *on ne s'arrête plus* et on perd beaucoup de temps pour améliorer *à la marge*

préférez au début des affichages minimalistes à peu près lisibles

quelques fonctions pour améliorer:

* `fig.suptitle` pour donner un titre à la figure globale (repérée par la variable-python `fig`)

* `ax1.set_title` pour donner un titre à la sous-figure (repérée par la variable-python `ax1`)

* et aussi `ax.set_xlabel`, `ax.set_ylabel`...

* et enfin le **magique** `plt.tight_layout()` pour ajuster automatique les paddings

exemple de 3 sous-figures avec titres, sous-titres et légendes  
à essayer avec et sans `plt.tight_layout()`

```python
plt.suptitle('une figure avec 3 sous-figures')

ax1 = plt.subplot(2, 2, 1)
ax1.plot(x, y, 'b')
ax1.set_title('sinus bleu')

ax2 = plt.subplot(2, 2, 2)
ax2.set_xlabel('abscisses')
ax2.set_ylabel('ordonnées')
ax2.plot(x, y, 'r')

ax3 = plt.subplot(2, 2, (3, 4))
ax3.plot(x, y, 'g')
ax3.set_title('sinus vert')

# plt.tight_layout()
```

certaines fonctionnalités sont très avancées  
référez-vous à la documentation  <https://matplotlib.org/api/axes_api.html>  
et aux exemples sur Internet
````

```{code-cell} ipython3
:cell_style: center

# le code

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

plt.suptitle('une figure avec 3 sous-figures')

ax1 = plt.subplot(2, 2, 1)
ax1.plot(x, y, 'b')
ax1.set_title('sinus bleu')

ax2 = plt.subplot(2, 2, 2)
ax2.set_xlabel('abscisses')
ax2.set_ylabel('ordonnées')
ax2.plot(x, y, 'r')

ax3 = plt.subplot(2, 2, (3, 4))
ax3.plot(x, y, 'g')
ax3.set_title('sinus vert')


plt.tight_layout()
```
