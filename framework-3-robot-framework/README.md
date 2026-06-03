# Framework 3 - Robot Framework

## Objetivo

Este bloque utiliza **Robot Framework** para realizar pruebas funcionales automatizadas sobre el Sistema de Gestión de Salas UCU.

Robot Framework se incluye en el proyecto porque permite escribir pruebas de una forma clara, legible y cercana a documentación funcional. Esto lo convierte en una herramienta útil tanto para perfiles técnicos como para personas que necesitan entender los escenarios de prueba sin leer código Python directamente.

---

## Tipo de pruebas realizadas

- Pruebas funcionales de navegación.
- Validación de carga del frontend.
- Validación de módulos principales.
- Validación de textos visibles.
- Validación de errores visibles desde la interfaz.
- Capturas de evidencia.
- Generación automática de reportes propios de Robot Framework.

---

## Módulos probados

- Dashboard
- Participantes
- Salas
- Reservas
- Reportes
- Sanciones

---

## Archivo principal

- `framework-3-robot-framework/tests/navegacion_sistema.robot`

---

## Ejecución de pruebas

Desde la raíz del proyecto:

`robot -d framework-3-robot-framework/reports framework-3-robot-framework/tests`

---

## Resultado actual

Resultado obtenido en la ejecución inicial:

`7 tests, 7 passed, 0 failed`

---

## Reportes generados

Robot Framework genera automáticamente los siguientes archivos:

- `framework-3-robot-framework/reports/output.xml`
- `framework-3-robot-framework/reports/log.html`
- `framework-3-robot-framework/reports/report.html`

---

## Evidencias generadas

Las capturas generadas durante las pruebas se guardan en:

`framework-3-robot-framework/evidencias/`

Algunas capturas generadas:

- `robot-frontend-home.png`
- `robot-participantes.png`
- `robot-salas.png`
- `robot-reservas.png`
- `robot-reportes.png`
- `robot-sanciones-error.png`
- `robot-dashboard-error-horarios.png`

---

## Casos implementados

- RF-001 - Verificar carga del frontend.
- RF-002 - Verificar navegación a Participantes.
- RF-003 - Verificar navegación a Salas.
- RF-004 - Verificar navegación a Reservas.
- RF-005 - Verificar navegación a Reportes.
- RF-006 - Verificar error en módulo Sanciones.
- RF-007 - Verificar error en Dashboard.

---

## Observación QA

Robot Framework permitió expresar pruebas automatizadas de una forma más descriptiva que otros frameworks.

Mientras Selenium y Pytest requieren una estructura más orientada al código, Robot permite que los casos se lean casi como documentación funcional. Esto puede ser útil en equipos donde QA, desarrollo y negocio necesitan entender rápidamente qué se está validando.

En este proyecto, Robot ayudó a validar módulos principales y errores visibles ya detectados durante la exploración manual.

---

## Aprendizaje

Con este bloque practiqué:

- Cómo escribir pruebas con sintaxis Robot.
- Cómo usar SeleniumLibrary.
- Cómo crear keywords reutilizables.
- Cómo ejecutar suites de pruebas.
- Cómo generar reportes automáticos.
- Cómo capturar evidencia visual.
- Cómo expresar casos de prueba de forma más legible.

---

## Estado del bloque

Estado actual: **completado en etapa inicial**.

Próximas posibles mejoras:

- Separar keywords en una carpeta `resources/`.
- Crear keywords específicas por módulo.
- Automatizar formularios.
- Agregar pruebas negativas.
- Comparar claridad de Robot frente a Selenium y Playwright.