import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.base_page import BasePage


def test_frontend_carga_correctamente(driver):
    page = BasePage(driver)

    page.open("/")

    page.take_screenshot("selenium-frontend-home.png")

    assert page.page_contains("Dashboard") or page.page_contains("Sistema")


def test_navegacion_modulos_principales(driver):
    page = BasePage(driver)

    page.open("/")

    modulos = [
        "Participantes",
        "Salas",
        "Reservas",
        "Reportes",
    ]

    for modulo in modulos:
        page.click_menu_option(modulo)
        page.take_screenshot(f"selenium-{modulo.lower()}.png")

        assert page.page_contains(modulo)