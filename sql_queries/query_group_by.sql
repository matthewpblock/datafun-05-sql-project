-- use GROUP BY clause (and optionally with aggregation)

-- average weight of players by team
SELECT team, ROUND(AVG(weight), 2) AS avg_weight
FROM players
GROUP BY team
ORDER BY avg_weight DESC;
