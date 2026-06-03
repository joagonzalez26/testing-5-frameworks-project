from playwright.sync_api import expect

from pages.base_page import BasePage


class SistemaPage(BasePage):
    def ir_a_modulo(self, modulo: str):
        self.click_text(modulo)
        self.expect_text(modulo)

    def validar_dashboard(self):
        self.expect_text("Dashboard")

    def validar_modulo_con_tabla(self, modulo: str):
        self.ir_a_modulo(modulo)
        self.expect_table_visible()

    def validar_error_dashboard_horarios(self):
        self.validar_dashboard()
        expect(self.body()).to_contain_text("Error cargando horarios")

    def validar_error_sanciones(self):
        self.ir_a_modulo("Sanciones")
        expect(self.body()).to_contain_text("Error")

    def validar_reportes_con_contenido(self):
        self.ir_a_modulo("Reportes")
        self.expect_text("Reportes")