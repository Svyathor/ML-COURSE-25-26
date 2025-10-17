import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

filled_cells = [48, 50, 53, 56]

print("="*100)
print("SUMMARY OF FILLED CELLS")
print("="*100)

for idx in filled_cells:
    print(f"\n{'='*100}")
    print(f"CELL {idx}")
    print(f"{'='*100}")

    # Show previous markdown cell for context
    if idx > 0 and nb['cells'][idx-1]['cell_type'] == 'markdown':
        prev_text = ''.join(nb['cells'][idx-1]['source'])
        # Extract task number if present
        if 'Задание' in prev_text:
            lines = prev_text.split('\n')
            for line in lines:
                if 'Задание' in line:
                    print(f"Task: {line.strip()}")
                    break

    print(f"\nCode filled:")
    print(''.join(nb['cells'][idx]['source']))
    print()

print("\n" + "="*100)
print("CELLS NOT FILLED (Theoretical/Bonus Questions)")
print("="*100)
print("\nCell 26: Task 1.1 - Mathematical proof (requires LaTeX)")
print("Cell 30: Task 1.2 - Geometric analysis (requires LaTeX)")
print("Cell 51: Additional text answer for Task 3.2 (answer included in code Cell 50)")
print("Cell 54: Additional text answer for Task 3.3 (answer included in code Cell 53)")
print("Cell 57: Additional text answer for Task 3.4 (answer included in code Cell 56)")
print("Cell 59: Bonus - Meme image (optional)")
