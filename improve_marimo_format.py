#!/usr/bin/env python3
"""
Script pour améliorer le format des notebooks Marimo
en ajoutant les décorateurs @mo.cell appropriés
"""

import re
import os
from pathlib import Path

def improve_marimo_format(file_path):
    """Améliore le format d'un fichier Marimo"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajouter l'import de marimo au début
    if 'import marimo' not in content:
        content = "import marimo as mo\n\n" + content
    
    # Trouver les cellules de code (sections commençant par #)
    lines = content.split('\n')
    improved_lines = []
    cell_count = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Si c'est un commentaire de cellule (commence par # et contient du texte)
        if (line.startswith('# ') and 
            len(line) > 2 and 
            not line.startswith('# import') and
            not line.startswith('# Cellule')):
            
            # Créer une fonction de cellule
            cell_count += 1
            cell_name = f"cell_{cell_count}"
            
            # Extraire le commentaire
            comment = line[2:].strip()
            
            # Trouver le code de la cellule
            cell_code = []
            i += 1
            while i < len(lines) and not (lines[i].startswith('# ') and len(lines[i]) > 2):
                cell_code.append(lines[i])
                i += 1
            
            # Nettoyer le code
            cell_code = '\n'.join(cell_code).strip()
            
            # Créer la cellule Marimo
            improved_lines.append(f'@mo.cell')
            improved_lines.append(f'def {cell_name}():')
            improved_lines.append(f'    """{comment}"""')
            if cell_code:
                # Indenter le code
                indented_code = '\n'.join('    ' + l if l.strip() else l for l in cell_code.split('\n'))
                improved_lines.append(indented_code)
            else:
                improved_lines.append('    pass')
            improved_lines.append('')
            
        else:
            improved_lines.append(line)
            i += 1
    
    # Écrire le fichier amélioré
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(improved_lines))
    
    print(f"✅ Amélioré: {file_path} ({cell_count} cellules créées)")

def main():
    """Fonction principale"""
    
    marimo_dir = Path("marimo")
    
    # Trouver tous les fichiers .py (sauf les scripts de conversion)
    py_files = [f for f in marimo_dir.glob("*.py") 
                if f.name not in ["convert_myst_to_marimo.py", 
                                 "convert_myst_to_marimo_improved.py",
                                 "improve_marimo_format.py",
                                 "start_marimo.py",
                                 "example_marimo_notebook.py"]]
    
    print(f"Amélioration du format de {len(py_files)} fichiers Marimo...")
    
    for file_path in py_files:
        try:
            improve_marimo_format(file_path)
        except Exception as e:
            print(f"❌ Erreur lors de l'amélioration de {file_path}: {e}")
    
    print("\n🎉 Amélioration terminée!")
    print("\n📝 Note: Les fichiers ont été convertis en format Marimo avec des cellules réactives.")
    print("   Vous pouvez maintenant utiliser `marimo edit` pour les ouvrir.")

if __name__ == "__main__":
    main() 