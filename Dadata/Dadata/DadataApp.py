from dadata import Dadata
from database import create_database, get_language, get_token, insert_userdata

url = "https://dadata.ru/"
create_database()

user_language = get_language()
if user_language == None:
    user_language = input("Выберите язык / Choose language (ru/en): ")
    if user_language != "ru" and user_language != "en":
        user_language = "ru"
else:
    user_language = user_language[0]

token = get_token()
if token == None:
    bool_var = False
    while bool_var == False: #проверка токена пользователя
        try:
            value = ""
            token = input("Введите API ключ: ") if user_language == "ru" else input("Enter API key:")
            dadata = Dadata(token)
            userdata = (url, token, user_language)
            result = dadata.suggest("address", query=value)
            bool_var = True
            insert_userdata(userdata)
        except:
            print("Неверный API ключ ") if user_language == "ru" else print("Invalid API key")
else:
    token = token[0]
    dadata = Dadata(token)

print("Для завершения программы введите 0") if user_language == "ru" else print("Enter 0 for completion of the program")

while True: #пока пользователь не вышел из интерфейса идет исполнение программы
    value = input("Введите адрес: ") if user_language == "ru" else input("Enter address: ")
    if value == "0":
        break
    else:
        result = dadata.suggest(name = "address", query=value, language = user_language)
        if not result:
            print("Адрес не найден") if user_language == "ru" else print("Address is not found")
        else:
            for i in result:
                print(result.index(i) + 1, " - ", i['value'])
            value_of_address = 0

            while value_of_address not in range(1,11):
                value_of_address = int(input("Введите цифру, соответствующую адресу: ")) if user_language == "ru" else int(input("Enter the number corresponding to the address:"))
                if value_of_address not in range(1,11):
                    pass
            else:
                value_of_address = value_of_address - 1
                print(result[value_of_address]['value'])
                if (result[value_of_address]['data']['geo_lon'] != None) and (result[value_of_address]['data']['geo_lat'] != None):
                    print(f"{result[value_of_address]['data']['geo_lat']}, {result[value_of_address]['data']['geo_lon']}")
                else:
                    print("Координаты не найдены") if user_language == "ru" else print("Coordinates are not found")



