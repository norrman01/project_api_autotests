import sender_stand_request
import data

#данная функция создает пользователя и записывает токкен в data.authorization
#но дергать её надо только один раз, так как нужен один зарег. пользователь,
#поэтому в начале test_, что бы она с самого начала запустилась, и на весь
#ход тестов был один токкен.
def test_new_user_token():
    user_token = sender_stand_request.post_new_user(data.user_body).json()["authToken"]
    data.authorization["Authorization"] = "Bearer " + user_token

#данная функция меняет name в kit_body
def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name

#это настройки позитивной проверки. проверка на код 201 и на совпадение name
def positive_assert(kit_body):
    kit_name = get_kit_body(kit_body)
    user_response = sender_stand_request.post_new_client_kit(kit_name)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == kit_name["name"]

#это настройки негативной проверки и проверка кода 400
def negative_assert_code_400(kit_body):
    kit_name = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(kit_name)
    assert response.status_code == 400
    assert response.json()["code"] == 400

#test1 - Допустимое количество символов (1)
def test_create_kit_body_1_letter_in_name():
    positive_assert("a")

#test2- Допустимое количество символов (511)
def test_create_kit_body_511_letter_in_name():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#test3 - Количество символов меньше допустимого (0)
def test_create_kit_body_0_letter_in_name():
    negative_assert_code_400("")

#test4 - Количество символов больше допустимого (512)
def test_create_kit_body_512_letter_in_name():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#test5 - Разрешены английские буквы
def test_create_kit_body_english_letter_in_name():
    positive_assert("QWErty")

#test6 - Разрешены русские буквы
def test_create_kit_body_russian_letter_in_name():
    positive_assert("Мария")

#test7 - Разрешены спецсимволы
def test_create_kit_body_special_symbol_in_name():
    positive_assert("\"№%@\",")

#test8 - Разрешены пробелы
def test_create_kit_body_has_space_in_name():
    positive_assert(" Человек и КО ")

#test9 - Разрешены цифры
def test_create_kit_body_has_number_in_name():
    positive_assert("123")

#test10 - Параметр не передан в запросе
def test_create_kit_body_no_name():
    current_name = data.kit_body.copy()
    current_name.pop("name")
    negative_assert_code_400(current_name)

#test11 - Передан другой тип параметра (число)
def test_create_kit_body_number_in_name():
    current_name = get_kit_body(12)
    response = sender_stand_request.post_new_client_kit(current_name)
    assert response.status_code == 400