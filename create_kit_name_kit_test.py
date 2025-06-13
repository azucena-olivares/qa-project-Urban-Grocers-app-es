import sender_stand_request
import data
import requests


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name  # Asegúrate de que la clave sea "firstName" con F mayúscula
    return current_body


def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body


# --- MODIFICACIÓN AQUÍ: positive_assert ahora devuelve el authToken ---
def positive_assert_and_get_auth_token(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    print(user_response.content)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()

    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1

    # ¡Devuelve el token de autenticación!
    return user_response.json()["authToken"]
def create_personal_kit(auth_token, kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)

    print(f"\nRespuesta al crear kit '{kit_name}':")
    print(f"Status Code: {kit_response.status_code}")
    try:
        print(f"Response JSON: {kit_response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Response Content: {kit_response.content}")

    assert kit_response.status_code == 201, f"Esperado Status 201 al crear kit, Obtenido {kit_response.status_code}. Contenido: {kit_response.content}"
    assert "id" in kit_response.json(), "El kit creado no devuelve un 'id' en la respuesta."
    assert kit_response.json()["name"] == kit_name, "El nombre del kit en la respuesta no coincide."

    return kit_response


def test_create_a_kit_with_one_character_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "a")

def test_create_a_kit_with_501_characters_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_a_kit_with_zero_characters_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "")

def test_create_a_kit_with_512_characters_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_a_kit_with_special_characters_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "№%@")

def test_create_a_kit_with_space_between_characters_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "A Aaa")

def test_create_a_kit_with_numbers_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, "123")

def test_create_a_kit_without_name_in_the_request():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token,)

def test_create_a_kit_with_numbers_name():
    # --- MODIFICACIÓN AQUÍ: Captura el authToken devuelto ---
    auth_token = positive_assert_and_get_auth_token("Andrea")
    # Pasa el authToken real a la función create_personal_kit
    create_personal_kit(auth_token, 123)