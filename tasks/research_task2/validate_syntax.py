import json
import ast

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

print("Notebook is valid JSON")
print(f"Total cells: {len(nb['cells'])}\n")

code_cells = [48, 50, 53, 56]

for i in code_cells:
    source = ''.join(nb['cells'][i]['source'])
    try:
        ast.parse(source)
        print(f"Cell {i}: ✓ Valid Python syntax")
    except SyntaxError as e:
        print(f"Cell {i}: ✗ Syntax error: {e}")
        print(f"Source:\n{source[:200]}\n")
