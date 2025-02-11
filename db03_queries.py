# Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings:

'''
Use Python to execute SQL scripts. 
'''

# Imports from Python Standard Library
import sqlite3
import pathlib
import pandas as pd

# Import local modules
from utils_logger import logger

############################################
# Define Variables
############################################

# Define the database file in the current root project directory
db_file = pathlib.Path("data\\db.sqlite")

# Define path variables
ROOT_DIR = pathlib.Path(__file__).parent.resolve()
SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
DATA_FOLDER = ROOT_DIR.joinpath("data")
DB_PATH = DATA_FOLDER.joinpath('db.sqlite')
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

############################################
# Define Functions
############################################
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
            cursor.executescript(sql_script)
            results = cursor.fetchall()
            df_results = pd.DataFrame()
            for row in results:
                df_row = (row)
                df_results = df_results.append(df_row)
            print(df_results.head())
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise
    
def sorting_rim_protection():
    '''Sort the players by rim protection (blocks per game) in descending order.'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        with open(SQL_QUERIES_FOLDER.joinpath('query_sorting.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            # Execute the SQL script into a DataFrame
            df_sorted = pd.read_sql_query(sql_script, connection)
            print(df_sorted.head())
        logger.info("Sorted successfully.")
    except Exception as e:
        logger.error(f"Error during sorting: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
    
        
def group_by_team_avg_weight():
    '''Group the players by team and calculate the average weight of each team.'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        with open(SQL_QUERIES_FOLDER.joinpath('query_group_by.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            # Execute the SQL script into a DataFrame
            df_grouped = pd.read_sql_query(sql_script, connection)
            print(df_grouped.head())
        logger.info("Grouped successfully.")
    except Exception as e:
        logger.error(f"Error during grouping: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
        
def filter_bench():
    '''Filter to only performances coming off the bench (no starters)'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        with open(SQL_QUERIES_FOLDER.joinpath('query_filter.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            # Execute the SQL script into a DataFrame
            df_filtered = pd.read_sql_query(sql_script, connection)
            print(df_filtered.head())
        logger.info("Filtered successfully.")
    except Exception as e:
        logger.error(f"Error during filtering: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
    
def aggregation():
    '''Calculate average height and weight of league players'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        with open(SQL_QUERIES_FOLDER.joinpath('query_aggregation.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            # Execute the SQL script into a DataFrame
            df_aggregated = pd.read_sql_query(sql_script, connection)
            print(df_aggregated.head())
        logger.info("Aggregated successfully.")
    except Exception as e:
        logger.error(f"Error during aggregation: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
    #print(f"Results:\n"
    #      f"Average height in inches: {avg_height_in}\n"
    #      f"Average weight: {avg_weight}\n"
    #      f"Count of Bubble Games: {bubble_games}\n"
    #      f"Count of Regular Games: {regular_games}\n"
    #      f"Bubble Home Points: {bubble_home_points}\n"
    #      f"Bubble Away Points: {bubble_away_points}\n"
    #      f"Regular Home Points: {regular_home_points}\n"
    #      f"Regular Away Points: {regular_away_points}")
    
def join():
    '''Reserved for future use.
    Will implement joining once .sql file is created.'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        # execute_sql_file(connection, SQL_QUERIES_FOLDER.joinpath('query_capture.sql'))
        with open(SQL_QUERIES_FOLDER.joinpath('query_join.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            df_join = pd.read_sql_query(sql_script, connection)
            print(df_join.head())
        logger.info("Joined successfully.")
    except Exception as e:
        logger.error(f"Error during joining: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
        
def capture_dataframe():
    '''Capture the results of the SQL query in a Pandas DataFrame.'''
    try:
        logger.info(f"Connected to database: {DB_PATH}")
        # execute_sql_file(connection, SQL_QUERIES_FOLDER.joinpath('query_capture.sql'))
        with open(SQL_QUERIES_FOLDER.joinpath('query_sorting.sql'), 'r') as file:
            # Read the SQL file into a string
            sql_script: str = file.read()
            df = pd.read_sql_query(sql_script, connection)
            print(df.head())
        logger.info("Captured successfully.")
    except Exception as e:
        logger.error(f"Error during capturing: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")
    
###############################################
# Main Execution 
# ###############################################
def main() -> None:
    print("Using queries module...")



if __name__ == '__main__':
    main()