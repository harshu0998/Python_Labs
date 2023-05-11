import sqlite3

class DatabaseManager:
    
    def __init__(self):
        # Connect to the database
        self.con = sqlite3.connect('test.db')
        self.c = self.con.cursor()

        # Check if the students table already exists
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
        table_exists = self.c.fetchone()

        if not table_exists:
            # If the students table does not exist, create it
            self.c.execute('''
                CREATE TABLE students (
                    row TEXT PRIMARY KEY,
                    firstName TEXT,
                    lastName TEXT,
                    phoneNumber TEXT,
                    email TEXT,
                    department TEXT,
                    Major TEXT,
                    gpa TEXT,
                    birthday TEXT
                )
            ''')
            print("Students table created successfully.")
        else:
            print("Students table already exists.")

    def __del__(self):
        # Close the cursor and connection
        self.c.close()
        self.con.close()


    def add_student(self, data):
        # Build the SQL query
        query = "INSERT INTO students VALUES ("
        placeholders = ", ".join("?" * len(data))
        query += placeholders + ")"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, data)

            # Commit the changes
            self.con.commit()
            return "Student added successfully."
        except sqlite3.IntegrityError:
            return "The user already exists"

    def update_student(self, row, column, value):
        # Build the SQL query
        query = f"UPDATE students SET {column.lower()} = ? WHERE row = ?"

        try:
            # Execute the SQL query with the given data
            self.c.execute(query, (value, row))

            # Commit the changes
            self.con.commit()
            return f"{column.capitalize()} for student {row} updated successfully."
        except:
            return f"Failed to update {column} for student {row}."

    def delete_student(self, student_id):
        # Build the SQL query to find the row containing the student_id
        query = "SELECT row FROM students WHERE row = ?"
        self.c.execute(query, (student_id,))
        row = self.c.fetchone()

        # If the row containing the student_id exists, delete the whole row
        if row:
            # Build the SQL query to delete the row
            query = "DELETE FROM students WHERE row = ?"

            try:
                # Execute the SQL query with the given data
                self.c.execute(query, (student_id,))

                # Commit the changes
                self.con.commit()
                return f"Student {student_id} deleted successfully."
            except:
                return f"Failed to delete student {student_id}."
        else:
            return f"No student found with ID {student_id}."

    def delete_student(self, student_id):
        # Connect to the database
        con = sqlite3.connect('test.db')
        c = con.cursor()

        # Build the SQL query to find the row containing the student_id
        query = "SELECT row FROM students WHERE row = ?"
        c.execute(query, (student_id,))
        row = c.fetchone()

        # If the row containing the student_id exists, delete the whole row
        if row:
            # Build the SQL query to delete the row
            query = "DELETE FROM students WHERE row = ?"

            try:
                # Execute the SQL query with the given data
                c.execute(query, (student_id,))

                # Commit the changes and close the database connection
                con.commit()
                con.close()
                return f"Student {student_id} deleted successfully."
            except:
                # Close the database connection
                con.close()
                return f"Failed to delete student {student_id}."
        else:
            # Close the database connection
            con.close()
            return f"No student found with ID {student_id}."


    def display_students(self):
        # Retrieve all data from the students table
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()

        # Display the data in a tabular format
        print("{:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<25} {:<10} {:<15}".format(
            "Student ID", "First Name", "Last Name", "Phone Number", "Email", "Department", "Major", "GPA", "Birthday"))
        print("-" * 140)
        for row in data:
            print("{:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<25} {:<10} {:<15}".format(*row))

        # Close the database connection
        self.con.close()
