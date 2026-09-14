class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.usuario_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.boton_login = page.locator("#login-button")
        self.mensaje_error = page.locator("[data-test='error']")

    def ir_a_la_pagina(self):
        self.page.goto(self.url)

    def login(self, usuario, password):
        self.usuario_input.fill(usuario)
        self.password_input.fill(password)
        self.boton_login.click()