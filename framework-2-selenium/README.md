# Framework 2 - Selenium

## Objetivo

Este bloque utiliza **Selenium** para automatizar pruebas de interfaz sobre el Sistema de Gestión de Salas UCU.

Selenium se trabaja con especial profundidad dentro del proyecto porque es una herramienta clásica, muy utilizada en el mercado QA y clave para aprender automatización web desde una mirada profesional.

El objetivo no es solamente abrir el navegador y validar una pantalla, sino comenzar a estructurar pruebas de interfaz de forma ordenada, reutilizable y con evidencia visual.

---

## Tipo de pruebas realizadas

* Pruebas de carga del frontend.
* Pruebas de navegación entre módulos.
* Validación de textos visibles en pantalla.
* Validación de tablas y datos cargados.
* Validación de módulos principales.
* Validación de errores visibles desde la interfaz.
* Capturas de evidencia durante la ejecución.
* Capturas automáticas en caso de fallo.
* Generación de reporte HTML.
* Primer acercamiento a Page Object Model.
* Uso de `conftest.py` para reutilizar configuración.
* Uso de parametrización con Pytest para repetir pruebas sobre distintos módulos.

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

* `framework-2-selenium/pages/base_page.py`
* `framework-2-selenium/tests/conftest.py`
* `framework-2-selenium/tests/test_navegacion_sistema.py`
* `framework-2-selenium/tests/test_modulos_tablas.py`
* `framework-2-selenium/tests/test_bugs_visible.py`

---

## Estructura del bloque

* `pages/`: contiene clases reutilizables para interactuar con la interfaz.
* `tests/`: contiene las pruebas automatizadas.
* `evidencias/`: contiene capturas generadas durante la ejecución.
* `evidencias/fallos/`: contiene capturas automáticas si una prueba falla.
* `reports/`: contiene reportes HTML generados con Pytest.

---

## Pruebas implementadas

### Navegación general

Se valida que el frontend cargue correctamente y que sea posible navegar por los módulos principales del sistema.

Pruebas incluidas:

* Carga inicial del frontend.
* Navegación hacia Participantes.
* Navegación hacia Salas.
* Navegación hacia Reservas.
* Navegación hacia Reportes.

---

### Validación de tablas

Se valida que los módulos principales muestren tablas con contenido visible.

Módulos validados:

* Participantes
* Salas
* Reservas

En estas pruebas se verifica:

* Que el módulo cargue.
* Que exista al menos una tabla.
* Que la tabla tenga filas visibles.
* Que se genere una captura como evidencia.

---

### Validación de bugs visibles

Se automatizaron pruebas sobre errores detectados durante la exploración manual inicial.

Errores validados:

* Error en Dashboard relacionado con “Horarios más demandados”.
* Error `Failed to fetch` en el módulo Sanciones.
* Métricas incompletas o valores `N/A` en Reportes.

Estas pruebas no buscan ocultar los errores del sistema, sino documentarlos y demostrar cómo Selenium puede ayudar a detectarlos desde la interfaz.

---

## Ejecución de pruebas

Desde la raíz del proyecto:

`python -m pytest framework-2-selenium/tests -v`

---

## Generar reporte HTML

Para generar un reporte HTML con los resultados:

`python -m pytest framework-2-selenium/tests -v --html=framework-2-selenium/reports/reporte-selenium-completo.html`

---

## Resultado actual

Resultado obtenido en la ejecución ampliada:

`9 passed`

---

## Evidencias generadas

Las capturas generadas durante las pruebas se guardan en:

`framework-2-selenium/evidencias/`

Algunas evidencias generadas:

* `selenium-frontend-home.png`
* `selenium-participantes.png`
* `selenium-salas.png`
* `selenium-reservas.png`
* `selenium-reportes.png`
* `selenium-dashboard-error-horarios.png`
* `selenium-sanciones-error.png`
* `selenium-tabla-participantes.png`
* `selenium-tabla-salas.png`
* `selenium-tabla-reservas.png`
* `selenium-reportes-contenido.png`

El reporte HTML se guarda en:

`framework-2-selenium/reports/reporte-selenium-completo.html`

---

## Capturas automáticas ante fallos

Se agregó una configuración en `conftest.py` para que, si una prueba falla, Selenium guarde automáticamente una captura del navegador en:

`framework-2-selenium/evidencias/fallos/`

Esto permite contar con evidencia visual del momento exacto en que se produce un error.

Esta práctica es muy útil en proyectos reales porque ayuda a entender rápidamente qué estaba viendo el navegador cuando una prueba falló.

---

## Buenas prácticas aplicadas

En este bloque se aplicaron varias prácticas importantes de automatización:

* Separación entre lógica de página y lógica de prueba.
* Uso inicial de Page Object Model mediante `BasePage`.
* Uso de fixture `driver` reutilizable.
* Uso de `conftest.py` para configuración compartida.
* Uso de esperas explícitas.
* Uso de capturas como evidencia.
* Uso de pruebas parametrizadas.
* Validación de errores visibles.
* Generación de reportes HTML.

---

## Observación QA

Selenium permitió validar el sistema desde la perspectiva del usuario, navegando por la interfaz real y comprobando que los módulos principales cargan correctamente.

También permitió detectar y documentar errores visibles, como el fallo del módulo Sanciones y el error del Dashboard en la sección de horarios más demandados.

Este enfoque es importante porque no solo valida respuestas técnicas del backend, sino también la experiencia visible del usuario final.

---

## Aprendizaje

Con este bloque practiqué:

* Cómo abrir un navegador con Selenium.
* Cómo navegar una aplicación web.
* Cómo validar textos visibles.
* Cómo interactuar con elementos de la interfaz.
* Cómo usar esperas explícitas.
* Cómo guardar capturas como evidencia.
* Cómo generar reportes HTML con Pytest.
* Cómo aplicar una estructura inicial basada en Page Object Model.
* Cómo preparar capturas automáticas ante fallos.
* Cómo usar `conftest.py` para reutilizar configuración.
* Cómo parametrizar pruebas para validar varios módulos con una misma lógica.
* Cómo transformar observaciones manuales en pruebas automatizadas.

---

## Estado del bloque

Estado actual: **completado en etapa inicial ampliada**.

Próximas posibles mejoras:

* Crear Page Objects específicos para cada módulo.
* Automatizar creación de salas.
* Automatizar creación de participantes.
* Automatizar edición y eliminación de registros.
* Agregar pruebas negativas.
* Mejorar selectores para hacerlos más robustos.
* Integrar capturas directamente dentro del reporte HTML.
* Ejecutar pruebas en modo headless.
* Separar pruebas smoke, regresión y bugs visibles por marcador.
