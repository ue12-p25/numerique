import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # la mémoire

    ## contenu de ce notebook (sauter si déjà acquis)

    avoir une intuition de ce qui se passe dans en mémoire pour un `numpy.ndarray`  

    > *An array object represents a multidimensional, **homogeneous** array of **fixed-size** items.*

    * indiçage des tableaux `numpy`
    * modification de la taille des tableaux `numpy` avec `numpy.resize` et `numpy.reshape` (la mémoire sous-jacente est partagée)
    * indirection versus décalage (*offset*)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## organisation de la mémoire

    /// admonition | →
    ### pourquoi comprendre comment `numpy` travaille en mémoire ?

    pour prendre des décisions en connaissance de cause  

    * savoir les conséquences de vos choix
    * comprendre les erreurs  
    (conversions implicites...)

    pour ne pas être dépourvu le jour où votre code, en se complexifiant

    * devient beaucoup trop lent
    * prend beaucoup trop d'espace mémoire

    pour vous familiariser avec l'informatique et comprendre

    * les mécanismes sous-jacents
    * les choix des concepteurs

    pour vous faire une petite culture en informatique technique

    * ne jamais penser que c'est magique, incompréhensible, trop compliqué...
    * le plus souvent c'est simplement logique
    ///

    créons un tableau `numpy` en 2 dimensions: 4 lignes et 5 colonnes
    """
    )
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(np):
    mat =  np.array(
        [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]])
    mat
    return (mat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""la mémoire occupée en mémoire en nombre d'octets (byte)""")
    return


@app.cell
def _(mat):
    mat.nbytes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### organisation en mémoire des tableaux

    /// admonition | →
    l'aide (accessible via `help(np.ndarray)`) dit
    > *An array object represents a multidimensional, homogeneous array of fixed-size items.*

    donc un `numpy.ndarray` est un tableau
    1. **multi-dimensionnel**
    1. avec un type d'élément **homogène**
    1. et des éléments de **taille fixe**

    **homogène**  

    * toutes les cases du tableau ont le même type
    * donc elles occupent la même taille en mémoire

    **taille fixe**  

    * une fois un tableau créé, on ne peut plus modifier la taille de ses éléments  
    i.e. le nombre d'octets sur lequel chaque élément est stocké en mémoire est fixe



    * si on manipule et que la taille des éléments ne suffit plus ?  
    `numpy` convertit la valeur  
    mais ne modifie pas la taille de ses éléments


    * pour modifier la taille des éléments ?  
    on n'a pas le choix, il faut allouer un nouveau tableau, et recopier l'ancien dedans (et c'est à éviter...)

    pourquoi ces **contraintes** ?  

    * pour que `numpy` soit le plus rapide possible dans ses manipulations de tableaux
    * grâce à ces contraintes, passer d'une case du tableau à une autre  est très rapide
    ///

    ---

    ### rapidité des manipulations mémoire

    /// admonition | →
    deux **idées** pour assurer la rapidité de manipulation de tableaux en mémoire


    * passez rapidement d'une case du tableau à une autre (**offset**)


    * avoir la valeur de l'élément directement dans la case (pas **d'indirection** mémoire)
    ///

    ---

    ### offset

    /// admonition | →
    supposons que le tableau soit représenté en mémoire par un **bloc d'octets continu**  
    (ici 9 cases sont **contiguës** et de même taille - homogène)

    <div class="memory">

    ```
    ...☐☐☐☐☐☐☐☐☐...
    ```

    </div>


    passer d'une case à une autre devient un simple décalage mémoire  
    *on va 2 cases plus loin*  


    l'**offset** est la distance qui sépare ces deux cases

    un tel décalage devient impossible si un tableau était réparti un peu partout en mémoire...  

    <div class="memory">

    ```
    ...☐.......☐..☐....☐...  
    ☐....☐.....☐.....☐.....  
    ......☐.....
    ```

    </div>
    ///

    ---

    ### pas d'indirection mémoire

    /// admonition | →
    pour un tableau, on sait maintenant

    * que la taille des éléments est homogène  
    * que le bloc est contigu en mémoire

    <div class="memory">

    ```
    ☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
    ```
    </div>


    l'idée de n'avoir pas d'indirection est

    * quand on arrive dans une case du tableau
    * elle contient la valeur qu'on cherche
    * on n'a pas besoin d'aller ailleurs en mémoire

    Que pourrait-il y avoir d'autre dans une case que la valeur d'un élément ?

    si toutes les cases d'un même tableau en informatique ont la même taille, comment puis-je

    * y "*mettre*"  des élément hétérogènes ? entier, réel, string...
    * modifier ces éléments sans réallouer le tableau ?

    ```python
    tab = [1, np.pi, True ]
    tab[0] = 12345678235234501256848345678901234567890264378034
    tab[0] = "bonjour"
    ```

    en `python`, dans une case d'un vecteur (`list`)

    * on ne trouve pas l'objet lui même (`1` ou `"bonjour"`)
    * mais l'**adresse** en mémoire de l'endroit où l'objet a été alloué

    si un tableau contient les adresses de ses éléments  
    et pas directement la valeur des éléments  
    il y aura une indirection à faire quand on arrive sur une case
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### exercice: tableau de chaînes de caractères

    **exercices**

    1. à partir de la liste Python de chaînes de caractères
    ```python
    l = ['un', 'deux', 'trois', 'cinq']
    ```
    créez un tableau `numpy.ndarray` (de nom `tab`) et affichez-le

    1. modifiez le premier élément pour mettre `quatre`
    ```python
    tab[0] = 'quatre'
    ```
    et affichez le tableau

    1. Que constatez-vous ? Pourquoi `quatr` ?

    1. affichez le type des éléments, le comprenez-vous ?  
    `<` est une histoire d'ordre des octets dans les objets  
    `U` signifie unicode  
    Que signifie `5` ?
    """
    )
    return


@app.cell
def _():
    # votre code ici
    return


@app.cell
def _(np):
    "CORRECTION"
    l = ['un', 'deux', 'trois', 'cinq']
    tab = np.array(l)
    tab
    return (tab,)


@app.cell
def _(tab):
    "CORRECTION"
    tab[0] = 'quatre'
    tab
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `numpy` cherche le plus petit type pour stocker les chaînes de caractères initiales

    ici une case est constituée d'un tableau d'au plus 5 caractères  
    (une case n'est pas l'adresse d'une chaîne de caractère mais bien la valeur de la chaîne)
    """
    )
    return


if __name__ == "__main__":
    app.run()
