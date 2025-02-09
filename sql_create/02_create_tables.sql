-- create your database schema using sql


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