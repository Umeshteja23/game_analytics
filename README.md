# game_analytics
🎾 Game Analytics: Unlocking Tennis Data with SportRadar API
📌 Project Overview

This project is an end-to-end Data Analytics application built to extract, store, analyze, and visualize professional tennis data using the SportRadar API.
It demonstrates real-world skills in API integration, PostgreSQL database design, SQL analytics, and Streamlit dashboard development.

The application allows users to explore:

Tennis competitions and categories

Sports complexes and venues worldwide

Doubles competitor rankings

Key analytical insights through SQL and interactive dashboards

🎯 Objectives

Collect structured tennis data from external APIs

Transform and normalize nested JSON data

Design and populate a relational PostgreSQL database

Write analytical SQL queries for insights

Build an interactive Streamlit dashboard for visualization

🛠️ Tech Stack

Programming Language: Python

Database: PostgreSQL

API: SportRadar Tennis API

Visualization: Streamlit

Data Handling: Pandas

Version Control: Git & GitHub

📂 Project Structure
tennis_project/
│
├── app.py                     # Streamlit dashboard
├── fetch_competitions.py      # Fetch competitions data from API
├── fetch_complexes.py         # Fetch complexes & venues data
├── insert_competitions.py     # Insert competitions & categories into DB
├── insert_complexes.py        # Insert complexes & venues into DB
├── insert_rankings.py         # Insert competitor rankings
├── competitions.json          # Raw competitions data
├── complexes.json             # Raw complexes data
├── rankings.json              # Sample rankings data
├── sql_queries.sql            # All required SQL analysis queries
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file

🗄️ Database Schema

The database is designed using normalized relational tables:

Core Tables

categories

competitions

complexes

venues

competitors

competitor_rankings

Each table uses primary keys and foreign keys to maintain data integrity.

📊 SQL Analysis

All required 21+ SQL queries are written and stored in:

sql_queries.sql


The queries cover:

Competition & category analysis

Venue & complex insights

Country-wise distribution

Competitor rankings & performance metrics

📈 Streamlit Dashboard Features

The Streamlit application provides:

📊 Overview metrics

Total competitions

Total categories

Total venues

Total competitors

🏆 Competition Explorer

Filter by competition type (singles/doubles)

🌍 Venues Analysis

Top countries by number of venues (bar chart)

🥇 Doubles Rankings

Competitor rankings and points table

The dashboard is clean, responsive, and designed for analytical storytelling.

🔐 API Security Handling

To follow best practices:

API keys are not hard-coded

Environment variables are used instead

.gitignore prevents sensitive data from being pushed to GitHub

This ensures the project is secure and production-ready.

⚠️ Note on Rankings Data

The SportRadar trial API restricts access to certain ranking endpoints.
To demonstrate the complete data pipeline:

A representative sample JSON was used for competitor rankings

The schema, insertion logic, and SQL analysis remain production-ready

▶️ How to Run the Project
1️⃣ Set API Key (Windows PowerShell)
setx SPORTRADAR_API_KEY "your_api_key_here"

2️⃣ Run Streamlit App
streamlit run app.py


Open in browser:

http://localhost:8501

📸 Dashboard Screenshots

Screenshots of the Streamlit dashboard are included in the repository to showcase:

Overview metrics

Competitions table

Venues analysis chart

Rankings table

🧠 Key Learnings

Handling nested API responses

Designing scalable SQL schemas

Writing analytical SQL queries

Debugging real-world data issues (nulls, schema mismatches)

Building production-style dashboards

👤 Author

Umesh Teja Chowdary
Data Analytics Enthusiast | Python | SQL | Streamlit

✅ Project Status

✔ Completed
✔ Evaluation Ready
✔ Portfolio Ready
