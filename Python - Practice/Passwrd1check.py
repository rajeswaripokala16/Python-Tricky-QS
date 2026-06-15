# Secure password storage and verification with bcrypt
# Install bcrypt first: pip install bcrypt

import bcrypt

# 1) Create & store a hashed password (run once when setting the password)
def create_hashed_password(plain_password: str) -> bytes:
    # bcrypt.gensalt() chooses a secure salt and cost factor
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed

# Example: store this 'hashed_password' in your database securely
# hashed_password = create_hashed_password("MySecret123")
# print(hashed_password)

# 2) Verify user input against stored hashed password
def verify_password(plain_password: str, stored_hashed: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), stored_hashed)

if __name__ == "__main__":
    # Example: pretend this is the hashed password loaded from DB
    # (create it first and paste the printed bytes here, or store persistently)
    stored_hashed_password = b"$2b$12$e0N0u1y...replace_with_actual_hash..."  # replace with real hash

    user_input = input("Enter your password: ")

    if verify_password(user_input, stored_hashed_password):
        print("Access granted ✅")
    else:
        print("Access denied ❌")
