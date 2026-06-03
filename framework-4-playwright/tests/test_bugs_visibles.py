import sys
from pathlib import Path

from playwright.sync_api import expect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.sistema_page import SistemaPage


def test_dashboard_muestra_error_horarios_demandados(app_page):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.validar_error_dashboard_horarios()
    sistema.take_screenshot("playwright-dashboard-error-horarios.png")


def test_sanciones_muestra_error_failed_to_fetch(app_page):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.validar_error_sanciones()
    sistema.take_screenshot("playwright-sanciones-error.png")


def test_reportes_muestra_metricas_incompletas(app_page):
    sistema = SistemaPage(app_page)

    sistema.open_home()
    sistema.ir_a_modulo("Reportes")
    sistema.take_screenshot("playwright-reportes-na.png")

    expect(sistema.body()).to_contain_text("Reportes")
    expect(sistema.body()).to_contain_text("N/A")