import json
import sys

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# Write to file with UTF-8 encoding
with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\cells_info.txt', 'w', encoding='utf-8') as out:
    for i in range(min(15, len(nb['cells']))):
        out.write(f"\n{'='*80}\n")
        out.write(f"Cell {i} ({nb['cells'][i]['cell_type']})\n")
        out.write(f"{'='*80}\n")
        out.write(''.join(nb['cells'][i]['source'])[:800])
        out.write('\n')

print("Done - check cells_info.txt")
