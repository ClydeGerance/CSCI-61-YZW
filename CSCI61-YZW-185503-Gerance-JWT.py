import requests

def verify_api(auth_key):
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users"
    requests.get(url, headers={"Authorization": f"Bearer {auth_key}"})

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

def add_user(auth_key):
    url = "https://user-api-1045581321523.asia-southeast1.run.app/api/v1/users"
    headers = {
        "Authorization": f"Bearer {auth_key}",
        "Content-Type": "application/json"
    }
    user_data = {
        "email": "clyde.gerance@student.ateneo.edu",
        "username": "clydelester2",
        "password": "clydelester2"
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
        verify_api(access_token)
        add_user(access_token)
    except Exception as err:
        print(f"Unexpected Issue: {err}")
