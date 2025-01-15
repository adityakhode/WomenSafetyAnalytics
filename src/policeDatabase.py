# import mysql.connector

# class POLICE:
#     def __init__(self, host, user, password, database):
#         # Establishing the connection to the MySQL database
#         self.connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Pass@1234",
#             database="police_database"
#         )
#         self.cursor = self.connection.cursor()

#     # Method to create the login and policeStationDetails tables
#     def create(self):
#         try:
#             # Creating the login table for police stations
#             self.cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS login (
#                     policeStationId INT PRIMARY KEY AUTO_INCREMENT,
#                     phoneNo INT NOT NULL UNIQUE,
#                     email VARCHAR(255) NOT NULL UNIQUE,
#                     password VARCHAR(255) NOT NULL
#                 );
#             """)
#             print("Police login table created successfully!")

#             # Creating the policeStationDetails table
#             self.cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS policeStationDetails (
#                     policeStationId INT PRIMARY KEY,
#                     stationAddress VARCHAR(255) NOT NULL,
#                     stationCity VARCHAR(100) NOT NULL,
#                     stationState VARCHAR(100) NOT NULL,
#                     stationCountry VARCHAR(100) NOT NULL,
#                     policeChiefIdProof BLOB,
#                     chiefName VARCHAR(255) NOT NULL,
#                     chiefContactNo INT NOT NULL,
#                     FOREIGN KEY (policeStationId) REFERENCES login(policeStationId)
#                 );
#             """)
#             print("Police station details table created successfully!")

#             self.connection.commit()
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#             self.connection.rollback()

#     # Method to insert login details into the 'login' table
#     def insert_login(self, phoneNo, email, password):
#         try:
#             query = """
#                 INSERT INTO login (phoneNo, email, password)
#                 VALUES (%s, %s, %s);
#             """
#             self.cursor.execute(query, (phoneNo, email, password))
#             self.connection.commit()
#             print("Police station login details inserted successfully!")
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#             self.connection.rollback()

#     # Method to insert police station details into the 'policeStationDetails' table
#     def insert_station_details(self, policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo):
#         try:
#             query = """
#                 INSERT INTO policeStationDetails (policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
#             """
#             self.cursor.execute(query, (policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo))
#             self.connection.commit()
#             print("Police station registration details inserted successfully!")
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
#             self.connection.rollback()

#     # Method to close the connection
#     def close_connection(self):
#         self.cursor.close()
#         self.connection.close()
#         print("Database connection closed.")

# # Example usage:
# if __name__ == "__main__":
#     # Initialize the POLICE class with your database credentials
#     police = POLICE(host="localhost", user="root", password="Pass@1234", database="policeDB")

#     # Create the tables
#     police.create()

#     # Insert data into the 'login' table
#     police.insert_login(phoneNo=9876543210, email="police@station.com", password="securepassword")

#     # Insert data into the 'policeStationDetails' table (Example)
#     chief_id_proof = None  # Example: You can replace None with an actual binary image data.
#     police.insert_station_details(
#         policeStationId=1,
#         stationAddress="456, Main Road",
#         stationCity="Citytown",
#         stationState="Stateland",
#         stationCountry="Countryland",
#         policeChiefIdProof=chief_id_proof,
#         chiefName="John Doe",
#         chiefContactNo=9876543210
#     )

#     # Close the connection after operations are done
#     police.close_connection()
import mysql.connector

class POLICE:
    def __init__(self, host, user, password, database):
        # Establishing the connection to the MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pass@1234",
            database="policestation_database"
        )
        self.cursor = self.connection.cursor()

    # Method to create the login and registration tables
    def create(self):
        try:
            # Creating the login table for police stations
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS login (
                    policeStationId INT PRIMARY KEY AUTO_INCREMENT,
                    phoneNo INT NOT NULL UNIQUE,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                );
            """)
            print("Login table created successfully!")

            # Creating the policeStationDetails table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS policeStationDetails (
                    policeStationId INT PRIMARY KEY,
                    stationAddress VARCHAR(255) NOT NULL,
                    stationCity VARCHAR(100) NOT NULL,
                    stationState VARCHAR(100) NOT NULL,
                    stationCountry VARCHAR(100) NOT NULL,
                    policeChiefIdProof BLOB,
                    chiefName VARCHAR(255) NOT NULL,
                    chiefContactNo INT NOT NULL,
                    pincode INT NOT NULL,  -- Added pincode column
                    FOREIGN KEY (policeStationId) REFERENCES login(policeStationId)
                );
            """)
            print("Police station details table created successfully!")

            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Method to insert login details into the 'login' table
    def insert_login(self, phoneNo, email, password):
        try:
            query = """
                INSERT INTO login (phoneNo, email, password)
                VALUES (%s, %s, %s);
            """
            self.cursor.execute(query, (phoneNo, email, password))
            self.connection.commit()
            print("Login details inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Method to insert police station details into the 'policeStationDetails' table
    def insert_registration(self, policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo, pincode):
        try:
            query = """
                INSERT INTO policeStationDetails (policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo, pincode)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            self.cursor.execute(query, (policeStationId, stationAddress, stationCity, stationState, stationCountry, policeChiefIdProof, chiefName, chiefContactNo, pincode))
            self.connection.commit()
            print("Police station registration details inserted successfully!")
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
    # Initialize the POLICE class with your database credentials
    police = POLICE(host="localhost", user="root", password="Pass@1234", database="policeDB")

    # Create the tables
    police.create()

    # Insert data into the 'login' table
    police.insert_login(phoneNo=1234567890, email="police@station.com", password="securepassword")

    # Insert data into the 'policeStationDetails' table (Example)
    police_chief_id_proof = None  # Example: You can replace None with an actual binary image data.
    police.insert_registration(
        policeStationId=1,
        stationAddress="456, Police Lane",
        stationCity="Cityville",
        stationState="Stateland",
        stationCountry="Countryland",
        policeChiefIdProof=police_chief_id_proof,
        chiefName="John Doe",
        chiefContactNo=9876543210,
        pincode=123456
    )

    # Close the connection after operations are done
    police.close_connection()
