# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
from .sql_execution import QueryMixin
import pandas as pd

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self) -> list:
        
        # Return an empty list
        # YOUR CODE HERE
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id: int) -> pd.DataFrame:

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        id_column = f"{self.name}_id"
        sql_query = f"""
        SELECT event_date, 
               SUM(positive_events) AS positive_count,
               SUM(negative_events) AS negative_count
        FROM employee_events
        WHERE {id_column} = {id}
        GROUP BY event_date
        ORDER BY event_date;
        """
        # Execute the query and return the result as a pandas dataframe
        return self.pandas_query(sql_query)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id: int) -> pd.DataFrame:

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE
        id_column = f"{self.name}_id"
        sql_query = f"""
        SELECT note_date, note
        FROM notes
        WHERE {id_column} = {id}
        ORDER BY note_date;
        """
        # Execute the query and return the result as a pandas dataframe
        return self.pandas_query(sql_query)

