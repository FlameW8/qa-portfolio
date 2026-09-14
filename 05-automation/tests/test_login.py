from playwright.sync_api import Page, expect

def test_titulo_saucedemo(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

import sys
sys.path.append('..')
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_login_exitoso(page: Page):
    login_page = LoginPage(page)
    login_page.ir_a_la_pagina()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_credenciales_invalidas(page: Page):
    login_page = LoginPage(page)
    login_page.ir_a_la_pagina()
    login_page.login("usuario_invalido", "clave_invalida")
    expect(login_page.mensaje_error).to_be_visible()