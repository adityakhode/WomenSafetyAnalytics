# import mysql.connector

# class USER:
#     def __init__(self, host, user, password, database):
#         self.connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Pass@1234",
#             database="user_database"
#         )
#         self.cursor = self.connection.cursor()

#     def create_tables(self):
#         queries = [
#             """
#             CREATE TABLE IF NOT EXISTS sosDetails (
#                 userId INT PRIMARY KEY,
#                 phoneNo1 BIGINT,
#                 phoneNo2 BIGINT,
#                 phoneNo3 BIGINT,
#                 phoneNo4 BIGINT,
#                 phoneNo5 BIGINT,
#                 email1 VARCHAR(255),
#                 email2 VARCHAR(255),
#                 email3 VARCHAR(255),
#                 email4 VARCHAR(255),
#                 email5 VARCHAR(255)
#             );
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS userLogin (
#                 userId INT AUTO_INCREMENT PRIMARY KEY,
#                 email VARCHAR(255) NOT NULL UNIQUE,
#                 phoneNo BIGINT NOT NULL,
#                 password VARCHAR(255) NOT NULL
#             );
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS userBasicDetails (
#                 userId INT PRIMARY KEY,
#                 tag CHAR(1),
#                 firstName VARCHAR(255),
#                 middleName VARCHAR(255),
#                 lastName VARCHAR(255),
#                 dob DATE,
#                 disabilityStatus BINARY,
#                 bloodGroup VARCHAR(5),
#                 FOREIGN KEY (userId) REFERENCES userLogin(userId)
#             );
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS userAddress (
#                 userId INT PRIMARY KEY,
#                 permanentAddress VARCHAR(255),
#                 permanentLandMark VARCHAR(255),
#                 permanentCity VARCHAR(100),
#                 permanentPinCode SMALLINT,
#                 permanentDistrict VARCHAR(100),
#                 permanentState VARCHAR(100),
#                 permanentCountry VARCHAR(100),
#                 currentAddress VARCHAR(255),
#                 currentLandmark VARCHAR(255),
#                 currentCity VARCHAR(100),
#                 currentPinCode SMALLINT,
#                 currentDistrict VARCHAR(100),
#                 currentState VARCHAR(100),
#                 currentCountry VARCHAR(100),
#                 FOREIGN KEY (userId) REFERENCES userLogin(userId)
#             );
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS userLocation (
#                 userId INT PRIMARY KEY,
#                 latitude VARCHAR(50),
#                 longitude VARCHAR(50),
#                 FOREIGN KEY (userId) REFERENCES userLogin(userId)
#             );
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS userTickets (
#                 userId INT,
#                 latitude VARCHAR(50),
#                 longitude VARCHAR(50),
#                 status BINARY,
#                 PRIMARY KEY (userId, latitude, longitude),
#                 FOREIGN KEY (userId) REFERENCES userLogin(userId)
#             );
#             """
#         ]

#         for query in queries:
#             self.cursor.execute(query)
#         self.connection.commit()
#         print("Tables created successfully.")

#     def register_user(self, email, phoneNo, password, basic_details, sos_details):
#         try:
#             # Insert into userLogin and fetch userId
#             login_query = """
#             INSERT INTO userLogin (email, phoneNo, password)
#             VALUES (%s, %s, %s)
#             """
#             self.cursor.execute(login_query, (email, phoneNo, password))
#             userId = self.cursor.lastrowid  # Fetch the auto-generated userId
#             print(f"User login created with userId: {userId}")

#             # Insert into userBasicDetails
#             basic_query = """
#             INSERT INTO userBasicDetails (
#                 userId, tag, firstName, middleName, lastName, dob, disabilityStatus, bloodGroup
#             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             self.cursor.execute(basic_query, (
#                 userId,
#                 basic_details["tag"],
#                 basic_details["firstName"],
#                 basic_details["middleName"],
#                 basic_details["lastName"],
#                 basic_details["dob"],
#                 basic_details["disabilityStatus"],
#                 basic_details["bloodGroup"]
#             ))
#             print("User basic details inserted successfully.")

#             # Insert into sosDetails
#             sos_query = """
#             INSERT INTO sosDetails (
#                 userId, phoneNo1, phoneNo2, phoneNo3, phoneNo4, phoneNo5,
#                 email1, email2, email3, email4, email5
#             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             self.cursor.execute(sos_query, (
#                 userId,
#                 sos_details["phoneNo1"],
#                 sos_details["phoneNo2"],
#                 sos_details["phoneNo3"],
#                 sos_details["phoneNo4"],
#                 sos_details["phoneNo5"],
#                 sos_details["email1"],
#                 sos_details["email2"],
#                 sos_details["email3"],
#                 sos_details["email4"],
#                 sos_details["email5"]
#             ))
#             print("SOS details inserted successfully.")

#             # Commit the transaction
#             self.connection.commit()
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#             self.connection.rollback()
#         finally:
#             self.close_connection()

#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()
#         print("Database connection closed.")


# # Example usage
# if __name__ == "__main__":
#     db = USER(host="localhost", user="root", password="Pass@1234", database="user_database")
#     db.create_tables()

#     # User details
#     basic_details = {
#         "tag": "M",
#         "firstName": "John",
#         "middleName": "A.",
#         "lastName": "Doe",
#         "dob": "1990-01-01",
#         "disabilityStatus": 0,
#         "bloodGroup": "O+"
#     }
#     sos_details = {
#         "phoneNo1": 1111111111,
#         "phoneNo2": 2222222222,
#         "phoneNo3": 3333333333,
#         "phoneNo4": 4444444444,
#         "phoneNo5": 5555555555,
#         "email1": "email1@example.com",
#         "email2": "email2@example.com",
#         "email3": "email3@example.com",
#         "email4": "email4@example.com",
#         "email5": "email5@example.com"
#     }

#     db.register_user("example3@example.com", 9876543210, "securepassword", basic_details, sos_details)





import mysql.connector
from functools import wraps

class USER:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = "Pass@1234"
        self.database = "user_database"

    def _manage_connection(func):
        """Decorator to manage database connection and cursor."""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            try:
                result = func(self, *args, **kwargs)
                self.connection.commit()
                return result
            except mysql.connector.Error as err:
                print(f"Database Error: {err}")
                self.connection.rollback()
            finally:
                self.cursor.close()
                self.connection.close()
                print("Database connection closed.")
        return wrapper

    @_manage_connection
    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS sosDetails (
                userId INT PRIMARY KEY,
                phoneNo1 BIGINT,
                phoneNo2 BIGINT,
                phoneNo3 BIGINT,
                phoneNo4 BIGINT,
                phoneNo5 BIGINT,
                email1 VARCHAR(255),
                email2 VARCHAR(255),
                email3 VARCHAR(255),
                email4 VARCHAR(255),
                email5 VARCHAR(255)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS userLogin (
                userId INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL UNIQUE,
                phoneNo BIGINT NOT NULL,
                password VARCHAR(255) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS userBasicDetails (
                userId INT PRIMARY KEY,
                tag CHAR(1),
                firstName VARCHAR(255),
                middleName VARCHAR(255),
                lastName VARCHAR(255),
                dob DATE,
                disabilityStatus BINARY,
                bloodGroup VARCHAR(5),
                FOREIGN KEY (userId) REFERENCES userLogin(userId)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS userAddress (
                userId INT PRIMARY KEY,
                permanentAddress VARCHAR(255),
                permanentLandMark VARCHAR(255),
                permanentCity VARCHAR(100),
                permanentPinCode SMALLINT,
                permanentDistrict VARCHAR(100),
                permanentState VARCHAR(100),
                permanentCountry VARCHAR(100),
                currentAddress VARCHAR(255),
                currentLandmark VARCHAR(255),
                currentCity VARCHAR(100),
                currentPinCode SMALLINT,
                currentDistrict VARCHAR(100),
                currentState VARCHAR(100),
                currentCountry VARCHAR(100),
                FOREIGN KEY (userId) REFERENCES userLogin(userId)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS userLocation (
                userId INT PRIMARY KEY,
                latitude VARCHAR(50),
                longitude VARCHAR(50),
                FOREIGN KEY (userId) REFERENCES userLogin(userId)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS userTickets (
                userId INT,
                latitude VARCHAR(50),
                longitude VARCHAR(50),
                status BINARY,
                PRIMARY KEY (userId, latitude, longitude),
                FOREIGN KEY (userId) REFERENCES userLogin(userId)
            );
            """
        ]

        for query in queries:
            self.cursor.execute(query)
        print("Tables created successfully.")

    @_manage_connection
    def register_user(self, email, phoneNo, password, basic_details, sos_details):
        # Insert into userLogin and fetch userId
        login_query = """
        INSERT INTO userLogin (email, phoneNo, password)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(login_query, (email, phoneNo, password))
        userId = self.cursor.lastrowid  # Fetch the auto-generated userId
        print(f"User login created with userId: {userId}")

        # Insert into userBasicDetails
        basic_query = """
        INSERT INTO userBasicDetails (
            userId, tag, firstName, middleName, lastName, dob, disabilityStatus, bloodGroup
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(basic_query, (
            userId,
            basic_details["tag"],
            basic_details["firstName"],
            basic_details["middleName"],
            basic_details["lastName"],
            basic_details["dob"],
            basic_details["disabilityStatus"],
            basic_details["bloodGroup"]
        ))
        print("User basic details inserted successfully.")

        # Insert into sosDetails
        sos_query = """
        INSERT INTO sosDetails (
            userId, phoneNo1, phoneNo2, phoneNo3, phoneNo4, phoneNo5,
            email1, email2, email3, email4, email5
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sos_query, (
            userId,
            sos_details["phoneNo1"],
            sos_details["phoneNo2"],
            sos_details["phoneNo3"],
            sos_details["phoneNo4"],
            sos_details["phoneNo5"],
            sos_details["email1"],
            sos_details["email2"],
            sos_details["email3"],
            sos_details["email4"],
            sos_details["email5"]
        ))
        print("SOS details inserted successfully.")


