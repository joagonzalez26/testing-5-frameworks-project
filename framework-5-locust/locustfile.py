from locust import HttpUser, task, between


class SistemaGestionUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def obtener_inicio_api(self):
        self.client.get("/")

    @task(2)
    def obtener_participantes(self):
        self.client.get("/participantes/")

    @task(2)
    def obtener_salas(self):
        self.client.get("/salas/")

    @task(2)
    def obtener_reservas(self):
        self.client.get("/reservas/")

    @task(1)
    def obtener_openapi_json(self):
        self.client.get("/openapi.json")