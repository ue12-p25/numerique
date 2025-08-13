#!/usr/bin/env python3

import ast
import ast_comments


# list all marimo (.py) files in the current directory
import glob

from pathlib import Path

marimo_dir = Path(__file__).parent / "marimo"
marimo_student_version_dir = marimo_dir / "student_version"


files_to_process = marimo_dir.glob("*.py") # all the marimo files in the marimo directory


for file in files_to_process:
    tree = ast_comments.parse(file.read_text(), file.name)

    # for decl in tree.body:
    nodes_to_remove = []
    for decl in ast.iter_child_nodes(tree):
        if isinstance(decl, ast.FunctionDef):
            if decl.body and isinstance(decl.body[0], ast.Expr):
                expr = decl.body[0].value
                if isinstance(expr, ast.Constant) and expr.value == "CORRECTION":
                    # decl.body = [ast.Pass()]
                    nodes_to_remove.append(decl)

    print(tree.body)
    for node in nodes_to_remove:
        tree.body.remove(node)

    output_file = marimo_student_version_dir / file.name
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(ast_comments.unparse(tree), encoding="utf-8")