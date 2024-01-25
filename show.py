import psycopg2

def show_table_data(connection_params, table_name):
    # Connect to PostgreSQL
    conn = psycopg2.connect(**connection_params)

    # Create a cursor
    cur = conn.cursor()

    # Execute a query to retrieve data from the specified table
    cur.execute(f"SELECT * FROM {table_name};")

    # Fetch all the rows
    table_data = cur.fetchall()

    # Print the table data
    print(f"\nContents of {table_name} table:")
    for row in table_data:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()

# Define the connection parameters
connection_params = {
    "host": "127.0.0.1",
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres"
}

# Specify the table names you want to show
table_names = ["actors", "events"]

# Call the function to show data for each table
for table_name in table_names:
    show_table_data(connection_params, table_name)
