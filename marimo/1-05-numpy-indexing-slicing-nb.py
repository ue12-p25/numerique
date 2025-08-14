import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium", css_file="public/style_local.css")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# indexation et *slicing*""")
    return


@app.cell
def _():
    import numpy as np
    from matplotlib import pyplot as plt

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Accès à un tableau de dimension > à 1

    l'accès à un élément du tableau dépend de la forme du tableau  

    il y aura - au plus - un indice par dimension (voir plus bas pourquoi *au plus*)

    ---

    #### En dimension 2

    ```python
    tab = np.arange(12).reshape((2, 6))

    # première ligne, deuxième colonne
    line, col = 0, 1

    tab[line, col] = 1000
    tab
    -> array([[ 0, 1000,  2,  3,  4,  5],
              [ 6,    7,  8,  9, 10, 11]])
    ```

    ---

    #### En dimension 3

    ```python
    tab.resize((2, 3, 2))

    # deuxième matrice, troisième ligne, première colonne
    mat, line, col = 1, 2, 0

    tab[mat, line, col] = 2000
    tab
    -> array([[[   0, 10],
               [   2,  3],
               [   4,  5]],

              [[   6,  7],
               [   8,  9],
               [2000, 11]]])
    ```

    /// hint | rappel
    le nombre d'éléments dans chaque dimension est donné par `tab.shape`
    ///

    /// note | pourquoi "au plus" ?

    on a dit qu'il peut y avoir **au plus** un indice par dimension, car on peut en donner moins  
    dans ce cas vous obtenez un sous-tableau au lieu d'une valeur scalaire 

    par exemple si le tableau `a` a pour `shape=(2, 3, 4, 5)`  
    alors `a[i, j]` va, bien sûr, désigner .. un tableau de `shape=(4, 5)`  
    ///

    /// hint | rappel: lignes et colonnes
    :class: dropdown

    * en dimension >=2, les deux dernières dimensions sont les lignes et les colonnes, dans cet ordre  
      (enfin plus exactement, c'est la convention pour l'affichage des tableaux)  

    * du coup en dimension 2, voici un idiome pour ranger ça dans deux variables:  
      ```python
      rows, columns = tab.shape
      ```
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## accès aux éléments d'un tableau

    /// admonition | →

    *accéder à des éléments ou à des sous-tableaux  
    va nous permettre de leur appliquer des fonctions vectorisées*


    la manière d'accéder aux éléments d'un tableau `numpy`  
    dépend de la forme du tableau (`shape`)


    la forme d'un `numpy.ndarray` est donnée par une indexation  
    sur le segment mémoire sous-jacent continu de votre tableau

    **par exemple**

    un `numpy.ndarray` de `12` éléments

    <div class="memory">

    ```
    ☐☐☐☐☐☐☐☐☐☐☐☐
    ```

    </div>

    peut être indexé sous différentes dimensions et formes

    * dimension 1, par exemple `(12,)`
    * dimension 2, par exemple `(1, 12)` `(6, 2)` `(3, 4)` `(4, 3)`
    * dimension 3, par exemple `(2, 3, 2)`...
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## contenu de ce notebook (sauter si déjà acquis)

    * les manières d'accéder à des éléments et de slicer un tableau `numpy`
    * les slices sont des vues et non des copies
    * la notion de `numpy.ndarray.base`
    * voir les `exercices avancés pour les rapides`
    """
    )
    return


@app.cell
def _(np):
    # le code
    tab = np.arange(12)
    tab[0] = np.pi
    tab[0].dtype, tab[0]
    return (tab,)


@app.cell
def _(np, tab):
    # le code
    tab1 = tab.astype(np.float64)
    tab1[0] = np.pi
    tab1[0].dtype, tab1[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    !!! tip ""
        Importa recordar as seguintes regras de diferenciação de matrizes:
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
