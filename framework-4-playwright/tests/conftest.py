from pathlib import Path

import pytest


@pytest.fixture
def app_page(page, request):
    page.set_viewport_size({"width": 1440, "height": 900})
    request.node.page = page

    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = getattr(item, "page", None)

        if page:
            screenshots_dir = Path("framework-4-playwright/evidencias/fallos")
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            screenshot_path = screenshots_dir / f"{item.name}.png"

            try:
                page.screenshot(path=str(screenshot_path), full_page=True)
                print(f"\nCaptura guardada por fallo: {screenshot_path}")
            except Exception as error:
                print(f"\nNo se pudo guardar captura del fallo: {error}")