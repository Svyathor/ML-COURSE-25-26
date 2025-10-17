import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

placeholder = '#ваш код'
cells_to_fill = []

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source']).strip()
        if source == placeholder:
            cells_to_fill.append(i)

print(f"Cells to fill: {cells_to_fill}\n")

for idx in cells_to_fill:
    print("="*100)
    print(f"CELL {idx} NEEDS TO BE FILLED")
    print("="*100)

    # Show 2 cells before for context
    if idx >= 2:
        print(f"\n--- Cell {idx-2} ({nb['cells'][idx-2]['cell_type']}) ---")
        print(''.join(nb['cells'][idx-2]['source']))

    if idx >= 1:
        print(f"\n--- Cell {idx-1} ({nb['cells'][idx-1]['cell_type']}) ---")
        print(''.join(nb['cells'][idx-1]['source']))

    print(f"\n>>> CELL {idx} TO FILL <<<")
    print(''.join(nb['cells'][idx]['source']))

    # Show 2 cells after
    if idx < len(nb['cells']) - 1:
        print(f"\n--- Cell {idx+1} ({nb['cells'][idx+1]['cell_type']}) ---")
        print(''.join(nb['cells'][idx+1]['source']))

    if idx < len(nb['cells']) - 2:
        print(f"\n--- Cell {idx+2} ({nb['cells'][idx+2]['cell_type']}) ---")
        print(''.join(nb['cells'][idx+2]['source'])[:1000])

    print("\n")
