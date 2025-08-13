import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    # vectorisation\n\n    ## contenu de ce notebook (sauter si déjà acquis)\n\n    - la **vectorisation** (appliquer une fonction à tout un tableau sans passer par un `for-python`)\n    - les `ufunc`\n    - `numpy.vectorize`\n""")
    return


@app.cell
def _():
    # on importe la librairie numpy
    import numpy as np
    from matplotlib import pyplot as plt
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    ## qu'est-ce que la vectorisation ?\n\n    ### l'idée\n    pour appliquer une fonction à tous les éléments d'un tableau `numpy`\n\n    * ne **jamais** utiliser une boucle `for-python`  \n    * mais appliquer la fonction (ou l'opérateur)  \n      **directement au tableau** - de manière *vectorisée*\n    * c'est plus concis à écrire, vos codes sont plus rapides, plus lisibles !\n    et pourront être optimisés en temps\n\n    /// admonition | la bonne façon \n\n    ```python\n    n = 10000000\n    x = np.linspace(0, 2*np.pi, n)\n\n    y = np.sin(x)  # OUI c'est la bonne façon\n    ```\n    ///\n\n    /// attention | la mauvaise façon\n    :class: danger\n\n    ```python\n    n = 10000000\n    x = np.linspace(0, 2*np.pi, n)\n\n    y = []\n    for e in x:   # NON IL NE FAUT PAS FAIRE UN FOR !!`\n        y.append(np.sin(e))\n    ```\n    ///\n\n    la vectorisation est **la seule manière** d'écrire du code en `numpy`  \n    pour avoir des **temps d'exécution acceptables**\n\n    ### conclusion\n\n    sur des tableaux `numpy` utilisez **toujours** la **vectorisation**  \n    **vectorisation** = le `for` est fait dans `numpy`\n\n\n    vérifiez en comparant les temps d'exécution des deux codes `%%timeit`  \n    attention c'est très long...\n""")
    return


@app.cell
def _(np):
    n = 2000000
    x = np.linspace(0, 2 * np.pi, n)
    # la bonne façon

    def vecto_sin():
        np.sin(x)  # np.sin appliquée au tableau x
    from timeit import timeit
    timeit(vecto_sin, number=1000)
    return timeit, vecto_sin, x


@app.cell
def _():
    # pour comparer les choses comparables
    import math
    return (math,)


@app.cell
def _(math, timeit, vecto_sin, x):
    y = [0 for _ in range(len(x))]
    # la mauvaise façon

    def sin_python():
        for i, e in enumerate(x):  # une boucle for sur un tableau numpy
            # c'est toujours une mauvaise idée
            y[i] = math.sin(e)
    timeit(vecto_sin, number=1000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    /// admonition | pourquoi math.sin et pas np.sin ?\n\n    dans une première version de ce notebook, pour cette deuxième - et mauvaise - façon de faire on avait artificiellement forcé le trait car:\n\n    - on avait utilisé `np.sin` au lieu de `math.sin`; merci à Damien Corral qui a remarqué que `np.sin` appliqué à un scalaire Python ajoute une inefficacité !  \n    - et de plus on rangeait les résultats dans une liste, ce qui aggrave encore les écarts\n\n    après ces corrections, qui permettent de mieux isoler la perte d'efficacité, on observe toujours un rapport de 1 à 10 !\n    (et en plus on ne garde même pas les résultats du calcul)\n    ///\n""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    ### dessiner un cercle de rayon `r`\n\n    **exercice**\n\n    Dessinez un cercle de rayon `r`  \n\n    indices\n\n    1. $x = r\\, sin(\\theta)$  \n       $y = r\\, cos(\\theta)$  \n       avec $\\theta$ variant de $0$ à $2\\pi$\n    1. si votre cercle apparaît elliptique, c'est que les échelles de vos axes diffèrent  \n       demandez à ce qu'elles soient égales avec `plt.axis('equal')`\n""")
    return


@app.cell
def _():
    # votre code
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    ### calculer une fonction polynomiale\n\n    **exercice**\n\n    1. faites une fonction qui retourne le calcul d'un polynome  \n       par exemple $x^3 + 2x^2 -5x +1$  \n       (puissance: `**` ou `np.power`)\n\n    2. appliquez la directement à un `np.ndarray` (sans faire de `for`)\n       qu'obtenez-vous en retour ?\n\n    4. tracez la courbe de la fonction\n""")
    return


@app.function
def scalar_function(x):
    pass


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    ## les `ufunc`\n\n    /// admonition | →\n    Le mécanisme général qui applique une fonction à un tableau  \n    est connu sous le terme de *Universal function* - ou encore `ufunc`  \n\n    En conclusion, vous **devez** toujours utiliser les `ufunc` et plus jamais les `for-python`\n\n    * même si ça vous paraît plus difficile\n    * même si vous utilisiez des `for-python` en prépa\n    * par souci de la **performance en temps**, et de propreté de votre code, vous ne pouvez plus y échapper\n\n    Une habitude à prendre:\n\n    * c'est juste une autre manière de penser le code  \n    * vos codes seront compacts et lisibles (élégants)\n\n    /// attention | utile pour les recherches\n    Souvenez-vous du terme `ufunc` car c'est utile pour des recherches sur Internet\n    ///\n\n    ///\n\n    ---\n\n    ### quelles sont les fonctions vectorisées ?\n\n    /// admonition | →\n    **les opérateurs arithmétiques classiques**  \n    et leur contre-partie `numpy` (*Ufuncs*)\n\n\n    | opérateur | `numpy` fonction    |\n    |----------:|-------------------|\n    |   `+`    | `np.add` |\n    |   `-`    | `np.substract`|\n    |   `*`    | `np.multiply` |\n    |   `/`    | `np.divide` |\n    |   `//`   | `np.floor_divide` |\n    |   `\\%`   | `np.mod` |\n    |   `**`   | `np.power` |\n\n    **les fonctions de comparaison, trigonométriques...**\n\n    | fonction         | `numpy` fonction    |\n    |-----------------:|-------------------|\n    | comparaison      | `np.greater`, `np.less`, `np.equal`, ...|\n    |   valeur absolue | `np.absolute` or `np.abs` |\n    |   trigonometrie  | `np.sin`, `np.cos`, ... |\n    |   exponentielle  | `np.exp`, `np.exp2`, .. |\n    |   logarithme     | `np.log`, `np.log2`, `np.log10` |\n\n    vous allez les utiliser sans même vous en rendre compte !\n    ///\n\n    ---\n\n    ### savoir si une fonction est une `ufunc`\n\n    /// admonition | →\n     demandez-le lui\n\n    ```python\n    np.add\n    <ufunc 'add'>\n    ```\n\n    `numpy.add` en est !\n    ///\n""")
    return


@app.cell
def _(np):
    # essayez !
    np.power
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""\n    ## pour vectoriser une fonction\n\n    **exercice**\n\n    /// admonition | consigne\n\n    le but du jeu ici c'est de voir comment vectoriser une fonction **que vous écrivez vous**  \n    on s'interdit donc, dans cet exercice, d'utiliser des fonctions de `numpy`, ni la fonction *builtin* `abs` de Python\n\n    si vous préférez, vous pouvez choisir d'implémenter une fonction définie par morceaux  \n    genre $x**2$ sur les nombres négatifs et $x^3$ sur les positifs\n    ///\n\n    1. écrivez une fonction qui calcule la valeur absolue d'un scalaire x  `absolute(x)`\n    2. testez votre fonction sur des scalaires\n    3. créez un `np.ndarray` de scalaires et appliquez-lui la fonction\n    4. que se passe-t-il ?\n""")
    return


@app.cell
def _():
    # votre code ici
    return


if __name__ == "__main__":
    app.run()
