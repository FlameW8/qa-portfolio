class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.titulo_pagina = page.locator(".title")
        self.carrito_icono = page.locator(".shopping_cart_link")
        self.contador_carrito = page.locator(".shopping_cart_badge")

    def agregar_producto_al_carrito(self, nombre_producto):
        # Convierte "Sauce Labs Backpack" en "add-to-cart-sauce-labs-backpack" (el formato real de los IDs del sitio)
        id_boton = "add-to-cart-" + nombre_producto.lower().replace(" ", "-")
        self.page.locator(f"#{id_boton}").click()

    def ir_al_carrito(self):
        self.carrito_icono.click()