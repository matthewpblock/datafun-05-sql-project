-- use GROUP BY clause (and optionally with aggregation)

-- average weight of players by team
SELECT teams, AVG(weight) AS avg_weight
FROM players
GROUP BY team;
