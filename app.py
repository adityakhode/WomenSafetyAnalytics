from src import userDatabase as USER

# Example usage
if __name__ == "__main__":
    db = USER(host="localhost", user="root", password="Pass@1234", database="user_database")
    
    # Create tables
    db.create_tables()

    # Register a user
    basic_details = {
        "tag": "M",
        "firstName": "John",
        "middleName": "A.",
        "lastName": "Doe",
        "dob": "1990-01-01",
        "disabilityStatus": 0,
        "bloodGroup": "O+"
    }
    sos_details = {
        "phoneNo1": 1111111111,
        "phoneNo2": 2222222222,
        "phoneNo3": 3333333333,
        "phoneNo4": 4444444444,
        "phoneNo5": 5555555555,
        "email1": "email1@example.com",
        "email2": "email2@example.com",
        "email3": "email3@example.com",
        "email4": "email4@example.com",
        "email5": "email5@example.com"
    }

    db.register_user("example4@example.com", 9876543210, "securepassword", basic_details, sos_details)

