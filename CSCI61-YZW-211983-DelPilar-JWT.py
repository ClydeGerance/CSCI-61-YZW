import requests

def fetch_token():
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users/login"
    response = requests.post(url, json={
        "username": "csci61-user", 
        "password": "be$super$secure@discs"
    })
    return response.json().get("token")

def register_user(auth_token):
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users"
    headers = {
        "Authorization": f"Bearer {auth_token}", 
        "Content-Type": "application/json"
    }
    data = {
        "email": "fritzie.delpilar@student.ateneo.edu", 
        "username": "diannedp2", 
        "password": "diannedp2"
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code ==200:
        print("User created successfully!")
        print( "Response", response.text)

    else:
        print("Failed to create user.")

if __name__ == "__main__":
    register_user(fetch_token())