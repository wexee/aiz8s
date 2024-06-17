import json
import matplotlib.pyplot as plt

# Načtení dat z JSON souboru
file_path = r'C:\Users\toust\Desktop\UNOB\AIZ2\output.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Zpracování dat
students_presence = {}

for record in data:
    student_name = f"{record['user.name']} {record['user.surname']}"
    if student_name not in students_presence:
        students_presence[student_name] = {'Přítomen': 0, 'Nepřítomen': 0}
    
    for event_key, event in record['presences'].items():
        if event['presenceType.name'] == 'Přítomen':
            students_presence[student_name]['Přítomen'] += 1
        else:
            students_presence[student_name]['Nepřítomen'] += 1

# Vykreslení grafu
student_names = list(students_presence.keys())
presence_counts = [students_presence[name]['Přítomen'] for name in student_names]
absence_counts = [students_presence[name]['Nepřítomen'] for name in student_names]

x = range(len(student_names))

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x, presence_counts, width=0.4, label='Přítomen', align='center')
ax.bar(x, absence_counts, width=0.4, label='Nepřítomen', align='edge')

ax.set_xlabel('Studenti')
ax.set_ylabel('Počet')
ax.set_title('Přítomnost a nepřítomnost studentů')
ax.set_xticks(x)
ax.set_xticklabels(student_names, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()
