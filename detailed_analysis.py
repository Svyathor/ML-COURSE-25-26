import json

# Read the notebook
with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task1\numpy-pandas-matplotlib.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']

# Write to file with UTF-8 encoding
output_file = r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\detailed_tasks.txt'
out = open(output_file, 'w', encoding='utf-8')

def p(msg):
    out.write(str(msg) + '\n')

# Cells that need code based on previous analysis
task_cells = [16, 20, 23, 26, 29, 37]

p("="*100)
p("DETAILED TASK ANALYSIS FOR NUMPY-PANDAS-MATPLOTLIB NOTEBOOK")
p("="*100)
p("")

# Group by section
p("SECTION GROUPING:")
p("-" * 100)
p("")

sections = {
    'Pandas': [16, 20, 23, 26, 29],
    'Matplotlib': [37],
    'Numpy': []  # No empty cells in numpy section (tasks 1-5 are in .py files)
}

for section, cells_list in sections.items():
    p(f"{section} Section: Cells {cells_list}")
p("")
p("")

# Detailed task descriptions
for cell_idx in task_cells:
    p("="*100)
    p(f"CELL {cell_idx}")
    p("="*100)

    # Find the immediately preceding markdown cell with task description
    for j in range(cell_idx - 1, max(0, cell_idx - 5), -1):
        if cells[j]['cell_type'] == 'markdown':
            source = ''.join(cells[j]['source'])
            # Check if this looks like a task description (has "Задание" in it)
            if 'Задание' in source or 'Задача' in source:
                p("\nTask Description:")
                p("-" * 100)
                p(source)
                break

    # Show current cell source
    current_source = ''.join(cells[cell_idx]['source'])
    p("\nCurrent Code:")
    p("-" * 100)
    p(current_source)
    p("")
    p("")

# Now let's also check the Numpy section more carefully
p("="*100)
p("NUMPY SECTION ANALYSIS")
p("="*100)
p("")

# Look for numpy task descriptions
for i, cell in enumerate(cells):
    if cell['cell_type'] == 'markdown':
        source = ''.join(cell['source'])
        if 'Задача' in source and 'Numpy' in source[:200]:
            p(f"\nFound Numpy task info in cell {i}:")
            p("-" * 100)
            p(source[:1000])
            p("")

# Also check for mentions of research_functions files
p("\n" + "="*100)
p("NUMPY IMPLEMENTATION FILES")
p("="*100)
p("")

for i, cell in enumerate(cells):
    source = ''.join(cell['source'])
    if 'research_functions' in source:
        p(f"\nCell {i} mentions research_functions:")
        p("-" * 100)
        p(source[:500])
        p("")

out.close()
print(f"Detailed analysis written to {output_file}")
