-- drop tables to restart
DROP TABLE IF EXISTS player_stats;
DROP TABLE IF EXISTS player_games;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS games;
-- save teams for last due to foreign key constraint
DROP TABLE IF EXISTS teams;