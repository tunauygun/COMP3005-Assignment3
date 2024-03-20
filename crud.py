import psycopg2

def connectToDatabase(databaseName, host, user, password, port):
    """
    Establishes a connection to a PostgreSQL database.

    Args:
        databaseName (str): The name of the database.
        host (str): The database host (e.g., "127.0.0.1").
        user (str): The database user.
        password (str): The user's password.
        port (str): The port number (e.g., "5432").

    Returns:
        psycopg2.extensions.cursor: A cursor object for executing queries.
    """
    conn = psycopg2.connect(database=databaseName,
                        host=host,
                        user=user,
                        password=password,
                        port=port)

    return conn


def getAllStudents(cursor):
    """
    Retrieves all students in the database.

    Args:
        cursor (psycopg2.extensions.cursor): The cursor connected to the database.

    Returns:
        list: A list of tuples, where each tuple represents a student.
    """
    # Define the SELECT query
    select_query = "SELECT * FROM students;"

    # Execute the query
    cursor.execute(select_query)

    # Fetch all rows
    all_students = cursor.fetchall()

    if all_students:
        for row in all_students:
            print(row)
    else:
        print("No student in the database!")
    print()

    return all_students


def addStudent(cursor, conn, first_name, last_name, email, enrollment_date):
    """
    Insert a new student into the students table.
    """
    sql = """
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (first_name, last_name, email, enrollment_date))   
    conn.commit()
    print("Student created successfully")


def updateStudentEmail(cursor, conn, student_id, new_email):
    """
    Updates the student email of a student with the given student id.
    """
    sql = "UPDATE students set email = '" + new_email + "' where student_id = " + str(student_id)
    cursor.execute(sql, (new_email, str(student_id)))   
    conn.commit()
    print("Student email updated successfully")


def deleteStudent(cursor, conn, student_id):
    """
    Deletes the student email of a student with the given student id.
    """
    sql = "DELETE FROM students WHERE student_id = " + str(student_id)
    cursor.execute(sql)
    conn.commit()
    print("Student deleted successfully")




if __name__ == "__main__":
    # Connect to the database and get the cursor
    conn = connectToDatabase("Assignment3", "127.0.0.1", "postgres", "admin", "5432")
    cursor = conn.cursor()

    # Query all students
    all_students = getAllStudents(cursor)

    # Add new student
    addStudent(cursor, conn, "Tuna", "Uygun", "tunauygun@cmail.carleton.ca", "2020-09-01")

    # Query all students
    all_students = getAllStudents(cursor)

    # Add new student
    updateStudentEmail(cursor, conn, 7, "tuna@cmail.carleton.ca")

    # Query all students
    all_students = getAllStudents(cursor)

    # Add new student
    deleteStudent(cursor, conn, 7)

    # Query all students
    all_students = getAllStudents(cursor)
