import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="game_analytics",
    user="postgres",
    password="postgres123",
    port=5432,
    options="-c search_path=game_analytics"
)

cur = conn.cursor()

with open("complexes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for complex_item in data.get("complexes", []):
    complex_id = complex_item.get("id")
    complex_name = complex_item.get("name")

    # insert complex
    cur.execute("""
        INSERT INTO complexes (complex_id, complex_name)
        VALUES (%s, %s)
        ON CONFLICT (complex_id) DO NOTHING
    """, (complex_id, complex_name))

    for venue in complex_item.get("venues", []):
        cur.execute("""
            INSERT INTO venues
            (venue_id, venue_name, city_name, country_name, country_code, timezone, complex_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (venue_id) DO NOTHING
        """, (
            venue.get("id"),
            venue.get("name"),
            venue.get("city_name"),
            venue.get("country_name"),
            venue.get("country_code"),
            venue.get("timezone"),
            complex_id
        ))

conn.commit()
cur.close()
conn.close()

print("✅ Complexes & Venues inserted successfully")
