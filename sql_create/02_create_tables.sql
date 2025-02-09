-- create your database schema using sql

-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

-- Create the teams table
CREATE TABLE teams (
    team TEXT PRIMARY KEY,
    nickname TEXT,
    city TEXT,
    [state] TEXT,
    conference TEXT,
    division TEXT
);

-- Create the players table with a foreign key to the teams table
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birthdate INTEGER,
    height TEXT,
    [weight] INTEGER,
    country TEXT,
    team TEXT,
    FOREIGN KEY (team) REFERENCES teams (team)
);