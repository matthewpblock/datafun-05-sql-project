-- update 1 or more records in a table.

UPDATE players
-- Convert the height from feet-inches to inches
SET height_inches = (
    (CAST(substr(height, 1, instr(height, '-') - 1) AS INTEGER) * 12) +
    CAST(substr(height, instr(height, '-') + 1) AS INTEGER)
);
