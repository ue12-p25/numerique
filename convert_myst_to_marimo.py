#!/usr/bin/env python3
"""
Script pour convertir les notebooks MyST vers le format Marimo
"""

import os
import re
import glob
from pathlib import Path

def extract_code_cells(content):
    """Extrait les cellules de code du contenu MyST"""
    code_cells = []
    
    # Pattern pour les cellules de code MyST
    code_pattern = r'```\{code-cell\} ipython3\s*\n(.*?)\n```'
    matches = re.findall(code_pattern, content, re.DOTALL)
    
    for i, match in enumerate(matches):
        code_cells.append(match.strip())
    
    return code_cells

def extract_markdown_sections(content):
    """Extrait les sections markdown du contenu MyST"""
    # Supprimer les métadonnées YAML
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    # Supprimer les cellules de code pour garder seulement le markdown
    content = re.sub(r'```\{code-cell\} ipython3\s*\n.*?\n```', '', content, flags=re.DOTALL)
    
    # Nettoyer les lignes vides multiples
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

def convert_to_marimo(myst_file_path, output_dir):
    """Convertit un fichier MyST vers le format Marimo"""
    
    with open(myst_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraire le titre du fichier
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(myst_file_path).stem
    
    # Extraire les cellules de code
    code_cells = extract_code_cells(content)
    
    # Extraire le contenu markdown
    markdown_content = extract_markdown_sections(content)
    
    # Créer le contenu Marimo
    marimo_content = f"""# {title}

{markdown_content}

"""
    
    # Ajouter les cellules de code
    for i, code in enumerate(code_cells):
        marimo_content += f"""
# Cellule {i+1}
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

def main():
    """Fonction principale de conversion"""
    
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
    
    # Créer un fichier index pour Marimo
    create_marimo_index(marimo_dir, converted_files)

def create_marimo_index(marimo_dir, converted_files):
    """Crée un fichier index pour Marimo"""
    
    index_content = """# Index des notebooks Python numérique

Ce dossier contient les notebooks convertis au format Marimo.

## Liste des notebooks disponibles:

"""
    
    for file_path in sorted(converted_files):
        filename = file_path.name
        title = filename.replace('.py', '').replace('_', ' ').title()
        index_content += f"- [{title}]({filename})\n"
    
    index_content += """

## Pour utiliser ces notebooks avec Marimo:

1. Installer Marimo: `pip install marimo`
2. Lancer Marimo: `marimo edit`
3. Ouvrir un des fichiers .py dans l'éditeur

## Structure des notebooks:

- **Section 1**: NumPy - Calcul scientifique
- **Section 2**: Pandas - Traitement de données  
- **Section 3**: Matplotlib - Visualisation
- **Section 4**: Cheatsheets
- **Section 5**: Python de base
"""
    
    index_path = marimo_dir / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Fichier index créé: {index_path}")

if __name__ == "__main__":
    main() 