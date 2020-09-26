import psycopg2
import psycopg2.extras

def to_db():
    """
    This function read a config file to set the database
    information and write example rows in a table that belongs
    to a database.

    Author: Ronie Paolo
    """

    # Reading config file
    f = open('config', 'r')
    ruser = f.readline().split('=')[1][:-1]
    rpassword = f.readline().split('=')[1][:-1]
    rhost = f.readline().split('=')[1][:-1]
    rport = f.readline().split('=')[1][:-1]
    rdatabase = f.readline().split('=')[1][:-1]
    f.close()

    # Writing data in database
    connection = psycopg2.connect(
        user=ruser,
        password=rpassword,
        host=rhost,
        port=rport,
        database=rdatabase
    )
    try:
        cursor = connection.cursor()
        tuples = [(1, 'Karla'), (2, 'Ronie'), (3, 'Emanuel'), (4, 'Andre')]
        psycopg2.extras.execute_batch(cursor, """
            INSERT INTO ods.user(id, name)
            VALUES (%s,%s)
            """, tuples, page_size=1000)
        connection.commit()

        print(cursor.rowcount, 'Record inserted successfully into table ods.user')
    except (Exception, psycopg2.Error) as error:
        print('Failed inserting record into ods.user table {}\n'.format(error))
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print('PostgreSQL connection is closed')

def main():
    to_db()

if __name__ == "__main__":
    main()

