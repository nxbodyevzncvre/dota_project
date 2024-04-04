# Предположим, что у вас есть текстовый файл с именем "credentials.txt",
# где логин и пароль разделены пробелом и каждая пара находится на новой строке.
# Пример содержимого файла:
# user1 password1
# user2 password2

# Этот код считывает первую строку из файла и сохраняет логин и пароль в переменные.
def read_details(file_name):
    dict = {"login" : [],
            "password" : []}
    with open(file_name, "r") as file:
        for line in file:  # Считываем первую строку
            login, password = line.strip().split()  # Разделяем строку на логин и пароль
            dict["login"].append(login)
            dict["password"].append(password)
    return dict
