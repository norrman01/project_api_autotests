import sender_stand_request
import data

def get_new_user_token():
    user_token = sender_stand_request.post_new_user(data.user_body).json()["authToken"]
    data.authorization["Authorization"] = "Bearer " + user_token

def test_autorization_user():
    get_new_user_token()
def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name

def positive_assert(kit_body):
    kit_name = get_kit_body(kit_body)
    user_response = sender_stand_request.post_new_client_kit(kit_name)
    assert user_response.status_code == 201
    assert user_response.json()["name"] != ""

def test_create_kit_body_1_letter_in_name():
    positive_assert("a")

def test_create_kit_body_511_letter_in_name():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def negative_assert_code_400(kit_body):
    kit_name = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(kit_name)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def test_create_kit_body_0_letter_in_name():
    negative_assert_code_400("")

def test_create_kit_body_512_letter_in_name():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_body_english_letter_in_name():
    positive_assert("QWErty")

def test_create_kit_body_russian_letter_in_name():
    positive_assert("Мария")

def test_create_kit_body_special_symbol_in_name():
    positive_assert("\"№%@\",")

def test_create_kit_body_has_space_in_name():
    positive_assert(" Человек и КО ")

def test_create_kit_body_has_number_in_name():
    positive_assert("123")

def negative_assert_no_name(kit_name):
    response = sender_stand_request.post_new_client_kit(kit_name)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

def test_create_kit_body_no_name():
    current_name = data.kit_body.copy()
    current_name.pop("name")
    negative_assert_no_name(current_name)

def test_create_kit_body_number_in_name():
    current_name = get_kit_body(12)
    response = sender_stand_request.post_new_client_kit(current_name)
    assert response.status_code == 400