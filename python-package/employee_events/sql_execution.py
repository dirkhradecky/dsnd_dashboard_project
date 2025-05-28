from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE

db_path = Path(__file__).parent / "employee_events.db"


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    """
    A mixin class that provides methods for executing SQL queries.
    This class can be used to execute SQL queries and return results
    as pandas DataFrames or lists of tuples.
    """
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    def pandas_query(self, sql_query: str) -> pd.DataFrame:
        """
        Executes an SQL query and returns the result as a pandas DataFrame.

        Args:
            sql_query (str): The SQL query to execute.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the query result.
        """
        connection = connect(db_path)
        df = pd.read_sql_query(sql_query, connection)
        connection.close()
        return df

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(self, sql_query: str) -> list:
        """
        Executes an SQL query and returns the result as a list of tuples.

        Args:
            sql_query (str): The SQL query to execute.

        Returns:
            list: A list of tuples containing the query result.
        """
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(sql_query).fetchall()
        connection.close()
        return result
 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
