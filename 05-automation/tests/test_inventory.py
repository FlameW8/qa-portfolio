import sys
sys.path.append('..')
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect

def test_agregar_producto_al_carrito(page: Page):
    login_page = LoginPage(page)
    login_page.ir_a_la_pagina()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.agregar_producto_al_carrito("Sauce Labs Backpack")

    expect(inventory_page.contador_carrito).to_have_text("1")