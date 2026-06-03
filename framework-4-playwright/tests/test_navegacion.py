import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.sistema_page import SistemaPage


@pytest.mark.parametrize(
    "modulo,nombre_captura",
    [
        ("Participantes", "playwright-participantes.png"),
        ("Salas", "playwright-salas.png"),
        ("Reservas", "playwright-reservas.png"),
        ("Reportes", "playwright-reportes.png"),
    ],
)
def test_navegacion_modulos_principales(app_page, modulo, nombre_captura):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.ir_a_modulo(modulo)
    sistema.take_screenshot(nombre_captura)

    sistema.expect_text(modulo)