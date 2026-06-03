# Framework 4 - Playwright

## Objetivo

Este bloque utiliza **Playwright** para automatizar pruebas end-to-end modernas sobre el Sistema de Gestión de Salas UCU.

Playwright se trabaja con profundidad dentro del proyecto porque representa una alternativa moderna para automatización web, con una ejecución rápida, esperas automáticas, capturas full page y herramientas de depuración como traces.

El objetivo de este bloque es comparar una forma moderna de automatización web frente a Selenium, manteniendo una estructura ordenada, reutilizable y orientada a evidencia.

---

## Tipo de pruebas realizadas

* Pruebas de carga del frontend.
* Pruebas de navegación entre módulos.
* Validación de textos visibles.
* Validación de tablas.
* Validación de bugs visibles.
* Capturas full page.
* Capturas automáticas ante fallos.
* Generación de reporte HTML.
* Ejecución con navegador visible.
* Ejecución con traces.
* Primer acercamiento a Page Object Model con Playwright.
* Uso de fixtures reutilizables.
* Uso de parametrización con Pytest.

---

## Módulos probados

* Dashboard
* Participantes
* Salas
* Reservas
* Reportes
* Sanciones

---

## Archivos principales

* `framework-4-playwright/pages/base_page.py`
* `framework-4-playwright/pages/sistema_page.py`
* `framework-4-playwright/tests/conftest.py`
* `framework-4-playwright/tests/test_smoke_ui.py`
* `framework-4-playwright/tests/test_navegacion.py`
* `framework-4-playwright/tests/test_modulos_tablas.py`
* `framework-4-playwright/tests/test_bugs_visibles.py`

---

## Estructura del bloque

* `pages/`: contiene clases reutilizables para interactuar con la aplicación.
* `tests/`: contiene las pruebas automatizadas.
* `evidencias/`: contiene capturas generadas durante la ejecución.
* `evidencias/fallos/`: contiene capturas automáticas si una prueba falla.
* `reports/`: contiene reportes HTML generados con Pytest.
* `test-results/`: puede contener trazas generadas por Playwright cuando se ejecuta con tracing.

---

## Pruebas implementadas

### Smoke test de interfaz

Se valida que el frontend cargue correctamente y que el Dashboard sea visible.

### Navegación entre módulos

Se valida la navegación hacia los módulos principales:

* Participantes
* Salas
* Reservas
* Reportes

### Validación de tablas

Se valida que los módulos principales muestren tablas visibles con contenido:

* Participantes
* Salas
* Reservas

### Validación de bugs visibles

Se automatizaron validaciones sobre errores detectados previamente durante la exploración manual:

* Error en Dashboard relacionado con “Horarios más demandados”.
* Error en el módulo Sanciones.
* Métricas incompletas o valores `N/A` en Reportes.

Estas pruebas ayudan a demostrar cómo Playwright puede validar comportamientos visibles desde la perspectiva del usuario final.

---

## Ejecución de pruebas

Desde la raíz del proyecto:

`python -m pytest framework-4-playwright/tests -v`

---

## Ejecución con navegador visible

Para ver Playwright ejecutando las pruebas en el navegador:

`python -m pytest framework-4-playwright/tests -v --headed`

---

## Generar reporte HTML

Para generar un reporte HTML con los resultados:

`python -m pytest framework-4-playwright/tests -v --html=framework-4-playwright/reports/reporte-playwright-completo.html`

---

## Ejecución con traces

Para generar trazas de ejecución:

`python -m pytest framework-4-playwright/tests -v --tracing=on`

Las trazas permiten analizar paso a paso lo que ocurrió durante la ejecución de las pruebas. Esto es muy útil para depurar errores, revisar acciones realizadas por el navegador y entender mejor el comportamiento de la aplicación.

---

## Resultado actual

Resultado obtenido en la ejecución ampliada:

`12 passed`

---

## Evidencias generadas

Las capturas generadas durante las pruebas se guardan en:

`framework-4-playwright/evidencias/`

Algunas evidencias generadas:

* `playwright-frontend-home.png`
* `playwright-participantes.png`
* `playwright-salas.png`
* `playwright-reservas.png`
* `playwright-reportes.png`
* `playwright-tabla-participantes.png`
* `playwright-tabla-salas.png`
* `playwright-tabla-reservas.png`
* `playwright-dashboard-error-horarios.png`
* `playwright-sanciones-error.png`
* `playwright-reportes-na.png`
* `playwright-reportes-contenido.png`

El reporte HTML se guarda en:

`framework-4-playwright/reports/reporte-playwright-completo.html`

---

## Capturas automáticas ante fallos

Se agregó una configuración en `conftest.py` para que, si una prueba falla, Playwright guarde automáticamente una captura en:

`framework-4-playwright/evidencias/fallos/`

Esto permite conservar evidencia visual del momento exacto del error.

---

## Buenas prácticas aplicadas

En este bloque se aplicaron varias prácticas de automatización moderna:

* Uso de Page Object Model inicial.
* Separación entre lógica de página y lógica de prueba.
* Uso de fixtures reutilizables.
* Uso de `expect()` para validaciones.
* Uso de parametrización con Pytest.
* Capturas full page.
* Capturas automáticas ante fallos.
* Ejecución con navegador visible.
* Ejecución con traces.
* Generación de reporte HTML.
* Validación de bugs visibles.

---

## Observación QA

Playwright permitió automatizar pruebas de interfaz de forma rápida, clara y estable.

A diferencia de Selenium, Playwright ofrece una experiencia más moderna, con esperas automáticas, capturas full page y herramientas de depuración como traces.

En este proyecto, Playwright permitió validar los mismos módulos principales del sistema, pero con una ejecución más rápida y una sintaxis más orientada a pruebas end-to-end modernas.

---

## Aprendizaje

Con este bloque practiqué:

* Cómo ejecutar pruebas E2E con Playwright.
* Cómo usar el fixture `page`.
* Cómo validar contenido visible con `expect()`.
* Cómo navegar entre módulos.
* Cómo validar tablas.
* Cómo guardar capturas full page.
* Cómo generar reportes HTML.
* Cómo ejecutar pruebas con navegador visible.
* Cómo generar trazas de ejecución.
* Cómo estructurar pruebas usando Page Object Model.
* Cómo comparar Playwright con Selenium sobre el mismo sistema.

---

## Estado del bloque

Estado actual: **completado en etapa inicial ampliada**.

Próximas posibles mejoras:

* Crear Page Objects específicos por módulo.
* Automatizar formularios.
* Agregar pruebas negativas.
* Usar selectores más robustos.
* Ejecutar pruebas en varios navegadores.
* Separar pruebas por marcadores.
* Integrar traces como evidencia formal del proyecto.
* Comparar tiempos de ejecución con Selenium.
