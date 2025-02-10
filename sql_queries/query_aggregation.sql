--  use aggregation functions including COUNT, AVG, SUM.

-- report AVG height of all players
SELECT AVG(height_inches) AS avg_height_in, AVG(weight) AS avg_weight
FROM players;

-- report COUNT of bubble games
-- SELECT COUNT(*) AS bubble_games
-- FROM games
-- WHERE bubble = true;

-- report COUNT of regular games
-- SELECT COUNT(*) AS regular_games
-- FROM games
-- WHERE bubble = false;

-- compare home and road points in bubble games vs regular games
-- SELECT SUM(home_pts) AS bubble_home_points
-- FROM games
-- WHERE bubble = TRUE;

-- SELECT SUM(away_pts) AS bubble_away_points
-- FROM games
-- WHERE bubble = TRUE;

-- SELECT SUM(home_pts) AS regular_home_points
-- FROM games
-- WHERE bubble = FALSE;

-- SELECT SUM(away_pts) AS regular_away_points
-- FROM games
-- WHERE bubble = FALSE;

