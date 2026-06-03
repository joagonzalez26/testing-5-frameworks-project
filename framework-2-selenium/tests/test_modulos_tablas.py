import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.base_page import BasePage


@pytest.mark.parametrize(
    "modulo,nombre_captura",
    [
        ("Participantes", "selenium-tabla-participantes.png"),
        ("Salas", "selenium-tabla-salas.png"),
        ("Reservas", "selenium-tabla-reservas.png"),
    ],
)
def test_modulos_principales_muestran_tablas(driver, modulo, nombre_captura):
    page = BasePage(driver)

    page.open("/")
    page.click_menu_option(modulo)

    page.take_screenshot(nombre_captura)

    assert page.page_contains(modulo)
    assert page.count_tables() >= 1
    assert page.count_table_rows() >= 1


def test_reportes_carga_con_contenido_visible(driver):
    page = BasePage(driver)

    page.open("/")
    page.click_menu_option("Reportes")

    page.take_screenshot("selenium-reportes-contenido.png")

    assert page.page_contains("Reportes")