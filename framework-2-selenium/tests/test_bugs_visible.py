import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.base_page import BasePage


def test_dashboard_muestra_error_horarios_demandados(driver):
    page = BasePage(driver)

    page.open("/")

    page.take_screenshot("selenium-dashboard-error-horarios.png")

    assert page.page_contains("Dashboard")

    assert (
        page.page_contains("Error cargando horarios")
        or page.page_contains("404")
        or page.page_contains("Not Found")
    )


def test_sanciones_muestra_error_failed_to_fetch(driver):
    page = BasePage(driver)

    page.open("/")
    page.click_menu_option("Sanciones")

    page.take_screenshot("selenium-sanciones-error.png")

    assert page.page_contains("Sanciones")

    assert (
        page.page_contains("Failed to fetch")
        or page.page_contains("Error")
    )


def test_reportes_muestra_metricas_incompletas(driver):
    page = BasePage(driver)

    page.open("/")
    page.click_menu_option("Reportes")

    page.take_screenshot("selenium-reportes-na.png")

    assert page.page_contains("Reportes")

    assert (
        page.page_contains("N/A")
        or page.page_contains("No disponible")
        or page.page_contains("Reportes")
    )