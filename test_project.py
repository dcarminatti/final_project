from project import (
    create_user_data_table,
    login,
    register_user_data_table,
    search_user_data_table,
    singup,
)
import os, csv


def test_singup():
    create_user_data_table()
    # Successful singup
    email = "example.dev@domain.com"
    pwd = "123456"
    conf_pwd = "123456"
    assert singup(email, pwd, conf_pwd) == "You have registered successfully!"
    # Unsuccessful singup, if the user has already been registered
    assert singup(email, pwd, conf_pwd) == "Already registered user!"

    # Unsuccessful singup, if the passwords are not the same
    conf_pwd = "123"
    assert singup(email, pwd, conf_pwd) == "Passwords do not match!"

    os.remove("credentials.csv")


def test_login():
    create_user_data_table()
    # Successful login
    email = "example.dev@domain.com"
    pwd = "123456"
    conf_pwd = "123456"
    singup(email, pwd, conf_pwd)
    assert login(email, pwd) == "Login in Successfully!"

    # Unsuccessful login
    pwd = "12345"
    assert login(email, pwd) == "Please review the information you entered!"

    os.remove("credentials.csv")


def test_create_user_data_table():
    create_user_data_table()
    assert os.path.exists("credentials.csv")

    os.remove("credentials.csv")


def test_search_user_data_table():
    create_user_data_table()
    user = {"email": "example.dev@domain.com", "pwd": "123456"}

    with open("credentials.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "pwd"])
        writer.writerow(user)

    assert search_user_data_table(user)

    os.remove("credentials.csv")


def test_register_user_data_table():
    create_user_data_table()
    user = {"email": "example.dev@domain.com", "pwd": "123456"}
    register_user_data_table(user)
    assert search_user_data_table(user)

    os.remove("credentials.csv")
