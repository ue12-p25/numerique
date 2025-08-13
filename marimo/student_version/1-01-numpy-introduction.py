import marimo
__generated_with = '0.14.13'
app = marimo.App(width='medium')

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    # Python-numérique - introduction\n\n    /// admonition | Rappel\n\n    **Note**: pour un rendu optimal, pensez à installer les *requirements* du cours avec\n\n    ```bash\n    pip install -r requirements.txt\n    ```\n    ///\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## contenu de ce notebook\n\n    (sauter si déjà acquis)\n\n    /// admonition | →\n\n    comprendre que des objets qui semblent aussi différents qu'une matrice, une table de mesures hétérogènes, une série temporelle, une image...\n\n    sont en fait une même structure de données\n\n    que celle-ci n'existe pas en `python`\n\n    d'où le recours à la librairie `numpy`\n    ////\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## objectifs de Python-numérique\n\n    /// admonition | →\n\n    vous êtes désormais capables de lire et d'écrire du code **python simple**\n\n    vous savez le mettre en œuvre dans un **notebook**\n\n    nous allons maintenant aborder le cours de **Python-numérique**\n\n    il s'agit des fonctionnalités de base de **data-science**\n\n    issues de librairies python comme `numpy`, `pandas`, `matplotlib.pyplot`...\n\n\n    commençons par **importer** ces librairies dans Python\n\n    ```python\n    import numpy as np\n    import pandas as pd\n    from matplotlib import pyplot as plt\n    ```\n\n    il peut être nécessaire de les installer avec `pip install numpy pandas matplotlib`  \n    (ou `%pip install numpy pandas matplotlib` dans une cellule de vos notebooks)\n\n    et regarder la version de ces librairies\n\n    ```python\n    np.__version__\n    pd.__version__\n    ```\n    ///\n    ")
    return

@app.cell
def _():
    # manière classique d'importer les librairies de data-science
    # NB: la toute première fois qu'on importe une librairie 
    # après un pip install, ça peut être un peu long...
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    return (np, pd)

@app.cell
def _(np, pd):
    # vérifier les versions de ces librairies
    print(f'numpy version {np.__version__}')
    print(f'pandas version {pd.__version__}')
    import matplotlib as mpl  # la version de matplotlib
    print(f'matplotlib version {mpl.__version__}')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## les données\n\n\n    /// admonition | →\n\n    qui dit data-science dit **données**\n\n    données qui seront **manipulées** dans des programmes Python\n\n    pour les manipuler, il faut tout d'abord les **lire** et les **stocker** en mémoire\n\n    en data-science on peut avoir de **très grandes quantités** de données\n\n    * le stockage des données en mémoire doit être **optimisé**  \n      (en *espace mémoire** et en **temps d'accès** à cet espace mémoire)\n\n    * afin que les calculs prennent le **moins de temps possible**\n\n    mais avant de parler de cela, regardons les différentes formes de données que nous voulons manipuler :\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## différents formats de données\n\n    ### plusieurs exemples\n\n    /// admonition | →\n\n    1. des **vecteurs** et **matrices** numériques classiques\n\n    ![](public/matrice.png)\n\n    ------\n\n    2. des **tables** d'observations où\n\n    * chaque **observation** (*lignes*)...\n\n    * ...est décrite par une ou plusieurs **mesures** (*colonnes*)\n\n    * la première ligne indique, dans cet exemple, les noms des colonnes\n\n    Quelles sont ces différentes **mesures** ?  \n    certaines, *SibSp* et *Parch*, sont impossibles à comprendre sans les **meta-data** de la table\n\n    ![](public/titanic.png)\n\n    -----\n\n    3. des **séries temporelles**\n\n    * on affiche ici les valeurs cumulées des infections au covid de janvier à août 2020 en France\n\n    ![](public/corona-france.jpg)\n    <https://www.data.gouv.fr/fr/datasets/coronavirus-covid19-evolution-par-pays-et-dans-le-monde-maj-quotidienne/>\n\n    -----\n\n    4. des images\n\n    ![](public/les-mines.jpg)\n\n    -----\n\n    5. des sons (musique, voix)  \n\n    -----\n\n    6. **etc.**\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### la matrice\n\n    /// admonition | →\n\n    pour la matrice, on peut imaginer une représentation Python comme celle-là\n\n    ```python\n    matrice = [\n        [1, 2, 3, 4, 5],\n        [6, 7, 8, 9, 10],\n        [11, 12, 13, 14, 15],\n        [16, 17, 18, 19, 20]\n    ]\n    ```\n\n    mais pour transposer la sous-matrice ... c'est moins facile  \n    et on ne va pas coder une fonction qui doit déjà exister !\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    ### table d\'observations\n\n    /// admonition | →\n\n    la table (des passagers du Titanic), est donnée dans un fichier, voici les 5 premières lignes\n\n    ```\n    PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked\n    1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S\n    2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C\n    3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S\n    4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S\n    ...\n    ```\n\n    que remarquez-vous ?\n\n    * en première ligne - les noms des mesures (les colonnes de la table)\n\n\n    * puis une observation par ligne\n\n\n    * les valeurs des mesures sont séparées par des `\',\'`\n\n\n    * certaines valeurs sont manquantes `\',,\'`\n\n\n    * on voit des entiers, des réels (format US donc la virgule des décimales\n    est représentée par un `.`)...\n\n\n    * ce format est donc un tableau en 2 dimensions de données hétérogènes  \n    (des réels, des chaînes de caractères, des entiers...)\n\n    ce format s\'appelle un `CSV` pour **C**omma-**S**eparated-**V**alues  \n    (fichier `data/titanic.csv`)\n    ///\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### la série temporelle\n\n    /// admonition | →\n\n    pour la série, on a aussi un fichier `CSV`, `data/corona-par-pays.csv`\n\n    ```\n    #Vous pouvez utiliser ces données sans problème\n    #une référence à https://coronavirus.politologue.co sera appréciable\n    Date;Pays;Infections;Deces;Guerisons;TauxDeces;TauxGuerison;TauxInfection\n    2020-08-17;Andorre;989;53;863;5.36;87.26;7.38\n    2020-08-17;Émirats Arabes Unis;64312;364;57694;0.57;89.71;9.72\n    2020-08-17;Afghanistan;37596;1375;27166;3.66;72.26;24.09\n    ...\n    ```\n    que remarquez-vous ?\n\n    * il ressemble au précédent\n\n\n    * on a deux lignes de commentaires (commençant par `#`)\n\n\n    * les noms des colonnes sont dans la troisième ligne  \n\n\n    * les deux premières mesures sont la date et le pays\n    puis on voit 6 mesures reliées au covid\n\n\n    * dans chaque ligne, on a la valeur de ces 6 mesures pour une date et un pays\n\n\n    * les dates ont le format `year-month-day`\n\n\n\n    * les séparateurs sont des `';'`\n\n\n    * les réels sont en format US\n\n\n    * ce format est aussi une table en 2 dimensions de données hétérogènes  \n    (dates, identificateurs, réels...)\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### l'image\n\n    /// admonition | →\n\n    pour l'image on a le fichier, en format `jpg`, `media/les-mines.jpg`\n\n    on sait que l'image est constituée de $533$ lignes et $800$ colonnes de pixels\n\n    et que chaque pixel est représenté par ses 3 valeurs `RGB` RedGreenBlue\n\n    voici les valeurs des premiers pixels de l'image\n\n    ```python\n    [[[150, 106, 33], [143, 105, 0], [ 58, 31, 4], [135, 45, 36], [229, 131, 84], [153, 158, 200]...    ]]\n    ```\n\n    on devine les trois dimensions (les trois `[[[`)\n\n    les valeurs des pixels RGB\n\n    * ici, des entiers prenant 256 valeurs\n    * $2^8$ valeurs de 0 à 255  \n    * pour les stocker il suffit donc d'entiers non-signés sur 8 bits  \n      (0 est `00000000` et 255 est `11111111`)\n\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## représenter ces données en mémoire\n\n    /// admonition | →\n\n    ### notre problème\n\n    représenter ces données dans la mémoire de l'ordinateur afin de les analyser\n\n    * ces données semblent assez différentes : matrice, tables de passagers, série temporelle, image...  \n\n    * nous souhaitons pourtant leur appliquer le même genre de fonctions\n\n    comme un `max` ou un `min`\n\n    * le passager le plus agé ou le plus jeune du titanic\n    * les pixels les plus clairs ou les plus foncés\n    * les minima ou maxima des lignes de la matrice\n\n\n    comme des `plot` (boxplot, histogramme,  plot 2D...)\n\n    comme de petites statistiques (moyenne, écart-type...)\n\n    il faut leur trouver une **forme commune**\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### ces données sont des tableaux multi-dimensionnels\n\n    /// admonition | →\n\n    on a des tableaux **homogènes**\n\n    * la matrice est un tableau d'entiers, en 2 dimensions, de taille $5 \\times 4$\n\n\n    * l'image est un tableau d'entiers, en 3 dimensions, de taille $533 \\times 800 \\times 3$\n\n    et des tableaux **hétérogènes**\n\n    * la table des passagers du Titanic est un tableau 2D de taille $891 \\times 9$\n\n\n    * la série temporelle est un tableau 2D de taille $33342 \\times 8$\n\n\n    * les colonnes sont des séries de valeurs de même type\n\n\n    * toutes  les colonnes n'ont pas le même type\n    ///\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ### pas de type Python adéquat\n\n    /// admonition | →\n\n    **structures de ces données ?**\n\n    Python ne possède pas de type adapté à ces tableaux multi-dimensionnels\n\n    depuis 2006, une librairie numérique `numpy` est *développée* pour cela\n\n    non intégrée au core-langage Python par souci de maintenance du code\n\n    elle est LA librairie numérique incontournable de Python\n\n    elle étend Python avec la manipulation de tableaux multi-dimensionnels\n\n    c'est une bibliothèque libre et open source\n\n    `SciPy` (ScientificPython) pour le calcul scientifique est fondée sur `numpy`\n    ///\n    ")
    return
if __name__ == '__main__':
    app.run()