import hashlib, csv
from tabulate import tabulate


def main():
    create_user_data_table()
    while get_inteface():
        get_inteface()


def get_inteface():
    # Creates a table with the actions that can be taken on the login screen
    tab = tabulate(
        [["1", "Singup"], ["2", "Login"], ["3", "Exit"]],
        headers=["Login System"],
        tablefmt="grid",
    )
    try:
        print(tab)
        choice = int(input("Enter your choice: "))
        if choice not in range(1, 4):
            raise ValueError()
    except ValueError:
        print("Wrong choice")
    else:
        if choice == 1:
            email = input("Enter email address: ")
            pwd = input("Enter password: ")
            conf_pwd = input("Confirm password: ")
            output = singup(email, pwd, conf_pwd)
            print(output)
            return 1
        elif choice == 2:
            email = input("Enter email address: ")
            pwd = input("Enter password: ")
            output = login(email, pwd)
            print(output)
            return 1
        else:
            return 0


def create_user_data_table():
    # Creates a data table in a csv file to store users
    with open("credentials.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "pwd"])
        writer.writeheader()


def register_user_data_table(user: dict):
    # Checks if the user already exists in the table
    if search_user_data_table(user):
        return 0
    # If it does not exist, register it in the table and return true
    with open("credentials.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "pwd"])
        writer.writerow(user)

    return 1


def search_user_data_table(user: dict):
    # Checks if the user already exists in the table
    # If it does exist, return true
    # Else return false
    with open("credentials.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row == user:
                return 1

    return 0


def singup(email, pwd, conf_pwd):
    # If password and confirmation password are equal, then the function will hash the confirmation password
    # Else will print error message
    if conf_pwd == pwd:
        # Convert string to byte format
        enc = conf_pwd.encode()
        # Generate an md5 hash of encoded password using the hexdigest() function
        hash_pwd = hashlib.md5(enc).hexdigest()

        # Save the credentials in file called "credentials.csv"
        user = {"email": email, "pwd": hash_pwd}
        if register_user_data_table(user):
            return "You have registered successfully!"
        else:
            return "Already registered user!"
    else:
        return "Passwords do not match!"


def login(email, pwd):
    # Convert string to byte format
    auth = pwd.encode()
    # Generate an md5 hash of encoded password using the hexdigest() function
    auth_pwd = hashlib.md5(auth).hexdigest()
    # Open "credentials.csv" file to validade informations login
    user = {"email": email, "pwd": auth_pwd}
    if search_user_data_table(user):
        return "Login in Successfully!"
    else:
        return "Please review the information you entered!"


if __name__ == "__main__":
    main()
