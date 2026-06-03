import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.sistema_page import SistemaPage


@pytest.mark.parametrize(
    "modulo,nombre_captura",
    [
        ("Participantes", "playwright-tabla-participantes.png"),
        ("Salas", "playwright-tabla-salas.png"),
        ("Reservas", "playwright-tabla-reservas.png"),
    ],
)
def test_modulos_principales_muestran_tablas(app_page, modulo, nombre_captura):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.validar_modulo_con_tabla(modulo)
    sistema.take_screenshot(nombre_captura)


def test_reportes_carga_con_contenido_visible(app_page):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.validar_reportes_con_contenido()
    sistema.take_screenshot("playwright-reportes-contenido.png")