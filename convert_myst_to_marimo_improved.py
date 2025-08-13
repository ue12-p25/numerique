#!/usr/bin/env python3
"""
Script amélioré pour convertir les notebooks MyST vers le format Marimo
"""

import os
import re
import glob
from pathlib import Path

def clean_markdown_content(content):
    """Nettoie le contenu markdown pour Marimo"""
    # Supprimer les métadonnées YAML
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    # Supprimer les cellules de code pour garder seulement le markdown
    content = re.sub(r'```\{code-cell\} ipython3\s*\n.*?\n```', '', content, flags=re.DOTALL)
    
    # Supprimer les balises MyST spécifiques
    content = re.sub(r'\+\+\+.*?\+\+\+', '', content, flags=re.DOTALL)
    content = re.sub(r'```\{admonition\}.*?\n(.*?)\n```', r'**Note**: \1', content, flags=re.DOTALL)
    content = re.sub(r'```\{.*?\}\n(.*?)\n```', r'\1', content, flags=re.DOTALL)
    
    # Nettoyer les lignes vides multiples
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def extract_code_cells(content):
    """Extrait les cellules de code du contenu MyST"""
    code_cells = []
    
    # Pattern pour les cellules de code MyST
    code_pattern = r'```\{code-cell\} ipython3\s*\n(.*?)\n```'
    matches = re.findall(code_pattern, content, re.DOTALL)
    
    for i, match in enumerate(matches):
        code = match.strip()
        if code:
            code_cells.append(code)
    
    return code_cells

def convert_to_marimo(myst_file_path, output_dir):
    """Convertit un fichier MyST vers le format Marimo amélioré"""
    
    with open(myst_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire le titre du fichier
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(myst_file_path).stem
    
    # Extraire les cellules de code
    code_cells = extract_code_cells(content)
    
    # Extraire et nettoyer le contenu markdown
    markdown_content = clean_markdown_content(content)
    
    # Créer le contenu Marimo avec un format plus propre
    marimo_content = f"""# {title}

{markdown_content}

"""
    
    # Ajouter les cellules de code avec des commentaires descriptifs
    for i, code in enumerate(code_cells):
        # Essayer d'extraire un commentaire descriptif du code
        first_line = code.split('\n')[0].strip()
        if first_line.startswith('#'):
            comment = first_line[1:].strip()
        else:
            comment = f"Cellule de code {i+1}"
        
        marimo_content += f"""
# {comment}
{code}

"""
    
    # Créer le nom du fichier de sortie
    output_filename = Path(myst_file_path).stem.replace('-nb', '') + '.py'
    output_path = Path(output_dir) / output_filename
    
    # Écrire le fichier Marimo
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(marimo_content)
    
    print(f"Converti: {myst_file_path} -> {output_path}")
    return output_path

def create_marimo_app_file(marimo_dir, converted_files):
    """Crée un fichier app.py principal pour Marimo"""
    
    app_content = """# Application Marimo - Python Numérique
# 
# Ce fichier permet de naviguer entre tous les notebooks du cours

import marimo as mo

# Liste des notebooks disponibles
notebooks = {
    "Introduction": "0-00-intro.py",
    "NumPy - Introduction": "1-01-numpy-introduction.py", 
    "NumPy - Arrays": "1-02-numpy-array.py",
    "NumPy - Mémoire": "1-03-numpy-memory.py",
    "NumPy - Vectorisation": "1-04-numpy-vectorization.py",
    "NumPy - Indexation": "1-05-numpy-indexing-slicing.py",
    "NumPy - Agrégation": "1-07-numpy-aggregate.py",
    "NumPy - Broadcasting": "1-08-numpy-broadcast.py",
    "Pandas - Lecture CSV": "2-01-pandas-read-csv.py",
    "Pandas - Conditions": "2-02-pandas-condition.py",
    "Pandas - Indexation": "2-03-pandas-indexing-slicing.py",
    "Pandas - Group By": "2-07-pandas-group-by.py",
    "Matplotlib - Introduction": "3-01-matplotlib-intro.py",
    "Seaborn - Introduction": "3-05-seaborn-intro.py",
    "Python - Tour d'horizon": "5-01-un-tour-de-python.py",
    "Python - Fonctions": "5-03-fonctions.py",
    "Python - Classes": "5-10-classes.py"
}

# Interface de navigation
@mo.cell
def navigation():
    return mo.md(f\"\"\"
# Python Numérique - Navigation
    
Sélectionnez un notebook à ouvrir:
    
{chr(10).join([f"- [{title}]({filename})" for title, filename in notebooks.items()])}
    
## Instructions:
1. Cliquez sur un lien ci-dessus pour ouvrir le notebook
2. Ou utilisez `marimo edit nom_du_fichier.py` dans le terminal
3. Ou ouvrez directement un fichier .py dans l'éditeur Marimo
\"\"\")

@mo.cell  
def info():
    return mo.md(\"\"\"
## À propos de cette conversion
    
Ces notebooks ont été convertis automatiquement du format MyST vers Marimo.
    
### Différences avec l'original:
- Format Python pur (.py) au lieu de Markdown
- Cellules de code séparées par des commentaires
- Navigation simplifiée
    
### Pour utiliser:
- `marimo edit` pour lancer l'éditeur
- `marimo run nom_du_fichier.py` pour exécuter un notebook
- `marimo serve` pour servir l'application web
\"\"\")
"""
    
    app_path = marimo_dir / "app.py"
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(app_content)
    
    print(f"Application Marimo créée: {app_path}")

def main():
    """Fonction principale de conversion améliorée"""
    
    # Chemins
    notebooks_dir = Path("notebooks")
    marimo_dir = Path("marimo")
    
    # Créer le dossier marimo s'il n'existe pas
    marimo_dir.mkdir(exist_ok=True)
    
    # Trouver tous les fichiers MyST
    myst_files = list(notebooks_dir.glob("*-nb.md"))
    
    print(f"Trouvé {len(myst_files)} fichiers MyST à convertir...")
    
    # Convertir chaque fichier
    converted_files = []
    for myst_file in myst_files:
        try:
            output_path = convert_to_marimo(myst_file, marimo_dir)
            converted_files.append(output_path)
        except Exception as e:
            print(f"Erreur lors de la conversion de {myst_file}: {e}")
    
    print(f"\nConversion terminée! {len(converted_files)} fichiers convertis dans le dossier 'marimo'")
    
    # Créer l'application Marimo principale
    create_marimo_app_file(marimo_dir, converted_files)
    
    # Créer un fichier index amélioré
    create_improved_index(marimo_dir, converted_files)

def create_improved_index(marimo_dir, converted_files):
    """Crée un fichier index amélioré pour Marimo"""
    
    # Organiser les fichiers par section
    sections = {
        "Introduction": [],
        "NumPy - Calcul scientifique": [],
        "Pandas - Traitement de données": [],
        "Matplotlib - Visualisation": [],
        "Python de base": [],
        "Tests et exercices": []
    }
    
    for file_path in converted_files:
        filename = file_path.name
        if filename.startswith("0-"):
            sections["Introduction"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
        elif filename.startswith("1-"):
            sections["NumPy - Calcul scientifique"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
        elif filename.startswith("2-"):
            sections["Pandas - Traitement de données"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
        elif filename.startswith("3-"):
            sections["Matplotlib - Visualisation"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
        elif filename.startswith("5-"):
            sections["Python de base"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
        else:
            sections["Tests et exercices"].append((filename, filename.replace('.py', '').replace('-', ' ').title()))
    
    index_content = """# Python Numérique - Notebooks Marimo

Ce dossier contient tous les notebooks du cours convertis au format Marimo.

## 🚀 Démarrage rapide

```bash
# Installer Marimo
pip install marimo

# Lancer l'éditeur
marimo edit

# Ou lancer l'application principale
marimo edit app.py

# Ou exécuter un notebook spécifique
marimo run 1-01-numpy-introduction.py
```

## 📚 Structure du cours

"""
    
    for section_name, files in sections.items():
        if files:
            index_content += f"\n### {section_name}\n\n"
            for filename, title in sorted(files):
                index_content += f"- [{title}]({filename})\n"
    
    index_content += """

## 🔧 Utilisation avec Marimo

### Commandes utiles:
- `marimo edit` - Lancer l'éditeur interactif
- `marimo run fichier.py` - Exécuter un notebook
- `marimo serve` - Servir l'application web
- `marimo watch fichier.py` - Surveiller les changements

### Fonctionnalités Marimo:
- ⚡ Exécution réactive des cellules
- 🔄 Recalcul automatique lors des modifications
- 📊 Visualisations interactives
- 🎨 Interface moderne et intuitive

## 📁 Fichiers importants

- `app.py` - Application principale avec navigation
- `README.md` - Ce fichier d'aide
- `requirements.txt` - Dépendances Python (dans le dossier parent)

## 🎯 Conseils d'utilisation

1. Commencez par `0-00-intro.py` pour l'introduction
2. Suivez l'ordre numérique des sections
3. Utilisez `app.py` pour naviguer facilement
4. Les cellules se recalculent automatiquement

## 🔗 Liens utiles

- [Documentation Marimo](https://docs.marimo.io/)
- [Cours original](https://ue12-p25.github.io/numerique/)
- [GitHub du projet](https://github.com/ue12-p25/numerique)
"""
    
    index_path = marimo_dir / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Index amélioré créé: {index_path}")

if __name__ == "__main__":
    main() 