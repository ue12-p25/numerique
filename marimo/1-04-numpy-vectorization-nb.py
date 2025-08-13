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
    # vectorisation

    ## contenu de ce notebook (sauter si déjà acquis)

    - la **vectorisation** (appliquer une fonction à tout un tableau sans passer par un `for-python`)
    - les `ufunc`
    - `numpy.vectorize`
    """
    )
    return


@app.cell
def _():
    # on importe la librairie numpy
    import numpy as np
    from matplotlib import pyplot as plt
    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## qu'est-ce que la vectorisation ?

    ### l'idée
    pour appliquer une fonction à tous les éléments d'un tableau `numpy`

    * ne **jamais** utiliser une boucle `for-python`  
    * mais appliquer la fonction (ou l'opérateur)  
      **directement au tableau** - de manière *vectorisée*
    * c'est plus concis à écrire, vos codes sont plus rapides, plus lisibles !
    et pourront être optimisés en temps

    /// admonition | la bonne façon 

    ```python
    n = 10000000
    x = np.linspace(0, 2*np.pi, n)

    y = np.sin(x)  # OUI c'est la bonne façon
    ```
    ///

    /// attention | la mauvaise façon
    :class: danger

    ```python
    n = 10000000
    x = np.linspace(0, 2*np.pi, n)

    y = []
    for e in x:   # NON IL NE FAUT PAS FAIRE UN FOR !!`
        y.append(np.sin(e))
    ```
    ///

    la vectorisation est **la seule manière** d'écrire du code en `numpy`  
    pour avoir des **temps d'exécution acceptables**

    ### conclusion

    sur des tableaux `numpy` utilisez **toujours** la **vectorisation**  
    **vectorisation** = le `for` est fait dans `numpy`


    vérifiez en comparant les temps d'exécution des deux codes `%%timeit`  
    attention c'est très long...
    """
    )
    return


@app.cell
def _(np):
    n = 2000000
    x = np.linspace(0, 2*np.pi, n)

    # la bonne façon
    def vecto_sin():
        np.sin(x)         # np.sin appliquée au tableau x

    from timeit import timeit
    timeit(vecto_sin, number=1000)
    return n, timeit, vecto_sin, x


@app.cell
def _():
    # pour comparer les choses comparables
    import math
    return (math,)


@app.cell
def _(math, timeit, vecto_sin, x):
    y = [ 0 for _ in range(len(x)) ]

    # la mauvaise façon
    def sin_python():
        for i, e in enumerate(x):     # une boucle for sur un tableau numpy
                                      # c'est toujours une mauvaise idée
            y[i] = math.sin(e)

    timeit(vecto_sin, number=1000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// admonition | pourquoi math.sin et pas np.sin ?

    dans une première version de ce notebook, pour cette deuxième - et mauvaise - façon de faire on avait artificiellement forcé le trait car:

    - on avait utilisé `np.sin` au lieu de `math.sin`; merci à Damien Corral qui a remarqué que `np.sin` appliqué à un scalaire Python ajoute une inefficacité !  
    - et de plus on rangeait les résultats dans une liste, ce qui aggrave encore les écarts

    après ces corrections, qui permettent de mieux isoler la perte d'efficacité, on observe toujours un rapport de 1 à 10 !
    (et en plus on ne garde même pas les résultats du calcul)
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### dessiner un cercle de rayon `r`

    **exercice**

    Dessinez un cercle de rayon `r`  

    indices

    1. $x = r\, sin(\theta)$  
       $y = r\, cos(\theta)$  
       avec $\theta$ variant de $0$ à $2\pi$
    1. si votre cercle apparaît elliptique, c'est que les échelles de vos axes diffèrent  
       demandez à ce qu'elles soient égales avec `plt.axis('equal')`
    """
    )
    return


@app.cell
def _():
    # votre code
    return


@app.cell
def _(n, np, plt):
    "CORRECTION"
    theta = np.linspace(0, 2*np.pi, n)
    plt.axis('equal')
    plt.plot(np.sin(theta), np.cos(theta))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### calculer une fonction polynomiale

    **exercice**

    1. faites une fonction qui retourne le calcul d'un polynome  
       par exemple $x^3 + 2x^2 -5x +1$  
       (puissance: `**` ou `np.power`)

    2. appliquez la directement à un `np.ndarray` (sans faire de `for`)
       qu'obtenez-vous en retour ?

    4. tracez la courbe de la fonction
    """
    )
    return


@app.function
# votre code ici
def scalar_function(x):
    pass


@app.cell
def _(np, plt):
    "CORRECTION"
    def scalar_function_corrige(x):
        return x**3 + 2*x**2 -5*x + 1
    x1 = np.linspace(0, 100, 10000)
    y1 = scalar_function_corrige(x1)
    plt.plot(x1, y1)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## les `ufunc`

    /// admonition | →
    Le mécanisme général qui applique une fonction à un tableau  
    est connu sous le terme de *Universal function* - ou encore `ufunc`  

    En conclusion, vous **devez** toujours utiliser les `ufunc` et plus jamais les `for-python`

    * même si ça vous paraît plus difficile
    * même si vous utilisiez des `for-python` en prépa
    * par souci de la **performance en temps**, et de propreté de votre code, vous ne pouvez plus y échapper

    Une habitude à prendre:

    * c'est juste une autre manière de penser le code  
    * vos codes seront compacts et lisibles (élégants)

    /// attention | utile pour les recherches
    Souvenez-vous du terme `ufunc` car c'est utile pour des recherches sur Internet
    ///

    ///

    ---

    ### quelles sont les fonctions vectorisées ?

    /// admonition | →
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
    ///

    ---

    ### savoir si une fonction est une `ufunc`

    /// admonition | →
     demandez-le lui

    ```python
    np.add
    <ufunc 'add'>
    ```

    `numpy.add` en est !
    ///
    """
    )
    return


@app.cell
def _(np):
    # essayez !
    np.power
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## pour vectoriser une fonction

    **exercice**

    /// admonition | consigne

    le but du jeu ici c'est de voir comment vectoriser une fonction **que vous écrivez vous**  
    on s'interdit donc, dans cet exercice, d'utiliser des fonctions de `numpy`, ni la fonction *builtin* `abs` de Python

    si vous préférez, vous pouvez choisir d'implémenter une fonction définie par morceaux  
    genre $x**2$ sur les nombres négatifs et $x^3$ sur les positifs
    ///

    1. écrivez une fonction qui calcule la valeur absolue d'un scalaire x  `absolute(x)`
    2. testez votre fonction sur des scalaires
    3. créez un `np.ndarray` de scalaires et appliquez-lui la fonction
    4. que se passe-t-il ?
    """
    )
    return


@app.cell
def _():
    # votre code ici
    return


@app.cell
def _():
    "CORRECTION"
    def absolute(x):
        if x < 0:
            return -x
        return x

    print(absolute(-1))
    print(absolute(5))
    return (absolute,)


@app.cell
def _(np):
    "CORRECTION"
    test_array = np.array([-1, 2, -3, 4, 5])
    return (test_array,)


@app.cell
def _(absolute, test_array):
    "CORRECTION"
    absolute(test_array)
    return


@app.cell
def _(absolute, np, test_array):
    "CORRECTION"
    absolute_vec = np.vectorize(absolute)
    absolute_vec(test_array)
    return


if __name__ == "__main__":
    app.run()
