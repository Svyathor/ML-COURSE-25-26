import json
import sys

# Read the notebook
with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task1\numpy-pandas-matplotlib.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']

# Write to file with UTF-8 encoding
output_file = r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\notebook_analysis.txt'
out = open(output_file, 'w', encoding='utf-8')

def p(msg):
    out.write(str(msg) + '\n')

p(f'Total cells: {len(cells)}')
p('')

# First, let's print basic info about all cells
p('ALL CELLS OVERVIEW:')
p('=' * 100)

for i, cell in enumerate(cells):
    cell_type = cell['cell_type']
    source = ''.join(cell['source'])

    # For display, truncate source
    source_display = source[:300].replace('\n', ' ')

    p(f'{i:3d}. {cell_type:10s} | {source_display[:80]}...')

p('')
p('')
p('=' * 100)
p('CELLS THAT NEED CODE (empty or with TODO/pass):')
p('=' * 100)

# Identify cells that need code
tasks = []

for i, cell in enumerate(cells):
    cell_type = cell['cell_type']
    source = ''.join(cell['source'])

    # Check if it's a code cell that needs work
    if cell_type == 'code':
        # Check if empty or has TODO/task markers
        is_empty = len(source.strip()) == 0
        has_todo = 'TODO' in source or 'todo' in source or '# your code here' in source.lower() or (source.strip() == 'pass')

        if is_empty or has_todo:
            # Look for task description in previous markdown cells
            task_desc = ''
            for j in range(max(0, i-5), i):
                if cells[j]['cell_type'] == 'markdown':
                    prev_source = ''.join(cells[j]['source'])
                    task_desc = prev_source

            tasks.append({
                'index': i,
                'empty': is_empty,
                'has_todo': has_todo,
                'source': source,
                'task_desc': task_desc
            })

for task in tasks:
    p(f"\n{'='*100}")
    p(f"CELL {task['index']}")
    p(f"Empty: {task['empty']}, Has TODO/pass: {task['has_todo']}")
    p(f"\nTask Description (from previous markdown):")
    p(task['task_desc'][:500])
    p(f"\nCurrent Source:")
    p(task['source'][:200])
    p('='*100)

p(f"\n\nSUMMARY: {len(tasks)} cells need code to be written")
p(f"Cell indices: {[t['index'] for t in tasks]}")

out.close()
print(f"Analysis complete. Output written to {output_file}")
