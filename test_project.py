
from project import registrar_usuario, iniciar_sesion, mostrar_menu_principal

# Prueba para registrar_usuario
def test_registrar_usuario(monkeypatch):
    inputs = iter(["user123", "password123"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    nombre, clave = registrar_usuario()
    assert nombre == "user123"
    assert clave == "password123"

# Prueba para iniciar_sesion
def test_iniciar_sesion(monkeypatch):
    inputs = iter(["password123", "wrong_password", "password123"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert iniciar_sesion("user123", "password123") is None

# Prueba para mostrar_menu_principal
def test_mostrar_menu_principal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert mostrar_menu_principal() == "1"
