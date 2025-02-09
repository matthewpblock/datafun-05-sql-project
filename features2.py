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
        games_data_path = pathlib.Path("data", "games.csv")
        player_game_data_path = pathlib.Path("data", "player_game.csv")
        players_df = pd.read_csv(player_data_path)
        teams_df = pd.read_csv(team_data_path)
        games_df = pd.read_csv(games_data_path)
        player_games_df = pd.read_csv(player_game_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            players_df.to_sql("players", conn, if_exists="append", index=False)
            teams_df.to_sql("teams", conn, if_exists="append", index=False)
            games_df.to_sql("games", conn, if_exists="append", index=False)
            player_games_df.to_sql("player_games", conn, if_exists="append", index=False)
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

###############################################
# Main Execution 
################################################

def main() -> None:
    # Log start of database setup
    logger.info("Starting updates and feature engineering...")
    
    # Define path variables
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_FEATURES_FOLDER = ROOT_DIR.joinpath("sql_features")
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath('db.sqlite')

    # Ensure the data folder where we will put the db exists
    DATA_FOLDER.mkdir(exist_ok=True)

    # Connect to SQLite database (it will be created if it doesn't exist)
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        # Execute SQL files to set up the database
        # Pass in the connection and the path to the SQL file to be executed
        execute_sql_file(connection, SQL_FEATURES_FOLDER.joinpath('delete_records.sql'))
        # Insert data from CSV files into the database
        insert_data_from_csv()
        # Execute SQL files with feature engineering updates
        execute_sql_file(connection, SQL_FEATURES_FOLDER.joinpath('update_records.sql'))

        logger.info("Database updates completed successfully.")
    except Exception as e:
        logger.error(f"Error during database updates: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()