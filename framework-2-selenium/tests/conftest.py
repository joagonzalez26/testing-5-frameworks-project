from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            screenshots_dir = Path("framework-2-selenium/evidencias/fallos")
            screenshots_dir.mkdir(parents=True, exist_ok=True)

            screenshot_name = f"{item.name}.png"
            screenshot_path = screenshots_dir / screenshot_name

            driver.save_screenshot(str(screenshot_path))

            print(f"\nCaptura guardada por fallo: {screenshot_path}")