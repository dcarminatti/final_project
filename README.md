# Python Login System

## Video Demo:  
    <URL HERE>

## Description: 
    The Python code implements a basic user registration and login system, storing credentials in a CSV file called "credentials.csv". It uses the hashlib library to create MD5 hashes of passwords, offers a simple text interface for the user to choose between registration, login or exit, and validates user information through queries against the CSV file. The code also uses the tabulate library to present action options in a table format in the user interface. Note that using MD5 for password hashing is not recommended for security purposes.

## How it works

#### Function *create_user_data_table*
- This function is called at the beginning of the program (main) and is responsible for creating a CSV file called "credentials.csv" to store user data.
- The file will have two columns: "email" and "pwd" (password).

#### Function *register_user_data_table*
- This function takes a user dictionary as an argument, containing user information (email and password).
- Checks if the user already exists in the table by calling the search_user_data_table function.
- If the user does not exist, add the user to the CSV file.

#### Function *search_usar_data_table*
- This function takes a user dictionary as an argument, containing user information (email and password).
- Abre o arquivo CSV "credentials.csv" e verifica se o usuário existe na tabela.
- Retorna 1 se o usuário existir e 0 se não existir.
