import marimo
__generated_with = '0.14.13'
app = marimo.App(width='medium')

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    # les tableaux\n\n    ## contenu de ce notebook (sauter si déjà acquis)\n\n    /// admonition | fonctions de création de tableaux numpy\n\n    | les fonctions | ce qu'elles font |\n    |-:|-|\n    | `np.array` | renvoie la version ndarray d'un tableau existant |\n    | `np.empty` | renvoie un ndarray vide (éléments non initialisés) |\n    | `np.zeros` | renvoie un ndarray rempli de *0.* (float) |\n    | `np.ones` | renvoie un ndarray rempli de *1.* (float) |\n    | `np.linspace` | un vecteur de valeurs bien espacées entre deux bornes |\n    | `np.random.randint` | entiers aléatoirement générés |\n    | `np.random.randn` | flottants aléatoirement générés |\n    ///\n\n    /// admonition | attributs/méthodes de manipulation de tableaux numpy\n\n    | attributs/méthodes | ce qu'ils font |\n    |-:|-|\n    | `np.ndarray.shape`    | la forme du tableau (tuple) |\n    | `np.ndarray.size`     | le nombre d'éléments du tableau |\n    | `np.ndarray.ndim`     | le nombre de dimensions du tableau |\n    | `np.ndarray.dtype`    | le type des éléments |\n    | `np.ndarray.itemsize` | la taille en octet d'un élément |\n    | `np.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octet |\n    | `np.ndarray.astype`   | copie tableau avec autre type pour les éléments |\n    ///\n\n    la taille (en nombre d'octets) des éléments d'un `numpy.ndarray` existant est constante  \n    une modification peut causer une conversion de la valeur ou une erreur\n\n\n    calculs de temps d'exécution avec `%timeit`\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## rappels\n\n    /// admonition | →\n\n    Python ne possède pas, de base, de type adapté aux tableaux multi-dimensionnels\n\n\n    ceux-ci sont proposés par la librairie numérique `numpy`  \n    qu'il faut installer séparément (`pip install numpy` dans le terminal)\n    ///\n    ")
    return

@app.cell
def _():
    import numpy as np
    return (np,)

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## tableaux  multi-dimensionnels `numpy`\n\n    /// admonition | →\n\n    créés par la méthode `numpy.array`  \n    (ici plus précisément `np.array` comme l'identifiant utilisé lors de l'import est `np` mais on reste genéral)\n\n\n    leur type est `numpy.ndarray` (tableau en dimension n)\n\n    attributs et méthodes que nous allons utiliser souvent\n\n    | nom                      | comportement                                     |\n    |-------------------------:|--------------------------------------------------|\n    | `numpy.ndarray.shape`    | la forme du tableau (tuple)                      |\n    | `numpy.ndarray.dtype`    | le type des éléments                             |\n    | `numpy.ndarray.astype`   | crée tableau avec nouveau type d'éléments        |\n\n\n    ou moins souvent\n\n    | nom                      | comportement                                     |\n    |-------------------------:|--------------------------------------------------|\n    | `numpy.ndarray.ndim`     | le nombre de dimensions du tableau               |\n    | `numpy.ndarray.itemsize` | la taille en octet d'un élément                  |\n    | `numpy.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octets |\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### création d'un tableau multi-dimensionnel\n\n    /// admonition | →\n    reprenons notre matrice en Python brut\n\n    ```python\n    matrice = [\n        [1, 2, 3, 4, 5],\n        [6, 7, 8, 9, 10],\n        [11, 12, 13, 14, 15],\n        [16, 17, 18, 19, 20]\n    ]\n    ```\n\n    avec la fonction `numpy.array` nous créons un tableau multi-dimensionnel initialisé avec notre matrice\n\n    ```python\n    mat = np.array(matrice)\n    ```\n\n\n    nous n'avons indiqué\n\n    * ni la forme du tableau\n    * ni le type des éléments\n\n    `numpy.array` a tout déduit\n\n    **type** de `mat` est `numpy.ndarray` i.e. *n-dimensional-array*\n\n    ```python\n    type(mat)\n        -> <class 'numpy.ndarray'>\n    ```\n    ///\n\n    le code\n    ")
    return

@app.cell
def _(np):
    matrice = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    mat = np.array(matrice)
    print(mat)
    print(type(mat))
    return (mat,)

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ###  type et taille mémoire des éléments du tableau\n\n    /// admonition | →\n    ```python\n    matrice = [\n        [1, 2, 3],\n        [4, 5, 6]\n    ]\n    mat = np.array(matrice)\n    ```\n\n    l'attribut `numpy.ndarray.dtype` donne le **type des éléments** du tableau\n\n    ```python\n\n    mat.dtype\n    -> dtype('int64')\n    ```\n    ou bien\n    ```python\n\n    mat.dtype\n    -> dtype('int32')\n    ```\n\n    tous les éléments sont du même type et de la même taille  \n    (ici des entiers signés codés sur 64 bits = 8 octets ou bien 32 bits = 4 octets)\n\n\n    l'attribut `numpy.ndarray.itemsize` donne le nombre d'octets d'un élément du tableau\n\n    ```python\n    mat.itemsize\n    -> 8 # chaque élément fait 8 octets dans le cas int64\n    ```\n\n\n    l'attribut `numpy.ndarray.nbytes`  donne le nombre d'octets total du tableau\n\n    ```python\n    mat.nbytes\n    -> 48 # 6 éléments de 8 octets chacun dans le cas int64\n    ```\n    ///\n    ")
    return

@app.cell
def _(np):
    # le code
    matrice2 = [[1, 2, 3], [4, 5, 6]]
    mat2 = np.array(matrice2)
    (mat2.dtype, mat2.itemsize, mat2.nbytes)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### taille, forme, dimension du tableau\n\n    /// admonition | →\n    ```python\n    matrice = [\n        [1, 2, 3],\n        [4, 5, 6]\n    ]\n    mat = np.array(matrice)\n    ```\n\n    l'attribut `numpy.ndarray.shape` donne la forme d'un tableau sous la forme d'un tuple\n\n    ```python\n    mat.shape\n    -> (2, 3) # 2 lignes et 3 colonnes\n    ```\n\n\n\n\n    l'attribut `numpy.ndarray.size` donne le nombre d'éléments du tableau\n\n    ```python\n\n    mat.size # mat.shape[0] * mat.shape[1]\n    -> 6\n    ```\n\n\n    l'attribut `numpy.ndarray.ndim` donne la dimension d'un tableau\n\n    ```python\n    mat.ndim # len(mat.shape)\n    -> 2\n    ```\n    ///\n    ")
    return

@app.cell
def _(mat):
    # le code
    print(mat.shape)
    print(mat.size, mat.shape[0] * mat.shape[1])
    print(mat.ndim, len(mat.shape))
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### création d'un tableau avec le type des éléments\n\n    /// admonition | →\n    on peut laisser `numpy` décider du type des éléments\n\n    ```python\n    matrice = [\n        [-128, -78, -32],\n        [17, 5, 127]\n    ]\n    mat = np.array(matrice)\n    mat.dtype\n    -> int64\n    ```\n\n\n    calculons l'élément minimum et l'élément maximum d'un tableau\n\n    ```python\n    mat.min(), mat.max()\n    -> -128 127\n    ```\n\n\n    Combien faut-il d'octets, au minimum, pour stocker des entiers entre `-128` et `127` ?  \n    un seul octet\n\n\n    Quel type d'entier dois-je utiliser ?\n\n\n    **rappel avec n bits**, on représente $2^n$ valeurs entières\n    - soit des entiers signés $\\in [ -2^{n-1}$, $2^{n-1}-1]$\n    - soit des entiers non signés $\\in [0, 2^n-1]$\n\n\n\n\n    on peut donc utiliser le type  \n\n    * `numpy.int8` pour le type des entiers signés sur 8 bits  \n      `256` valeurs de `-128` à `127`\n\n    * le type correspondant sera `numpy.int8` (entier signé sur 8 bits)\n\n\n\n    avec le paramètre `dtype` on indique, à la fonction `numpy.array`, le type des éléments\n\n    ```python\n    matrice = [\n        [-128, -78, -32],\n        [17, 5, 127]\n    ]\n    mat = np.array(matrice, dtype=np.int8)\n    mat.dtype\n    -> int8\n    ```\n\n\n    **trompons-nous** et demandons un type `numpy.uint8`  \n    - ancienne librairie `numpy` vous obéit et,  \n    si elle rencontre un problème avec une valeur: elle modifie la valeur !\n\n    ```python\n    mat = np.array(matrice, dtype=np.uint8)\n    mat\n    -> [[128, 178, 224], # ouh là là ! 128 = 256 - 128\n                         # (complément à 2)\n        [ 17,   5, 127]], dtype=uint8\n    ```\n    - nouvelle librairie `numpy`  \n       la conversion implicite n'est plus effectuée: le code échoue\n    ///\n    ")
    return

@app.cell
def _(np):
    # le code
    matrice3 = [[-128, -78, -32], [17, 5, 127]]
    mat3 = np.array(matrice3)
    print(mat3.min(), mat3.max())
    print(mat3.dtype)
    return

@app.cell
def _(np):
    # le code avec type
    matrice4 = [[-128, -78, -32], [17, 5, 127]]
    mat4 = np.array(matrice4, dtype=np.int8)
    mat4
    return (matrice4,)

@app.cell
def _(matrice4, np):
    # le code avec erreur
    try:
        mat5 = np.array(matrice4, dtype=np.uint8)
        # soit affichage du tableau avec les négatifs convertis implicitement par complément à 2
        # soit échec: "Python integer -128 out of bounds for uint8"
        mat5
    except OverflowError as e:
        print(e)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    **exercice**\n\n    1. créez un tableau pour stocker la matrice ci-dessous avec le plus petit type entier non signé\n\n    ```python\n    l = [[  0,   8,  34,   8],\n         [255,  61, 128, 254]]\n    ```\n    ')
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### modifier le type des éléments d'un tableau existant\n\n    /// admonition | →\n    la méthode `numpy.ndarray.astype` crée un nouveau tableau de la même forme que le tableau initial  \n    avec la taille indiquée pour les éléments\n\n    ```python\n    l = [[  0,   8,  34,   8],\n         [255,  61, 128, 254]]\n\n    mat = np.array(l)\n    mat1 = mat.astype(np.int8)\n    mat1\n    ```\n\n\n    `mat` et `mat1` ne partagent **pas** le tableau d'éléments sous-jacent  \n    `mat1` est **une copie indépendante** avec la nouvelle taille et les éventuelles conversions  \n    l'ancien `mat` existe toujours avec sa taille initiale\n    ///\n    ")
    return

@app.cell
def _(mat, np):
    # le code
    l2 = [[0, 8, 34, 8], [255, 61, 128, 254]]
    mat_non_typee = np.array(l2)
    print(mat_non_typee)
    mat_typee = mat.astype(np.int8)  # des conversions sont effectuées
    print(mat_typee)
    print(mat_non_typee)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## `numpy` calcule à taille constante\n\n    /// admonition | →\n    créons un tableau avec des éléments de type entier (type par défaut)\n\n    ```python\n    l = [-1, 2, 3]\n    mat = np.array(l)\n    mat\n        -> [-1, 2, 3]\n    ```\n\n    multiplions les éléments du tableau `mat` par `100`\n\n    ```python\n    mat*100\n    -> [-100,  200,   300]\n    ```\n\n    créons maintenant un tableau avec des éléments de type *entier signé sur 8 bits* (1 octet)\n\n    ```python\n    l = [-1, 2, 3]\n    mat = np.array(l, np.int8)\n    mat\n        -> [-1, 2, 3]\n    ```\n\n    multiplions les éléments du tableau `mat` par `100`\n\n    ```python\n    mat*100\n    -> [-100,  -56,   44]\n    ```\n\n    **et non pas** `[-100,  200,  300]`\n\n    le problème ?\n\n    * `numpy` ne modifie jamais la taille (le type) des éléments d'un tableau existant\n    * il calcule donc à taille-mémoire constante\n    * et convertit au-besoin les valeurs\n\n    pour éviter tout problème restez sur le type inféré par `numpy`  \n    vos entiers seront le plus souvent des `numpy.int64` ou des `numpy.int32`\n    ///\n    ")
    return

@app.cell
def _(np):
    # le code
    l6 = [-1, 2, 3]
    mat6 = np.array(l6)  # vous laissez numpy inférer le type
    print(mat6)
    print(mat6 * 100)
    print(mat6.dtype)
    return

@app.cell
def _(np):
    # le code
    l7 = [-1, 2, 3]
    mat7 = np.array(l7, np.int8)  # vous imposez le type
    print(mat7)
    print(mat7 * 100)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## autres constructeurs de  `numpy.ndarray`\n\n    /// admonition | →\n\n    | les méthodes | ce qu'elles font |\n    | --------------------------- | ------------------------------------------- |\n    | `numpy.zeros` | renvoie un ndarray rempli de *0.* (float) |\n    | `numpy.ones` | renvoie un ndarray rempli de *1.* (float) |\n    | `numpy.empty` | renvoie un ndarray vide i.e. sans initialiser ses éléments |\n    | | |\n    | `numpy.arange` | tableau de valeurs régulièrement espacées|\n    | `numpy.linspace` |  tableau de valeurs régulièrement espacées|\n    | | |\n    | `numpy.random.randint` | entiers aléatoirement générés |\n    | `numpy.random.randn` | flottants aléatoirement générés |\n    ///\n\n    ---\n\n    ### tableau de zéros `numpy.zeros`\n\n    /// admonition | →\n\n    vous devez indiquer à la fonction `numpy.zeros` la forme du tableau\n\n\n    ```python\n    zorro = np.zeros(shape=(4, 5))\n    zorro\n    -> [[0., 0., 0., 0., 0.],\n        [0., 0., 0., 0., 0.],\n        [0., 0., 0., 0., 0.],\n        [0., 0., 0., 0., 0.]]\n    ```\n\n\n    on peut donner d'autres paramètres, comme le type des éléments...\n\n    ```python\n    zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)\n    zorro1\n    -> [[0, 0, 0, 0, 0],\n        [0, 0, 0, 0, 0],\n        [0, 0, 0, 0, 0],\n        [0, 0, 0, 0, 0]\n    ```\n    ///\n    ")
    return

@app.cell
def _(np):
    # le code
    zorro = np.zeros(shape=(4, 5))
    zorro
    return

@app.cell
def _(np):
    # le second code
    zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
    zorro1
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    /// admonition | exercice\n\n    * affichez le type des éléments de `zorro`\n\n    * créez le tableau multi-dimensionnel des entiers positifs 8 bits suivant\n\n    ```python\n    array([[[0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0]],\n\n           [[0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0],\n            [0, 0, 0]]])\n    ```\n    ///\n    ')
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### tableau non-initialisé `numpy.empty`\n\n    /// admonition | →\n\n    la fonction `numpy.empty`\n\n\n    **utilité ?**\n\n    * ne pas perdre de temps à initialiser inutilement un tableau\n    * quand vous n'allez jamais utiliser la valeur initiale des éléments\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    **exercice**\n\n    1. créez un tableau de forme `(3, 5)` de valeurs non-initialisées  \n       de type entiers signés sur 8 bits\n    1. affichez-le\n    1. que contient-il ?\n    ')
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### tableau de valeurs régulièrement espacées\n\n    /// admonition | →\n\n    `numpy.arange(from, to, step)`\n\n    * ressemble un peu au `range` de Python\n    * nombres équidistants de `step` sur l'intervalle `[from, to[`  \n    * en général `step` est entier (mais pas obligatoire)\n\n    `numpy.linspace(from-included, to-included, n)`\n\n    * `n` réels régulièrement espacés dans un intervalle\n    * la valeur supérieure de l'intervalle **est** incluse\n    ///\n    ")
    return

@app.cell
def _(np):
    # exemple avec arange
    # comme avec le range() de Python
    # la deuxième borne est exclue
    np.arange(0, 5)
    return

@app.cell
def _(np):
    # exemple avec linspace
    from matplotlib import pyplot as plt
    X = np.linspace(-np.pi, np.pi, 30)
    Y = np.sin(X)
    plt.plot(X, Y)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### générateur de valeurs aléatoires entières\n\n    /// admonition | →\n\n    `numpy.random.randint` permet de tirer un nombre entier aléatoirement entre deux bornes  \n    (la seconde est exclue)\n    ```python\n    borne_inf = 10\n    borne_sup = 20\n    np.random.randint(borne_inf, borne_sup)\n    ```\n\n    passez lui le paramètre `size` (et non pas `shape`)\n    pour générer un tableau-multi-dimensionnel d'une forme donnée\n\n    ```python\n    np.random.randint(10, 20, size=(2, 3, 5))\n    ->\n    array([[[11, 18, 14, 19, 16],\n            [17, 14, 15, 11, 11],\n            [13, 17, 11, 10, 13]],\n\n           [[12, 14, 10, 13, 17],\n            [11, 17, 18, 19, 18],\n            [19, 15, 10, 17, 18]]])\n    ```\n    ///\n    ")
    return

@app.cell
def _(np):
    # le code
    borne_inf = 10
    borne_sup = 20
    np.random.randint(borne_inf, borne_sup)
    return

@app.cell
def _(np):
    # le code
    np.random.randint(10, 20, size=(2, 3, 5))
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    ### générateur de valeurs aléatoires réelles\n\n    /// admonition | →\n\n    `numpy.random.randn` renvoie un échantillon  \n    de la loi normale centrée-réduite (moyenne 0, écart-type 1)\n\n    ```python\n    np.random.randn()\n    -> 0.19176811586596798\n    ```\n\n\n    `numpy.random.randn(d0, ..., dn)` génére un tableau de `shape` $(d_1, ..., d_n)$\n\n    ```python\n    np.random.randn(2, 3, 1)\n    ->\n    array([[[-0.91543618],\n            [-2.12493972],\n            [ 0.93155056]],\n\n           [[-0.17198904],\n            [-0.69164236],\n            [-0.43321452]]])\n    ```\n\n\n    la librairie `numpy.random`\n\n    * contient plus de fonctionnalités pour le calcul scientifique que `random.random`\n    * sait manipuler efficacement des tableaux `numpy.ndarray`\n    ///\n    ')
    return

@app.cell
def _(np):
    # le code
    np.random.rand()
    return

@app.cell
def _(np):
    # le code
    np.random.randn(2, 3, 1)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    **exercice** génération aléatoire et affichage *couleur*\n\n\n    avec la fonction `numpy.random.randint`\n    dont l'aide est obtenue en tapant\n    ```python\n    np.random.randint?\n    ```\n\n    1. construisez une image de `10 x 10` pixels en format RBG  \n    i.e. chaque pixel est composé de 3 valeurs entières entre 0 et 255 inclus\n\n\n    2. affichez l'image avec `plt.imshow`\n    ")
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## comparaison des temps de création tableaux\n\n    (avancé)\n\n    /// admonition | →\n    `timeit` permet d'évaluer le temps d'exécution d'une fonction, en secondes\n\n    ```python\n    from timeit import timeit\n\n    def f():\n        return 1 + 1\n\n    timeit(f, number=1000)\n    -> 0.012112832977436483 # temps en s pour 1000 itérations\n    ```\n    ///\n    ")
    return

@app.cell
def _():
    # le code
    from timeit import timeit, Timer
    return (timeit,)

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    **exercice**\n\n    comparez les temps d'exécution de\n\n    * la création d'un `numpy.ndarray` à partir d'une liste Python comportant 1000 floats initialisés à 0  \n    ne pas mettre la création de la liste Python dans le calcul du temps\n\n    * la création d'un `numpy.ndarray` de 1000 éléments initialisés à 0\n\n    * la création d'un `numpy.ndarray` de 1000 éléments non-initialisés\n\n    * lequel est le plus rapide ?\n    ")
    return

@app.cell
def _():
    # votre code ici
    return

@app.cell
def _(np, timeit):
    from random import randint

    def create_from_list():
        big_list = [0 for _ in range(1000)]
        return np.array(big_list)
    timeit(create_from_list, number=1000)
    return

@app.cell
def _(np, timeit):

    def create_zeros():
        return np.zeros(10000)
    timeit(create_zeros, number=1000)
    return

@app.cell
def _(np, timeit):

    def create_empty():
        return np.empty(10000)
    timeit(create_empty, number=1000)
    return

@app.cell
def _():
    return
if __name__ == '__main__':
    app.run()