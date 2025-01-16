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

    # Create the userLocation table
    def create_user_location_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS userLocation (
                    userId INT PRIMARY KEY,
                    latitude VARCHAR(50),
                    longitude VARCHAR(50),
                    FOREIGN KEY (userId) REFERENCES userLogin(userId)
                );
            ''')
            self.connection.commit()
            print("User location table created successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()
        
    # Setter for user location
    def set_user_location(self, userId, latitude, longitude):
        try:
            # Check if the record exists
            self.cursor.execute("SELECT * FROM userLocation WHERE userId = %s", (userId,))
            result = self.cursor.fetchone()
            if result:
                # Update the location
                self.cursor.execute('''
                    UPDATE userLocation
                    SET latitude = %s, longitude = %s
                    WHERE userId = %s;
                ''', (latitude, longitude, userId))
                print("User location updated successfully!")
            else:
                # Insert a new location
                self.cursor.execute('''
                    INSERT INTO userLocation (userId, latitude, longitude)
                    VALUES (%s, %s, %s);
                ''', (userId, latitude, longitude))
                print("User location inserted successfully!")
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    # Getter for user location
    def get_user_location(self, userId):
        try:
            self.cursor.execute("SELECT latitude, longitude FROM userLocation WHERE userId = %s", (userId,))
            result = self.cursor.fetchone()
            if result:
                print(f"User Location - Latitude: {result[0]}, Longitude: {result[1]}")
                return result
            else:
                print("No location found for the given user ID.")
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    # Close connection
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    user_db = USER(host="localhost", user="root", password="Pass@1234", database="user_database")

    # Create the userLocation table
    user_db.create_user_location_table()
    
    # Set user location
    user_db.set_user_location(userId=1, latitude="37.7749", longitude="-122.4194")  # Example coordinates for San Francisco
    
    # Get user location
    user_db.get_user_location(userId=1)
    
    # Close the connection
    user_db.close_connection()
