import marimo
__generated_with = '0.14.13'
app = marimo.App(width='medium')

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    # Python numérique\n    Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    ## contenu de ce module: numpy, pandas et matplotlib\n\n    le corpus principal porte sur:\n\n    * **`numpy`**: le tableau homogène , pour le calcul scientifique;\n    * **`pandas`**: la dataframe (similaire à une table SQL), pour le traitement de données;\n    * **`matplotlib`**: pour les affichages de données scientifiques.\n    * (et aussi un module optionnel, qui contient des rappels essentiels sur le Python dit "de base")\n    ')
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("\n    ## mode d'emploi / rappels\n\n    pour être sûr que vous avez tout ce qu'il faut pour travailler  \n    on suppose [les installations faites lors du cours d'introduction](https://ue12-p25.github.io/intro/1-1-installations/) (bash - vscode - conda - jupyter - jupytext - git)\n    ")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md('\n    ### convention (sachez à qui vous parlez)\n\n    lorsque c\'est ambigu, on préfixera :\n\n    /// admonition | dans le terminal\n    parfois on préfixe la commande à taper **avec un `$`** pour indiquer que ça s\'adresse au terminal\n\n    ```bash\n    $ python\n    ```\n\n    dans ce cas **attention** à ne pas copier-coller le signe `$` !\n    ///\n\n    /// admonition | dans l\'interpréteur Python\n    si on préfixe **avec `>>>`** c\'est pour indiquer que la commande est du Python - on peut alors la copier-coller dans `python` ou `ipython` ou `jupyter` \n\n    ```python\n    >>> a = 100\n    ```\n\n    et pareil il ne faut pas copier le `>>>` évidemment\n    ///\n\n\n    ça va sans dire, et mieux encore en le disant, mais si vous tapez une commande python dans le terminal - ou inversement - évidemment ça va mal se passer...\n\n\n    ### obtenir le cours\n\n    si tout cela est bien en place il ne vous reste plus alors que deux choses à faire:\n\n    - cloner ce dépôt\n      /// admonition | on fait comment déjà ?\n      ```bash\n      git clone git@github.com:ue12-p25/numerique.git\n      ```\n      ///\n  \n    - installer les dépendances\n      /// admonition | on fait comment déjà ?\n      ```bash\n      pip install -r requirements.txt\n      ```\n      ///\n\n\n    ### lancer Python\n\n    les notebooks du cours se trouvent .. dans le dossier `notebooks`\n\n    1. principalement on lira les notebooks avec jupyter avec (ne pas taper le `$` hein!)   \n       `$ jupyter lab`\n    1. exécuter un programme déjà fait  \n      `$ python monprogramme.py`\n    1. lancer un interpréteur interactif  \n      `$ python`  \n      ou encore mieux  \n      `$ ipython`\n\n\n    ### vidéo d\'illustration\n\n    ces usages ont été vus dans le cours d\'introduction, et [dans la vidéo associée](https://youtu.be/i_ZcP7iNw-U)\n\n\n    ## environnements virtuels\n\n    enfin, et pour les geeks:\n\n    lorsqu\'on travaille sur plusieurs projets, il est possible de créer un environnement virtuel afin d\'isoler les dépendances installées: cela évitera qu\'une modification apportée sur un projet impacte les autres projets par effet de bord.\n\n    si vous voulez essayer d\'utiliser ce système, [voyez cette page dans le cours d\'introduction](https://ue12-p25.github.io/intro/3-3-virtual-envs/)\n\n    /// attention | Attention !\n    Comme indiqué dans cette page, il est **crucial** de s\'assurer que votre "prompt" bash (ce qui est affiché avant le `$` lorsque vous avez la main dans le terminal) vous indique en permanence dans quel environnement vous vous trouvez.\n    ///\n\n    ')
    return
if __name__ == '__main__':
    app.run()