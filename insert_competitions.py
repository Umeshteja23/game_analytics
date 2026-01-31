import json
import psycopg2

# ---------- DATABASE CONNECTION ----------
conn = psycopg2.connect(
    host="localhost",
    database="game_analytics",
    user="postgres",
    password="postgres123",
    port=5432,
    options="-c search_path=game_analytics"
)

cur = conn.cursor()

# ---------- LOAD JSON ----------
with open("competitions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

competitions = data.get("competitions", [])

for comp in competitions:
    category = comp.get("category", {})

    category_id = category.get("id")
    category_name = category.get("name")

    # insert category
    cur.execute("""
        INSERT INTO categories (category_id, category_name)
        VALUES (%s, %s)
        ON CONFLICT (category_id) DO NOTHING
    """, (category_id, category_name))

    # insert competition
    cur.execute("""
    INSERT INTO competitions
    (competition_id, competition_name, parent_id, type, gender, category_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (competition_id) DO NOTHING
""", (
    comp.get("id"),
    comp.get("name"),
    comp.get("parent_id"),
    comp.get("type"),
    comp.get("gender") or "unknown",
    category_id
))

    

conn.commit()
cur.close()
conn.close()

print("✅ Categories & Competitions inserted successfully")

