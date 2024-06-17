import json
import plotly.express as px
import pandas as pd

# Načtení dat ze souboru
file_path = r'C:\Users\toust\Desktop\UNOB\AIZ2\output.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Příprava dat pro Sunburst diagram
rows = []

for record in data:
    class_name = record['class.name']
    user_full_name = f"{record['user.name']} {record['user.surname']}"
    for event_key, event_data in record['presences'].items():
        event_name = event_data['event.name']
        presence_type = event_data['presenceType.name']
        rows.append([class_name, user_full_name, event_name, presence_type])

df = pd.DataFrame(rows, columns=['Class', 'User Full Name', 'Event Name', 'Presence Type'])

# Vytvoření Sunburst diagramu
fig = px.sunburst(
    df,
    path=['Class', 'User Full Name', 'Event Name', 'Presence Type'],
    values=[1]*len(df),  # Dummy values to create the structure
    title="Sunburst Diagram of Class Attendance"
)

# Zobrazení diagramu
fig.show()
