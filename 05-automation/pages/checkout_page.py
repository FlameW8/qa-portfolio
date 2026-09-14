class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.zip_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.mensaje_confirmacion = page.locator(".complete-header")

    def ir_a_checkout(self):
        self.checkout_button.click()

    def completar_datos(self, nombre, apellido, codigo_postal):
        self.first_name_input.fill(nombre)
        self.last_name_input.fill(apellido)
        self.zip_input.fill(codigo_postal)
        self.continue_button.click()

    def finalizar_compra(self):
        self.finish_button.click()