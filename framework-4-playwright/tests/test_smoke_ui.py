import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.sistema_page import SistemaPage


def test_frontend_carga_correctamente(app_page):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.take_screenshot("playwright-frontend-home.png")

    sistema.validar_dashboard()