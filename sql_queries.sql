/* =========================================================
   SECTION 1: COMPETITIONS & CATEGORIES
   ========================================================= */

-- 1. List all competitions along with their category name
SELECT 
    c.competition_name,
    cat.category_name
FROM competitions c
JOIN categories cat 
ON c.category_id = cat.category_id;

-- 2. Count the number of competitions in each category
SELECT 
    cat.category_name,
    COUNT(c.competition_id) AS total_competitions
FROM categories cat
JOIN competitions c 
ON cat.category_id = c.category_id
GROUP BY cat.category_name;

-- 3. Find all competitions of type 'doubles'
SELECT 
    competition_name
FROM competitions
WHERE type = 'doubles';

-- 4. Get competitions that belong to a specific category (example: ITF Men)
SELECT 
    competition_name
FROM competitions c
JOIN categories cat 
ON c.category_id = cat.category_id
WHERE cat.category_name = 'ITF Men';

-- 5. Identify parent competitions and their sub-competitions
SELECT 
    parent.competition_name AS parent_competition,
    child.competition_name AS sub_competition
FROM competitions parent
JOIN competitions child
ON parent.competition_id = child.parent_id;

-- 6. Analyze the distribution of competition types by category
SELECT 
    cat.category_name,
    c.type,
    COUNT(*) AS count
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id
GROUP BY cat.category_name, c.type;

-- 7. List all competitions with no parent (top-level competitions)
SELECT 
    competition_name
FROM competitions
WHERE parent_id IS NULL;


/* =========================================================
   SECTION 2: COMPLEXES & VENUES
   ========================================================= */

-- 8. List all venues along with their associated complex name
SELECT 
    v.venue_name,
    c.complex_name
FROM venues v
JOIN complexes c
ON v.complex_id = c.complex_id;

-- 9. Count the number of venues in each complex
SELECT 
    c.complex_name,
    COUNT(v.venue_id) AS total_venues
FROM complexes c
JOIN venues v
ON c.complex_id = v.complex_id
GROUP BY c.complex_name;

-- 10. Get details of venues in a specific country (example: Chile)
SELECT 
    venue_name,
    city_name,
    country_name
FROM venues
WHERE country_name = 'Chile';

-- 11. Identify all venues and their timezones
SELECT 
    venue_name,
    timezone
FROM venues;

-- 12. Find complexes that have more than one venue
SELECT 
    complex_id,
    COUNT(venue_id) AS venue_count
FROM venues
GROUP BY complex_id
HAVING COUNT(venue_id) > 1;

-- 13. List venues grouped by country
SELECT 
    country_name,
    COUNT(*) AS total_venues
FROM venues
GROUP BY country_name;

-- 14. Find all venues for a specific complex (example: Nacional)
SELECT 
    v.venue_name
FROM venues v
JOIN complexes c
ON v.complex_id = c.complex_id
WHERE c.complex_name = 'Nacional';


/* =========================================================
   SECTION 3: COMPETITORS & RANKINGS
   ========================================================= */

-- 15. Get all competitors with their rank and points
SELECT 
    c.name,
    r.rank,
    r.points
FROM competitors c
JOIN competitor_rankings r
ON c.competitor_id = r.competitor_id;

-- 16. Find competitors ranked in the top 5
SELECT 
    c.name,
    r.rank
FROM competitors c
JOIN competitor_rankings r
ON c.competitor_id = r.competitor_id
WHERE r.rank <= 5;

-- 17. List competitors with no rank movement (stable rank)
SELECT 
    c.name,
    r.rank
FROM competitors c
JOIN competitor_rankings r
ON c.competitor_id = r.competitor_id
WHERE r.movement = 0;

-- 18. Get total points of competitors from a specific country (example: Croatia)
SELECT 
    country,
    SUM(r.points) AS total_points
FROM competitors c
JOIN competitor_rankings r
ON c.competitor_id = r.competitor_id
WHERE country = 'Croatia'
GROUP BY country;

-- 19. Count the number of competitors per country
SELECT 
    country,
    COUNT(*) AS total_competitors
FROM competitors
GROUP BY country;

-- 20. Find competitors with the highest points
SELECT 
    c.name,
    r.points
FROM competitors c
JOIN competitor_rankings r
ON c.competitor_id = r.competitor_id
ORDER BY r.points DESC
LIMIT 1;


/* =========================================================
   EXTRA (SAFE BONUS QUERIES – GOOD IMPRESSION)
   ========================================================= */

-- 21. Total number of competitions
SELECT COUNT(*) AS total_competitions
FROM competitions;

-- 22. Total number of venues
SELECT COUNT(*) AS total_venues
FROM venues;
