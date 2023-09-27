import sqlite3 as sql

def get_columns_and_insert_data(table):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            
            # Get column names for the specified table
            cur.execute(f"PRAGMA table_info({table})")
            columns = cur.fetchall()
            column_names = [column[1] for column in columns]
            
            # Initialize a dictionary to store user input data
            data = {}
            
            # Prompt the user to enter values for each column
            for column_name in column_names:
                value = input(f"Enter value for {column_name}: ")
                data[column_name] = value
            
            # Insert the data into the specified table
            cur.execute(f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '.join(['?'] * len(column_names))})", tuple(data.values()))
            con.commit()
            
            msg = "Record successfully added"
            print(msg)
    except Exception as e:
        con.rollback()
        msg = f"Error in insert operation: {str(e)}"
        print(msg)

# Prompt the user to enter the table name
table_name = input("Enter the table name: ")
get_columns_and_insert_data(table_name)
