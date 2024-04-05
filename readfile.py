def read_details(file_name):
    dict = {"login" : [],
            "password" : []}
    with open(file_name, "r") as file:
        for line in file:
            login, password = line.strip().split()
            dict["login"].append(login)
            dict["password"].append(password)
    return dict
