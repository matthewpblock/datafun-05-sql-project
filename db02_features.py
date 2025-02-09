# Create a Python script that demonstrates the ability to run sql scripts to interact with fields, update records, delete records, and maybe add additional columns.

############################################
# Imports
############################################
import sqlite3
import pandas as pd
import pathlib

# Import local modules
from utils_logger import logger
############################################
# Define Variables
############################################

# Define the database file in the current root project directory
db_file = pathlib.Path("data\\db.sqlite")

############################################
# Define Functions
############################################

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        player_data_path = pathlib.Path("data", "players.csv")
        team_data_path = pathlib.Path("data", "teams.csv")
        players_df = pd.read_csv(player_data_path)
        teams_df = pd.read_csv(team_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            players_df.to_sql("players", conn, if_exists="replace", index=False)
            teams_df.to_sql("teams", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql_file(connection, file_path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (str): Path to the SQL file to be executed.
    """
    # We know reading from a file can raise exceptions, so we wrap it in a try block
    try:
        with open(file_path, 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
        with connection:
            # Use the connection as a context manager to execute the SQL script
            connection.executescript(sql_script)
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise
            
def establish_keys():
    """Function to establish primary keys foreign keys between the players and teams tables."""
    try:
        with sqlite3.connect(db_file) as conn:
           
            print("Keys established.")
    except sqlite3.Error as e:
        print("Error establishing keys:", e)
        
############################################
# Main Execution
############################################
def main() -> None:
    insert_data_from_csv()
    
if __name__ == '__main__':
    main()