import mysql.connector

class HOSPITAL:
    def __init__(self, host, user, password, database):
        # Establishing the connection to the MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pass@1234",
            database="hospital_database"
        )
        self.cursor = self.connection.cursor()

    # Method to create the login and registration tables
    def create(self):
        try:
            # Creating the login table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS login (
                    hospId INT PRIMARY KEY AUTO_INCREMENT,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                );
            """)
            print("Login table created successfully!")

            # Creating the hospReggstrationDetails table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS hospReggstrationDetails (
                    hospId INT PRIMARY KEY,
                    hospName VARCHAR(255) NOT NULL,
                    hospAddress VARCHAR(255) NOT NULL,
                    hospCity VARCHAR(100) NOT NULL,
                    hospState VARCHAR(100) NOT NULL,
                    hospLicenceNo INT NOT NULL UNIQUE,
                    hospLicencePhoto BLOB,
                    drAdharNo INT NOT NULL UNIQUE,
                    drAdharPhoto BLOB,
                    FOREIGN KEY (hospId) REFERENCES login(hospId)
                );
            """)
            print("Hospital registration table created successfully!")

            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Method to insert login details into the 'login' table
    def insert_login(self, email, password):
        try:
            query = """
                INSERT INTO login (email, password)
                VALUES (%s, %s);
            """
            self.cursor.execute(query, (email, password))
            self.connection.commit()
            print("Login details inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Method to insert registration details into the 'hospReggstrationDetails' table
    def insert_registration(self, hospId, hospName, hospAddress, hospCity, hospState, hospLicenceNo, hospLicencePhoto, drAdharNo, drAdharPhoto):
        try:
            query = """
                INSERT INTO hospReggstrationDetails (hospId, hospName, hospAddress, hospCity, hospState, hospLicenceNo, hospLicencePhoto, drAdharNo, drAdharPhoto)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            self.cursor.execute(query, (hospId, hospName, hospAddress, hospCity, hospState, hospLicenceNo, hospLicencePhoto, drAdharNo, drAdharPhoto))
            self.connection.commit()
            print("Hospital registration details inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Method to close the connection
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")

# Example usage:
if __name__ == "__main__":
    # Initialize the HOSPITAL class with your database credentials
    hospital = HOSPITAL(host="localhost", user="root", password="Pass@1234", database="hospitalDB")

    # Create the tables
    hospital.create()

    # Insert data into the 'login' table
    hospital.insert_login("admin@hospital.com", "securepassword")

    # Insert data into the 'hospReggstrationDetails' table (Example)
    hosp_licence_photo = None  # Example: You can replace None with an actual binary image data.
    dr_adhar_photo = None      # Example: You can replace None with an actual binary image data.
    hospital.insert_registration(
        hospId=1,
        hospName="City Hospital",
        hospAddress="123, Main Street",
        hospCity="Citytown",
        hospState="Stateland",
        hospLicenceNo=123456,
        hospLicencePhoto=hosp_licence_photo,
        drAdharNo=987654321,
        drAdharPhoto=dr_adhar_photo
    )

    # Close the connection after operations are done
    hospital.close_connection()
