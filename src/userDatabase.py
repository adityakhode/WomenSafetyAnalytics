import mysql.connector

class USER:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pass@1234",
            database="user_database"
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS sosDetails (
                userId INT PRIMARY KEY,
                phoneNo1 INT,
                phoneNo2 INT,
                phoneNo3 INT,
                phoneNo4 INT,
                phoneNo5 INT,
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
                phoneNo INT NOT NULL,
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
        self.connection.commit()
        print("Tables created successfully.")

    def insert_user_login(self, email, phoneNo, password):
        query = """
        INSERT INTO userLogin (email, phoneNo, password)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (email, phoneNo, password))
        self.connection.commit()
        print("User login data inserted successfully.")

    def insert_sos_details(self, userId, phones, emails):
        query = """
        INSERT INTO sosDetails (
            userId, phoneNo1, phoneNo2, phoneNo3, phoneNo4, phoneNo5,
            email1, email2, email3, email4, email5
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (userId, *phones, *emails))
        self.connection.commit()
        print("SOS details inserted successfully.")

    def insert_user_basic_details(self, userId, tag, firstName, middleName, lastName, dob, disabilityStatus, bloodGroup):
        query = """
        INSERT INTO userBasicDetails (
            userId, tag, firstName, middleName, lastName, dob, disabilityStatus, bloodGroup
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (userId, tag, firstName, middleName, lastName, dob, disabilityStatus, bloodGroup))
        self.connection.commit()
        print("User basic details inserted successfully.")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")


# Example usage:
if __name__ == "__main__":
    db = USER(host="localhost", user="root", password="Pass@1234", database="user_database")
    db.create_tables()
    db.insert_user_login("example@example.com", 1234567890, "securepassword")
    db.insert_sos_details(1, [1111111111, 2222222222, 3333333333, 4444444444, 5555555555],
                          ["email1@example.com", "email2@example.com", "email3@example.com", "email4@example.com", "email5@example.com"])
    db.insert_user_basic_details(1, "M", "John", "A.", "Doe", "1990-01-01", 0, "O+")
    db.close_connection()
