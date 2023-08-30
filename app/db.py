import psycopg2

# psql -h database-2.caim22ddifvq.us-east-1.rds.amazonaws.com -U postgres -d pgdatabase
# Database connection parameters
dbname = "pgdatabase"
user = "postgres"
password = ""
host = "database-2.caim22ddifvq.us-east-1.rds.amazonaws.com"
port = "5432"  # Default PostgreSQL port is 5432

# Data to insert
data_to_insert = "Hello, PostgreSQL!"
time_stamp = "2023-08-18 12:34:56"

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )

    # Create a cursor
    cur = conn.cursor()

    # Define the SQL query for insertion
    insert_query = """
    INSERT INTO your_table_name (data, time_stamp)
    VALUES (%s, %s);
    """

    # Execute the insertion query with data
    cur.execute(insert_query, (data_to_insert, time_stamp))

    # Commit the changes
    conn.commit()
    # Close the cursor and connection
    cur.close()
    conn.close()

    print("Data inserted successfully!")

except Exception as e:
    print("Error:", e)
    