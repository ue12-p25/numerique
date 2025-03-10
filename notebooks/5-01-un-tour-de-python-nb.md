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
  title: un tour du langage Python
---

# un tour du langage Python

+++

tour d'horizon rapide du langage Python

+++ {"slideshow": {"slide_type": "slide"}}

## commentaires

tout ce qui est après un `#` est un commentaire,  
et sera ignoré par l'interpréteur Python

```{code-cell} ipython3
# ceci est un commentaire

10 * 10   # et ici aussi
```

+++ {"slideshow": {"slide_type": "slide"}}

## importer une librairie

+++

de nombreuses fonctionnalités ne sont pas dans le langage Python  
elles sont disponibles dans des bibliothèques (en Python on dit un **module**) 
qu'on doit **importer**

La première manière de coder est de réutiliser l'existant !

```{code-cell} ipython3
# j'importe le module math
import math
```

```{code-cell} ipython3
# attention cette façon d'obtenir de l'aide est 
# spécifique à IPython / notebooks
# avec un interprète Python standard, on ferait 
# help(math)
math?
```

+++ {"slideshow": {"slide_type": "slide"}}

## utiliser une librairie

une bibliothèque expose typiquement un certain nombre de symboles  
par exemple dans `math` on va trouver

* `pi` une variable qui dénote le nombre $\pi$
* `cos` une fonction qui sait calculer le cosinus

pour accéder à ces symboles on utilise la notation `.`

```{code-cell} ipython3
:cell_style: split

# ceci se lit comme:
# aller chercher l'attribut 'pi' dans l'objet module 'math'
math.pi
```

```{code-cell} ipython3
:cell_style: split

math.cos(math.pi)
```

+++ {"slideshow": {"slide_type": "slide"}}

## nombres

```{code-cell} ipython3
:cell_style: split

# entiers 
10
```

```{code-cell} ipython3
:cell_style: split

# flottants
3.14
```

```{code-cell} ipython3
:cell_style: split

# complexes
1j * (2+4j)
```

```{code-cell} ipython3
:cell_style: split

# booléens True et False
True
```

```{code-cell} ipython3
# les nombres ont des opérateurs (arithmétiques et de comparaison...)
```

```{code-cell} ipython3
:cell_style: split

# 3 est impair
10 % 3 == 1 
```

+++ {"slideshow": {"slide_type": "slide"}}

## précision des calculs flottants

bien sûr un flottant est représenté, en informatique, comme une suite de bits 0 ou 1  
cela induit des calculs avec une précision imparfaite

```{code-cell} ipython3
:cell_style: split

# sur les architectures actuelles 
# un flottant est encodé sur 64 bits

0.2 + 0.1
```

```{code-cell} ipython3
:cell_style: split

0.2 + 0.1 == 0.3
```

```{code-cell} ipython3
:cell_style: split

0.2 + 0.2 == 0.4
```

```{code-cell} ipython3
# cette fonction est pratique pour faire 
# un test de quasi-égalité sur les flottants
math.isclose(0.2+0.1, 0.3)
```

+++ {"slideshow": {"slide_type": "slide"}}

## précision des calculs flottants
**optionnel**

+++ {"slideshow": {"slide_type": ""}}

la façon de passer d'un flottant à une séquence de bits  
s'appelle un **encodage** 
[dans le cas des flottants: IEE754](https://en.wikipedia.org/wiki/IEEE_754)  
qui est efficace car supporté par le processeur

+++ {"slideshow": {"slide_type": ""}}

pour faire court - dans le cas le plus courant (`binary64`)  
la précision des calculs est de l'ordre de $10^{-15}$ 


voir un [convertisseur en ligne](http://www.binaryconvert.com/convert_double.html) pour visuels

+++ {"slideshow": {"slide_type": "slide"}}

## définir une variable

pour définir une variable, il suffit de l'affecter avec le signe `=`

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: ''
---
# remarquez que ceci n'affiche rien
a = 10
```

```{code-cell} ipython3
:cell_style: split

# l'utilité c'est bien sûr 
# de garder un résultat pour
# s'en reservir ensuite
a + a
```

+++ {"slideshow": {"slide_type": "slide"}}

## texte (chaînes de caractères)

```{code-cell} ipython3
:cell_style: split

# un texte est entre deux '

texte1 = 'bonjour le monde'
print(texte1)
```

```{code-cell} ipython3
:cell_style: split

# ou si on préfère entre "

texte2 = "bonjour le monde"
print(texte2)
```

```{code-cell} ipython3
:cell_style: split

# comme ça on peut insérer un "

print('Python est un langage "typé"')
```

```{code-cell} ipython3
:cell_style: split

# ou un '

print("Python est un langage 'typé'")
```

+++ {"slideshow": {"slide_type": "slide"}}

## `print()`

remarquez qu'on a utilisé la fonction `print` qui est prédéfinie  
on peut l'appeler avec autant d'arguments qu'on veut  
  et de n'importe quel type

```{code-cell} ipython3
# simplement pour illustration des possibilités d'appel de fonction
# car on va voir plus loin une forme beaucoup plus pratique
# pour faire ce genre de choses
#
x = 12
print("la somme de", x, "et", 13, "vaut", x+13)
```

+++ {"slideshow": {"slide_type": "slide"}}

## formatage

pour construire des chaines lisibles,  
le plus simple est la *f-string*

```{code-cell} ipython3
:cell_style: split

# une f-string se présente comme une chaine 
# mais préfixée par un f collé
# avant le guillement ouvrant
# qui peut être ' ou " 

f"une f-string"
```

```{code-cell} ipython3
:cell_style: split

# l'intérêt est qu'on peut 
# alors insérer des variables
# directement dans la chaine
# en les mettant entre {}

print(f'pi = {math.pi}')
```

```{code-cell} ipython3
# en fait j'ai dit 'variable' mais on peut mettre n'importe quelle expression
# c'est à dire qu'à l'intérieur des {} on peut faire des calculs, ici sin(pi)
print(f"pi = {math.pi} et sin(pi) = {math.sin(math.pi)}")
```

+++ {"slideshow": {"slide_type": "slide"}}

## formatage - plus finement

il y a des tas de possibilités pour affiner la façon  
dont les données sont mises en forme  
pour cela ajouter un format dans les `{}` avec un `:`  
par exemple pour afficher deux chiffres après la virgule :

```{code-cell} ipython3
:cell_style: center

print(f"bla {2*math.pi:.2f} bla")
```

+++ {"cell_style": "split"}

![](media/f-string.svg)

+++ {"slideshow": {"slide_type": "slide"}}

## fonctions

on définit une fonction avec le mot-clé `def`

```{code-cell} ipython3
:cell_style: center

# on définit une fonction en donnant son nom
# et les noms de ses paramètres
def P(x):
    return x**2 + 3*x + 2
```

vous remarquez que le code de la fonction est indenté  
en effet python utilise l'**indentation** pour déterminer le bloc auquel appartient une instruction

```{code-cell} ipython3
:cell_style: split

# mintenant que la fonction est définie
# on peut maintenant l'appeler (l'exécuter)
P(10)
```

```{code-cell} ipython3
:cell_style: split

# une curiosité: True se comporte comme le nombre 1
P(True)
```

## instructions

+++

conditions, branchements, boucles ... Python a tout un ensemble d'instructions pour contruire vos programmes

```{code-cell} ipython3
:cell_style: split

x = 12
if x%2 == 0:
    print(f'{x} est pair')
else:
    print(f'{x} est impair')
```

python utilise l'indentation pour déterminer le bloc auquel appartient une instruction

```{code-cell} ipython3
:cell_style: split

x = 3
while x != 0:
    print(x)
    x = x-1   
```

+++ {"cell_style": "split"}

```python
# à éviter d'exécuter ...
x = 3
while x != 0:
    print(x)
x = x-1
```
à quel bloc appartient ```x = x-1```

+++

## itérations

+++

parmi les instructions du langage, il y a la boucle `for` qui joue un rôle un peu à part (notion d'itérateurs et générateurs notamment)

```{code-cell} ipython3
# pour anticiper un peu
L = [1, 2, 3]
for item in L:
    print(item)
```

```{code-cell} ipython3
D = {'pierre': 20, 'jean': 32}
for key, value in D.items():
    print(key, '->', value)
```

## blocs

+++

les blocs sont délimités par indentation, il n'y a pas de syntaxe de bloc à-la `c` avec des `{...}`  
ce qui rend les codes un peu plus lisibles

+++ {"slideshow": {"slide_type": "slide"}}

## mots clés

+++ {"cell_style": "center"}

un certain nombre de mots sont réservés au langage;  
ce sont les "mots-clé" du langage   
on ne peut pas les utiliser comme noms de variable

+++ {"cell_style": "split"}

```python
# ceci provoque une erreur
if = 2

  File "<ipython-input>", line 3
    if = 2
       ^
SyntaxError: invalid syntax
```

+++ {"cell_style": "split"}

| **liste**    |   &nbsp; | &nbsp;  | &nbsp;       | &nbsp; |
|----------:|---------:|--------:|-------------:|-------:|
| False | await | else    | import       | pass   |
| None  | break    | except  | in           | raise  |
| True  | class    | finally | is           | return |
| and       | continue | for     | lambda       | try    |
| as        | def      | from    | nonlocal | while  |
| assert    | del      | global  | not          | with   |
| async | elif     | if      | or           | yield  |

+++ {"slideshow": {"slide_type": "slide"}}

## importer des symboles (variables, fonctions...)

on peut aussi faire comme ceci

```{code-cell} ipython3
:cell_style: split

from math import pi, sin

pi
```

```{code-cell} ipython3
:cell_style: split

# idem
sin(pi)
```

+++ {"slideshow": {"slide_type": "notes"}}

Préférez savoir d'où viennent les fonctions que vous utilisez.  
C'est pourquoi on vous recommande fortement d'utiliser la forme `math.sin` plutôt que `sin`, qui garde la trace du module d'où provient le symbole `sin`.

+++

On peut renommer une librairie  
par exemple pour en raccourcir le nom

```{code-cell} ipython3
:cell_style: split

# la librairie numpy doit être installée
# dans votre environnement ...
import numpy as np
```

```{code-cell} ipython3
:cell_style: split

# grâce à la forme import .. as
# on a installé la librairie numpy
# mais dans notre code on l'utilise sous le nom np
np.sin(np.pi)
```

+++ {"slideshow": {"slide_type": "notes"}}

Remarquez qu'ici on devrait obtenir 0, mais les calculs sur les flottants sont faits de manière approchée.

+++

## containers

+++

listes, ensembles, dictionnaires ... Python vous permet de définir des containeurs d'objets

```{code-cell} ipython3
# la liste permet de préserver l'ordre, avec d'éventuels duplicats
L = [10, 20, 10, 20, 10, 20]
L
```

```{code-cell} ipython3
# l'ensemble au contraire élimine les duplicats
S = {10, 20, 10, 20, 10, 20}
S
```

```{code-cell} ipython3
# le dictionnaire, c'est un peu comme un ensemble
# dans lequel chaque élément (qu'on appelle une clé)
# possède une valeur
D = {'dix': 10, 'vingt': 20}
D
```

```{code-cell} ipython3
# pour accéder, les indices commencent toujours à 0
print(L[0], L[5])
```

```{code-cell} ipython3
# dans les dictionnaires on accède par la clé
D['dix']
```

```{code-cell} ipython3
# on ne peut pas accéder au i-ème élément d'un ensemble
# mais on peut chercher si un élément existe
100 in S
```

pour les modifier

```{code-cell} ipython3
:cell_style: split

# liste ordonnée d'objets
# de type hétérogène
l = ['il', 12, 78.5, False, 'il']
l.append('bonjour')
print(l)
```

```{code-cell} ipython3
:cell_style: split

# ensemble d'objets de type hétérogène
s = {'il', 12, 78.5, False, 'il'}
s.add('bonjour')
print(s)
```

```{code-cell} ipython3
# dictionnaire i.e. ensemble de couples (clé, valeur)
d = {'zero':0, 'un':1,'trois':3}
d['deux'] = 2 
print(d)
```

+++ {"slideshow": {"slide_type": "slide"}}

## `len()`

+++

il existe une fonction prédéfinie très pratique: `len()`  
qui retourne la longeur d'un objet (le nombre d'éléments qu'il contient)

```{code-cell} ipython3
:cell_style: split

# sur une chaine len()
# retourne le nombre de caractères
#
# remarquez que les guillemets ne comptent pas
len("abc")
```

```{code-cell} ipython3
:cell_style: split

# on compte les caractères 
# et pas les octets

len("été")
```

```{code-cell} ipython3
:cell_style: center

# sur un objet d'un type structuré
# retourne le nombre d'éléments
d = {'zero': 0, 'un': 1, 'trois': 3}
len(d)
```

+++ {"slideshow": {"slide_type": "slide"}}

## textes plus longs

si vous avez besoin d'écrire des textes de plusieurs lignes  
utilisez `"""` au lieu de `"`  -- (ou `'''`)

```{code-cell} ipython3
:cell_style: split

bafouille = \
"""To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,"""
```

```{code-cell} ipython3
:cell_style: split

print(bafouille)
```

```{code-cell} ipython3
:cell_style: split

# idem avec '''
# le changement de ligne compte 
# pour un caractère (newline) 
court = '''a
b'''
```

```{code-cell} ipython3
:cell_style: split

print(court)
```

```{code-cell} ipython3
:cell_style: split

# les caractères sont 'a', '\n', et 'b'
len(court)
```

## types

+++

pas besoin de préciser le type d'un objet, Python le déduit tout seul        
tout a un type: les variables, les fonctions les modules ...

```{code-cell} ipython3
:cell_style: split

a = 10
type(a)
```

```{code-cell} ipython3
:cell_style: split

b = -17.5
type(b)
```

```{code-cell} ipython3
:cell_style: split

# le résultat d'une expression
# est un objet et du coup il a un type
type(10 < 3)
```

```{code-cell} ipython3
:cell_style: split

# une fonction usuelle
def incr (x):
    return x+1

type(incr)
```

```{code-cell} ipython3
# une fonction builtin
type(len)
```

```{code-cell} ipython3
:cell_style: split

# un module
import math
type(math)
```

## écrire dans un fichier

+++

en 3 étapes: on ouvre un fichier, on écrit dedans et on ferme le fichier

```{code-cell} ipython3
:cell_style: center

# on écrit des chaînes de caractères
file = 'hamlet.txt'
f = open(file, 'w') # w pour le mode écriture
f.write(bafouille)
f.write('Or to take Arms ...')
f.close()
# ne pas oublier de fermer le fichier !
```

cette première façon de faire c'est la version 'pédestre' mais c'est très *old-school*, et **pas du tout recommandé**; on la montre juste pour bien décortiquer ce qui est fait

la **bonne façon** de faire, c'est celle-ci:

```{code-cell} ipython3
:cell_style: center

# en beaucoup beaucoup plus élégant ....
file = 'hamlet.txt'

with open(file, 'w') as f:
    f.write(bafouille)
    f.write('Or to take Arms ...')
# vous ne pouvez pas oublier
# de fermer le fichier
```

on peut aussi utiliser `print(des, trucs, file=f)` plutôt que `write`

+++

## lire le contenu d'un fichier

```{code-cell} ipython3
:cell_style: split

# tout le contenu
file = 'hamlet.txt'
with open(file, 'r') as f:
    print(f.read())
```

```{code-cell} ipython3
:cell_style: split

# ligne par ligne
file = 'hamlet.txt'
with open(file, 'r') as f:
    for line in f:
        print(line, end='') # la fin de ligne est ''
```

## définir de nouveaux types - avancé

+++

on peut introduire dans Python de nouveaux types de données

+++

vous avez besoin d'objets de type rationnel ?  
construits à partir d'un numerator et d'un denominator ?  
avec  des fonctions de réduction et d'affichage ?

```python
r = Rational(2, 4)
r.reduce()
print(r) # affiche 1/2
```

* définissez une `class Rational`
* implémentez la fonction pour construire un objet de cette classe  
  en définissant la méthode `__init__`  
  qui va conserver dans des attributs del'objet le numérateur et le dénominateur    

* implémentez des méthodes de ces objets `reduce`, `add`...

```{code-cell} ipython3
class Rational:
    
    # le constructeur
    def __init__ (self, n, d):
        # self est par convention l'objet qu'on construit
        self.num = n # on range un attribut dans l'objet construit
        self.denom = d # on range un autre attribut dans self
        
    # une méthode = une fonction qui travaille sur un objet (ici self)
    def reduce (self):
        # à vous de la faire ...
        pass
    
    # la méthode qui sera appelée
    # quand votre objet sera affiché ou mis dans une chaîne de caractère
    def __str__ (self):
        return f'{self.num}/{self.denom}'

# on construit un objet de type Rational
# de numérateur 2 et dénominateur 4
r = Rational(2, 4)

# on le réduit ... (si vous implémentez la fonction)
r.reduce()

print(r) # on l'affiche sous la forme 1/2 si reduce est implémentée, sinon 2/4

# on le représente
r # pour changer cette représentation assez technique ... implémentez la fonction __repr__
```

## type prédéfinis

+++

`int`, `bool`, `float`, `str`, `list`, `dict`, `set` ... tous ces types sont eux même définis par des classes  
et donc tous ces types ont aussi des méthodes ...

```{code-cell} ipython3
:cell_style: split

# je construis une liste vide
l = list()
len(l)
```

```{code-cell} ipython3
:cell_style: split

# j'ajoute des éléments en fin de liste
l.append(12)
l.append(13)
print(l)
```

```{code-cell} ipython3
:cell_style: center

# méthodes sur les chaines
chaine = "bonjour"

chaine.capitalize()
```

+++ {"slideshow": {"slide_type": "slide"}}

deux méthodes très utiles sur les chaines : `split` et `join`

```{code-cell} ipython3
longue_chaine = "une liste de mots à découper"
```

```{code-cell} ipython3
:cell_style: split

# sert à découper une chaine 
# en morceaux

mots = longue_chaine.split()
mots
```

```{code-cell} ipython3
:cell_style: split

# et avec join on peut réassembler
# avec le caractère spécifié

"+".join(mots)
```

## python ... et la question du style

+++

tout code Python *est censé* obéir à un style très précis décrit ici https://www.python.org/dev/peps/pep-0008/

+++

Pourquoi ?  

parce que, comme le dit Guido Van Rossum  **un code est beaucoup plus souvent lu qu'il n'est écrit**  
aussi est-il important s'assurer la lisibilité et la cohérence de vos codes

+++

## objets et types 

**optionnel**

+++

Python est **orienté objet**; ça signifie que: 

* toutes les données manipulées en Python sont des **objets**
* tout objet a **un type unique** (qu'on peut obtenir avec `type()`)
* par contre une variable n'est pas typée  
  par exemple elle peut désigner (on dit *référencer*) d'abord un entier, puis plus tard une liste  
  (contrairement aux langages typés statiquement comme C++ par exemple)

* en créant une classe, je définis un **nouveau type** pour représenter de manière idoine les données de mon application

```{code-cell} ipython3
# on peut toujours appeler type() 
x, y = 1, 3.14
type(x)
type(y)
```

```{code-cell} ipython3
# une variable peut changer de type
x = [1, 2, 3]
type(x)
```

```{code-cell} ipython3
# vraiment tout a un type
import math
type(math)
```

```{code-cell} ipython3
# vraiment tout a un type
def foo(x):
    pass
type(foo)
```

```{code-cell} ipython3
# vraiment tout a un type
type(None)
```

```{code-cell} ipython3
# vous avez compris l'idée générale
type(type(x))
```
