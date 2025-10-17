import json

with open(r'C:\Users\MindstormS\Documents\GitHub\ML-COURSE-25-26\tasks\research_task2\KNN.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i in [26, 30, 51, 54, 57]:
    with open(f'C:\\Users\\MindstormS\\Documents\\GitHub\\ML-COURSE-25-26\\tasks\\research_task2\\cell_{i}.txt', 'w', encoding='utf-8') as out:
        out.write(f"Cell {i}:\n")
        out.write(''.join(nb['cells'][i]['source']))
        out.write('\n')

print("Done")
