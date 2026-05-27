import bcrypt
import jwt
import os
from dotenv import load_dotenv
from db.mongo import db

load_dotenv()

SECRET = os.getenv("JWT_SECRET")

users = db["users"]


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def create_user(name, email, password):
    existing_user = users.find_one({"email": email})

    if existing_user:
        return False, "User already exists"

    hashed = hash_password(password)

    users.insert_one({
        "name": name,
        "email": email,
        "password": hashed
    })

    return True, "User created successfully"


def login_user(email, password):
    user = users.find_one({"email": email})

    if not user:
        return False, "User not found"

    if verify_password(password, user["password"]):
        token = jwt.encode(
            {"email": user["email"]},
            SECRET,
            algorithm="HS256"
        )

        return True, {
            "user": user,
            "token": token
        }

    return False, "Invalid password"

def login_after_registration(email):
    user = users.find_one({"email": email})

    if not user:
        return None

    token = jwt.encode(
        {"email": user["email"]},
        SECRET,
        algorithm="HS256"
    )

    return {
        "user": user,
        "token": token
    }

def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )

        user = users.find_one({"email": payload["email"]})

        return user

    except:
        return None