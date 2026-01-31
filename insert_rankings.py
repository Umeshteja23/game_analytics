import json
import psycopg2

print("🚀 insert_rankings.py started")

conn = psycopg2.connect(
    host="localhost",
    database="game_analytics",
    user="postgres",
    password="postgres123",
    port=5432,
    options="-c search_path=game_analytics"
)

cur = conn.cursor()

with open("rankings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rankings = data.get("rankings", [])
print("Total ranking records:", len(rankings))

for entry in rankings:
    competitor = entry.get("competitor", {})

    competitor_id = competitor.get("id")
    name = competitor.get("name")
    country = competitor.get("country")
    country_code = competitor.get("country_code")
    abbreviation = competitor.get("abbreviation")

    # insert competitor
    cur.execute("""
        INSERT INTO competitors
        (competitor_id, name, country, country_code, abbreviation)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (competitor_id) DO NOTHING
    """, (competitor_id, name, country, country_code, abbreviation))

    # insert ranking
    cur.execute("""
        INSERT INTO competitor_rankings
        (rank, movement, points, competitions_played, competitor_id)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        entry.get("rank"),
        entry.get("movement"),
        entry.get("points"),
        entry.get("competitions_played"),
        competitor_id
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Competitors & Rankings inserted successfully")
