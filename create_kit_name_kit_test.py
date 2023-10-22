import sender_stand_request
import data

# Функция изменения содержимое тела запроса. параметр ame
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#Получение Токена (возникают проблемы пре тетстировании)
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

#Позитивная проверка
def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert kit_response.json()["name"] == kit_body(name)
    assert kit_response.status_code == 201

#Негативная проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert kit_response.status_code == 400

def negative_assert_no_name(kit_body):
	kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
	assert kit_response_negative_no_name.status_code == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assert("a")

# Тест 2. Успешное создание набора. Параметр name состоит из 511 символа
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка. Параметр состоит из 0 символов
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")

# Тест 4. Ошибка. Параметр name состоит из 512 символа
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5 .Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. спешное создание набора. Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')


# Тест 8. Успешное создание набора. Параметр name состоит из слов с пробелами
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора. Параметр name состоит из строки цифр
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр не передан в запросе
def test_create_kit_empty_in_name_get_error_response():
    kit_body = data.kit_body.copy()

    kit_body.pop("name")

    negative_assert_no_name(kit_body)

# Тест 10 Ошибка. Передан другой тип параметра (число)
def test_create_kit_type_number_in_name_get_error_response():
    negative_assert_code_400(123)
