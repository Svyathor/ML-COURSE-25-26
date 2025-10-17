import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Extract cells that import KNN and cross_val functions
with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\key_cells.txt', 'w', encoding='utf-8') as out:
    # Show cells 20-50 (includes imports and first tasks)
    for i in range(20, 50):
        if i >= len(nb['cells']):
            break
        cell = nb['cells'][i]
        out.write(f"\n{'='*100}\n")
        out.write(f"Cell {i} ({cell['cell_type']})\n")
        out.write(f"{'='*100}\n")
        source = ''.join(cell['source'])
        out.write(source)
        out.write('\n')

print("Done - check key_cells.txt")
