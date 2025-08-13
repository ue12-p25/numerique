import marimo
__generated_with = '0.14.13'
app = marimo.App(width='medium')

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    # la mémoire\n\n    ## contenu de ce notebook (sauter si déjà acquis)\n\n    avoir une intuition de ce qui se passe dans en mémoire pour un `numpy.ndarray`  \n\n    > *An array object represents a multidimensional, **homogeneous** array of **fixed-size** items.*\n\n    * indiçage des tableaux `numpy`\n    * modification de la taille des tableaux `numpy` avec `numpy.resize` et `numpy.reshape` (la mémoire sous-jacente est partagée)\n    * indirection versus décalage (*offset*)\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## organisation de la mémoire\n\n    /// admonition | →\n    ### pourquoi comprendre comment `numpy` travaille en mémoire ?\n\n    pour prendre des décisions en connaissance de cause  \n\n    * savoir les conséquences de vos choix\n    * comprendre les erreurs  \n    (conversions implicites...)\n\n    pour ne pas être dépourvu le jour où votre code, en se complexifiant\n\n    * devient beaucoup trop lent\n    * prend beaucoup trop d'espace mémoire\n\n    pour vous familiariser avec l'informatique et comprendre\n\n    * les mécanismes sous-jacents\n    * les choix des concepteurs\n\n    pour vous faire une petite culture en informatique technique\n\n    * ne jamais penser que c'est magique, incompréhensible, trop compliqué...\n    * le plus souvent c'est simplement logique\n    ///\n\n    créons un tableau `numpy` en 2 dimensions: 4 lignes et 5 colonnes\n    ")
    return

@app.cell
def _():
    import numpy as np
    return (np,)

@app.cell
def _(np):
    mat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
    mat
    return (mat,)

@app.cell(hide_code=True)
def _(mo):
    mo.md("la mémoire occupée en mémoire en nombre d'octets (byte)")
    return

@app.cell
def _(mat):
    mat.nbytes
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    ### organisation en mémoire des tableaux\n\n    /// admonition | →\n    l\'aide (accessible via `help(np.ndarray)`) dit\n    > *An array object represents a multidimensional, homogeneous array of fixed-size items.*\n\n    donc un `numpy.ndarray` est un tableau\n    1. **multi-dimensionnel**\n    1. avec un type d\'élément **homogène**\n    1. et des éléments de **taille fixe**\n\n    **homogène**  \n\n    * toutes les cases du tableau ont le même type\n    * donc elles occupent la même taille en mémoire\n\n    **taille fixe**  \n\n    * une fois un tableau créé, on ne peut plus modifier la taille de ses éléments  \n    i.e. le nombre d\'octets sur lequel chaque élément est stocké en mémoire est fixe\n\n\n\n    * si on manipule et que la taille des éléments ne suffit plus ?  \n    `numpy` convertit la valeur  \n    mais ne modifie pas la taille de ses éléments\n\n\n    * pour modifier la taille des éléments ?  \n    on n\'a pas le choix, il faut allouer un nouveau tableau, et recopier l\'ancien dedans (et c\'est à éviter...)\n\n    pourquoi ces **contraintes** ?  \n\n    * pour que `numpy` soit le plus rapide possible dans ses manipulations de tableaux\n    * grâce à ces contraintes, passer d\'une case du tableau à une autre  est très rapide\n    ///\n\n    ---\n\n    ### rapidité des manipulations mémoire\n\n    /// admonition | →\n    deux **idées** pour assurer la rapidité de manipulation de tableaux en mémoire\n\n\n    * passez rapidement d\'une case du tableau à une autre (**offset**)\n\n\n    * avoir la valeur de l\'élément directement dans la case (pas **d\'indirection** mémoire)\n    ///\n\n    ---\n\n    ### offset\n\n    /// admonition | →\n    supposons que le tableau soit représenté en mémoire par un **bloc d\'octets continu**  \n    (ici 9 cases sont **contiguës** et de même taille - homogène)\n\n    <div class="memory">\n\n    ```\n    ...☐☐☐☐☐☐☐☐☐...\n    ```\n\n    </div>\n\n\n    passer d\'une case à une autre devient un simple décalage mémoire  \n    *on va 2 cases plus loin*  \n\n\n    l\'**offset** est la distance qui sépare ces deux cases\n\n    un tel décalage devient impossible si un tableau était réparti un peu partout en mémoire...  \n\n    <div class="memory">\n\n    ```\n    ...☐.......☐..☐....☐...  \n    ☐....☐.....☐.....☐.....  \n    ......☐.....\n    ```\n\n    </div>\n    ///\n\n    ---\n\n    ### pas d\'indirection mémoire\n\n    /// admonition | →\n    pour un tableau, on sait maintenant\n\n    * que la taille des éléments est homogène  \n    * que le bloc est contigu en mémoire\n\n    <div class="memory">\n\n    ```\n    ☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐\n    ```\n    </div>\n\n\n    l\'idée de n\'avoir pas d\'indirection est\n\n    * quand on arrive dans une case du tableau\n    * elle contient la valeur qu\'on cherche\n    * on n\'a pas besoin d\'aller ailleurs en mémoire\n\n    Que pourrait-il y avoir d\'autre dans une case que la valeur d\'un élément ?\n\n    si toutes les cases d\'un même tableau en informatique ont la même taille, comment puis-je\n\n    * y "*mettre*"  des élément hétérogènes ? entier, réel, string...\n    * modifier ces éléments sans réallouer le tableau ?\n\n    ```python\n    tab = [1, np.pi, True ]\n    tab[0] = 12345678235234501256848345678901234567890264378034\n    tab[0] = "bonjour"\n    ```\n\n    en `python`, dans une case d\'un vecteur (`list`)\n\n    * on ne trouve pas l\'objet lui même (`1` ou `"bonjour"`)\n    * mais l\'**adresse** en mémoire de l\'endroit où l\'objet a été alloué\n\n    si un tableau contient les adresses de ses éléments  \n    et pas directement la valeur des éléments  \n    il y aura une indirection à faire quand on arrive sur une case\n    ///\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### exercice: tableau de chaînes de caractères\n\n    **exercices**\n\n    1. à partir de la liste Python de chaînes de caractères\n    ```python\n    l = ['un', 'deux', 'trois', 'cinq']\n    ```\n    créez un tableau `numpy.ndarray` (de nom `tab`) et affichez-le\n\n    1. modifiez le premier élément pour mettre `quatre`\n    ```python\n    tab[0] = 'quatre'\n    ```\n    et affichez le tableau\n\n    1. Que constatez-vous ? Pourquoi `quatr` ?\n\n    1. affichez le type des éléments, le comprenez-vous ?  \n    `<` est une histoire d'ordre des octets dans les objets  \n    `U` signifie unicode  \n    Que signifie `5` ?\n    ")
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    `numpy` cherche le plus petit type pour stocker les chaînes de caractères initiales\n\n    ici une case est constituée d'un tableau d'au plus 5 caractères  \n    (une case n'est pas l'adresse d'une chaîne de caractère mais bien la valeur de la chaîne)\n    ")
    return
if __name__ == '__main__':
    app.run()