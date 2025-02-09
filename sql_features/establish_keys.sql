ALTER TABLE teams ADD PRIMARY KEY (team_id);
ALTER TABLE players ADD PRIMARY KEY (player_id);
ALTER TABLE players ADD FOREIGN KEY (team_id) REFERENCES teams (team_id);
ALTER TABLE players ADD FOREIGN KEY (team_id2) REFERENCES teams (team_id);
