# Framework 1 - Pytest

## Objetivo

Este bloque utiliza **Pytest** junto con **Requests** para validar la capa de API del Sistema de Gestión de Salas UCU.

La idea es comenzar el proceso de automatización desde el backend, verificando que los servicios principales respondan correctamente antes de avanzar con pruebas de interfaz usando Selenium, Robot Framework y Playwright.

---

## Tipo de pruebas realizadas

* Smoke tests de API.
* Validación de disponibilidad del backend.
* Validación de Swagger.
* Validación de OpenAPI JSON.
* Validación de endpoints principales.
* Verificación de status codes.
* Verificación básica de estructura JSON.

---

## Endpoints probados

* `GET /`
* `GET /docs`
* `GET /openapi.json`
* `GET /participantes/`
* `GET /salas/`
* `GET /reservas/`

---

## Archivos de prueba

* `framework-1-pytest/tests/test_api_smoke.py`
* `framework-1-pytest/tests/test_api_modulos.py`

---

## Ejecución de pruebas

Desde la raíz del proyecto:

`python -m pytest framework-1-pytest/tests`

---

## Generar reporte HTML

Para generar un reporte HTML con los resultados:

`python -m pytest framework-1-pytest/tests --html=framework-1-pytest/reports/reporte-pytest-api.html`

---

## Resultado actual

Resultado obtenido en la ejecución inicial:

`6 passed`

---

## Evidencia generada

El reporte HTML generado se encuentra en:

`framework-1-pytest/reports/reporte-pytest-api.html`

---

## Observación QA

Pytest permitió validar rápidamente que el backend se encuentra disponible y que los endpoints principales responden correctamente.

Esta primera capa de pruebas es importante porque confirma que la API base funciona antes de avanzar con pruebas más complejas desde la interfaz.

En un proyecto real, este tipo de pruebas ayuda a detectar rápidamente si el backend está caído, si Swagger no carga, si la documentación OpenAPI falla o si endpoints principales dejan de responder.

---

## Aprendizaje

Con este bloque practiqué:

* Cómo estructurar pruebas de API con Pytest.
* Cómo usar Requests para enviar peticiones HTTP.
* Cómo validar status codes.
* Cómo validar respuestas JSON.
* Cómo generar reportes HTML.
* Cómo comenzar una estrategia de automatización desde la capa de backend.

---

## Estado del bloque

Estado actual: **completado en etapa inicial**.

Próximas posibles mejoras:

* Agregar pruebas negativas.
* Validar estructura más detallada de las respuestas JSON.
* Probar creación de registros mediante API.
* Probar edición y eliminación de datos.
* Conectar estos casos con la matriz de trazabilidad del proyecto.
