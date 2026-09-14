import sys
sys.path.append('..')
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import Page, expect

def test_checkout_completo(page: Page):
    login_page = LoginPage(page)
    login_page.ir_a_la_pagina()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.agregar_producto_al_carrito("Sauce Labs Backpack")
    inventory_page.ir_al_carrito()

    checkout_page = CheckoutPage(page)
    checkout_page.ir_a_checkout()
    checkout_page.completar_datos("Adrian", "Urunaga", "1234")
    checkout_page.finalizar_compra()

    expect(checkout_page.mensaje_confirmacion).to_have_text("Thank you for your order!")