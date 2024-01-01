import json
import psycopg2

db_params = {
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'db_lab3',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)

cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables = cur.fetchall()

all_data = {}

for table in tables:
    table_name = table[0]

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    all_data[table_name] = []

    for row in rows:
        row_dict = {}
        for i, desc in enumerate(cur.description):
            row_dict[desc[0]] = row[i]
        all_data[table_name].append(row_dict)

json_file_path = "all_data.json"

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, indent=2)

cur.close()
conn.close()
