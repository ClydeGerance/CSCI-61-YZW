import requests
import random
import jwt
from jwt.exceptions import InvalidTokenError
from cryptography.hazmat.primitives import serialization

def verify_api(auth_key):
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users"
    response = requests.options(url, headers={"Authorization": f"Bearer {auth_key}"})
    print(f"API Verification Response: {response.status_code} - {response.text}")

def retrieve_token():
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users/login"
    response = requests.post(url, json={
        "username": "csci61-user",
        "password": "be$super$secure@discs"
    })

    if response.status_code == 200:
        token = response.json().get("token")
        print(f"Access Key: {token}")
        return token

    print(f"Token Retrieval Failed: {response.status_code} - {response.text}")
    return None

PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEIewCqnkh6rSoBD401ARa4ET433RRsUKl
P3uX1oilx7b+BLB9utbG7J9/0u2KFwrhZ2ScqOpst3qCftmynIxet84MXdRabps2
3gR1C9Gjh140di/Y1W5Wwud9n+vCsSIS
-----END PUBLIC KEY-----
"""

def validate_jwt(token):
    try:
        decoded_no_verify = jwt.decode(token, options={"verify_signature": False})
        print("Decoded Token (No Verification):", decoded_no_verify)

        public_key = serialization.load_pem_public_key(PUBLIC_KEY.encode())
        
        decoded_token = jwt.decode(token, public_key, algorithms=["ES384"])
        print("Token is valid:", decoded_token)
        return decoded_token
    except InvalidTokenError as e:
        print("Invalid token:", e)
        return None
    except Exception as err:
        print("Unexpected JWT Error:", err)
        return None

def add_user(auth_key):
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users"
    headers = {
        "Authorization": f"Bearer {auth_key}",
        "Content-Type": "application/json"
    }
    user_data = {
        "email": "clyde.gerance@student.ateneo.edu",
        "username": f"clydegerance{random.randint(1000,9999)}",
        "password": "clydegerance"
    }

    response = requests.post(url, json=user_data, headers=headers)

    if response.status_code in [200, 201]:
        print("User added successfully!")
    else:
        print(f"Response Code: {response.status_code} | Message: {response.text}")
        try:
            print(f"Error Details: {response.json()}")
        except:
            print(f"Malformed Response: {response.text}")

if __name__ == "__main__":
    try:
        access_token = retrieve_token()
        if access_token:
            validate_jwt(access_token)
            verify_api(access_token)
            add_user(access_token)
    except Exception as err:
        print(f"Unexpected Issue: {err}")


# Guide Questions and Answers:
# 1. Is it safe to share this public key with you? Why or why not?
#    Yes, it is safe because public keys are meant to be shared. 
#    They are used to verify JWT signatures but cannot be used to sign or generate new tokens. 
#    The security of the system relies on keeping the private key secret.

# 2. Can this key be used to generate a valid JWT token? Expound on your answer.
#    No, this public key cannot generate a valid JWT token. JWTs are signed using a private key, which remains secret. 
#    The public key can only verify the signature of an already signed token, ensuring that it was issued by the legitimate private key owner.

# 3. How can this be used in real-world application development?
#    In real-world applications, JWT verification ensures API requests are authenticated. 
#    The server signs JWTs using a private key, and clients (or other services) verify them using the public key. 
#    This allows secure, stateless authentication without exposing secrets or requiring session storage. 
#    It is commonly used in OAuth, OpenID Connect, and microservices authentication.