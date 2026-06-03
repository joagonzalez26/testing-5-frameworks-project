from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url="http://localhost:5173"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self, path="/"):
        self.driver.get(f"{self.base_url}{path}")
        self.wait_for_page_loaded()

    def wait_for_page_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def get_body_text(self):
        self.wait_for_page_loaded()
        return self.driver.find_element(By.TAG_NAME, "body").text

    def page_contains(self, text):
        return text.lower() in self.get_body_text().lower()

    def click_menu_option(self, text):
        xpath = (
            f"//a[contains(normalize-space(.), '{text}')]"
            f" | //button[contains(normalize-space(.), '{text}')]"
            f" | //div[contains(normalize-space(.), '{text}')]"
        )

        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        element.click()
        self.wait_for_page_loaded()

    def count_tables(self):
        return len(self.driver.find_elements(By.TAG_NAME, "table"))

    def count_table_rows(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        return len(rows)

    def current_url_contains(self, text):
        return text.lower() in self.driver.current_url.lower()

    def take_screenshot(self, name):
        screenshots_dir = Path("framework-2-selenium/evidencias")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        path = screenshots_dir / name
        self.driver.save_screenshot(str(path))

        return path