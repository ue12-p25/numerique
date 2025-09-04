---
jupytext:
  custom_cell_magics: kql
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
  pygments_lexer: ipython3
  nbconvert_exporter: python
---

# exploration interactive

+++

````{admonition} →

pour finir je vous signale un outil commode pour une exploration un peu plus interactive de vos données depuis le notebook

````

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## le package `itables`

+++

le plus simple c'est de voir un exemple; naturellement il faut avoir d'abord installé le package `itables`

```bash
pip install itables
```

ensuite depuis le notebook il faut initialiser le mode interactif; c'est un peu comme le `%matplotlib ipympl` si on veut; ça se présenterait comme ceci

```python
# pour activer itables depuis un notebook
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)
```

```{code-cell} ipython3
# on ne le fait pas pour la sortie HTML parce que ça ne marche pas du tout dans ce contexte-là
# mais si vous lisez ceci depuis un notebook vous n'avez qu'à décommenter ces deux lignes

# from itables import init_notebook_mode
# init_notebook_mode(all_interactive=True)
```

et de là on peut afficher les dataframes comme d'habitude, et explorer les données interactivement:

- choisir une pagination
- trier par colonne
- faire des recherches

```{code-cell} ipython3
# je vais prendre le titanic

df = pd.read_csv('data/titanic.csv')
```

et maintenant chaque fois que j'affiche une dataframe j'obtiens ce genre de représentation

```{image} media/itables.png
```

```{code-cell} ipython3
# dans le HTML ça ne donne rien mais vous avez un aperçu statique ci-dessus

df
```

## voir aussi

un blog sur cet outil ici  
<https://blog.jupyter.org/make-your-pandas-or-polars-dataframes-interactive-with-itables-2-0-c64e75468fe6>
