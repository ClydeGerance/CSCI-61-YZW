import crypt
import getpass

def password_checker(username):
    try:
        with open("/etc/shadow") as file:
            for entry in file:
                if entry.startswith(username + ":"):
                    hashed_password = entry.split(":")[1]
                    break
            else:
                print("User not found!")
                return

        input_password = getpass.getpass("Enter password: ")
        salt_value = "$".join(hashed_password.split("$")[:4]) if "$y$" in hashed_password else "$".join(hashed_password.split("$")[:3])

        if crypt.crypt(input_password, salt_value) == hashed_password:
            print("Correct password!")
        else:
            print("Incorrect password!")

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    user_name = input("Enter username: ")
    password_checker(user_name)
