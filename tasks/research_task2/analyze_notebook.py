import json
import sys

# Load notebook
with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Find cells with placeholder comment
cells_to_fill = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if '#��� ���' in source or source.strip() == '':
            cells_to_fill.append(i)

print(f"Total cells: {len(nb['cells'])}")
print(f"Cells to fill: {cells_to_fill}")
print("\n" + "="*80)

# For each cell to fill, show context
for idx in cells_to_fill:
    print(f"\n{'='*80}")
    print(f"CELL {idx} TO FILL")
    print(f"{'='*80}")

    # Show previous cell (usually markdown with question)
    if idx > 0:
        prev_cell = nb['cells'][idx-1]
        print(f"\nPREVIOUS CELL {idx-1} ({prev_cell['cell_type']}):")
        print(''.join(prev_cell['source']))

    # Show current cell
    print(f"\nCURRENT CELL {idx} (code):")
    print(''.join(nb['cells'][idx]['source']))

    # Show next cell
    if idx < len(nb['cells']) - 1:
        next_cell = nb['cells'][idx+1]
        print(f"\nNEXT CELL {idx+1} ({next_cell['cell_type']}):")
        print(''.join(next_cell['source'])[:500])
