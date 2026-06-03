from pathlib import Path

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str = "http://localhost:5173"):
        self.page = page
        self.base_url = base_url

    def open_home(self):
        self.page.goto(self.base_url)
        expect(self.page.locator("body")).to_contain_text("Dashboard")

    def body(self):
        return self.page.locator("body")

    def expect_text(self, text: str):
        expect(self.body()).to_contain_text(text)

    def click_text(self, text: str):
        self.page.locator(f"text={text}").first.click()

    def count_tables(self):
        return self.page.locator("table").count()

    def expect_table_visible(self):
        expect(self.page.locator("table")).to_have_count(1)
        expect(self.page.locator("table tbody tr").first).to_be_visible()

    def take_screenshot(self, name: str):
        screenshots_dir = Path("framework-4-playwright/evidencias")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        path = screenshots_dir / name
        self.page.screenshot(path=str(path), full_page=True)

        return path