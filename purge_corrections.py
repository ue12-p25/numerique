#!/usr/bin/env python3

import ast
import ast_comments
from pathlib import Path

marimo_dir = Path(__file__).parent / "marimo"
marimo_student_version_dir = marimo_dir / "student_version"


files_to_process = sorted(
    marimo_dir.glob("*.py"),
    key=lambda x: x.name,
)  # all the marimo files in the marimo directory (sorted by name)

max_file_name_length = max(len(file.name) for file in files_to_process)

for file in files_to_process:
    print(f"PURGING {file.name + "...":<{max_file_name_length+3}}", end="")
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

    for node in nodes_to_remove:
        tree.body.remove(node)

    output_file = marimo_student_version_dir / file.name
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(ast_comments.unparse(tree), encoding="utf-8")

    print(" ✅")

print("FINITO 🎉")
