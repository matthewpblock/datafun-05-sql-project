-- use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

SELECT player_games.date, players.first, players.last, player_games.pts, player_games.reb, player_games.ast, player_games.stl, player_games.blk, players.height_inches, players.weight, players.season_exp, players.pos
FROM player_games
INNER JOIN players ON players.player_id = player_games.player_id
ORDER BY player_games.reb DESC;