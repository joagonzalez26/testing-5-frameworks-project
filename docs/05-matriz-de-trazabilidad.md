# 05 - Matriz de Trazabilidad

## Objetivo

La matriz de trazabilidad permite relacionar los módulos del sistema con los casos de prueba definidos, los tipos de prueba aplicados, las herramientas sugeridas y el estado actual de validación.

Este documento ayuda a mantener una visión ordenada del proceso de testing y permite identificar qué partes del sistema ya fueron revisadas, cuáles presentan errores y cuáles quedan pendientes de automatizar.

---

## Matriz inicial

| Módulo / Requisito        | Caso de prueba | Tipo de prueba            | Framework / Herramienta               | Estado                   | Evidencia |
| ------------------------- | -------------- | ------------------------- | ------------------------------------- | ------------------------ | --------- |
| Backend disponible        | CP-001         | API / Smoke test          | Pytest, Requests, Postman             | Aprobado                 | Pendiente |
| Swagger disponible        | CP-002         | API / Documentación       | Manual, Postman                       | Aprobado                 | Pendiente |
| Frontend disponible       | CP-003         | UI / Smoke test           | Selenium, Playwright                  | Aprobado                 | Pendiente |
| Dashboard visible         | CP-004         | Funcional / UI            | Selenium, Playwright                  | Con observación          | Pendiente |
| Horarios más demandados   | CP-005         | Error visible             | Selenium, Playwright                  | Fallido                  | BUG-001   |
| Listado de salas          | CP-006         | Funcional / UI            | Selenium, Playwright, Robot Framework | Aprobado                 | Pendiente |
| Listado de participantes  | CP-007         | Funcional / UI            | Selenium, Playwright, Robot Framework | Aprobado                 | Pendiente |
| Listado de reservas       | CP-008         | Funcional / UI            | Selenium, Playwright, Robot Framework | Aprobado                 | Pendiente |
| Módulo sanciones          | CP-009         | Funcional / Error visible | Selenium, Playwright, Pytest          | Fallido                  | BUG-002   |
| Módulo reportes           | CP-010         | Funcional / UI            | Selenium, Playwright                  | Con observación          | BUG-003   |
| Navegación lateral        | CP-011         | UI / E2E                  | Selenium, Playwright, Robot Framework | Con observación          | Pendiente |
| Crear sala                | CP-012         | CRUD / Funcional          | Selenium, Playwright, Pytest, Postman | Pendiente                | Pendiente |
| Editar sala               | CP-013         | CRUD / Funcional          | Selenium, Playwright, Pytest          | Pendiente                | Pendiente |
| Crear participante        | CP-014         | CRUD / Funcional          | Selenium, Playwright, Pytest, Postman | Pendiente                | Pendiente |
| Crear reserva             | CP-015         | Flujo principal           | Selenium, Playwright, Robot Framework | Pendiente                | Pendiente |
| API participantes         | CP-016         | API                       | Pytest, Requests, Postman             | Pendiente de automatizar | Pendiente |
| API salas                 | CP-017         | API                       | Pytest, Requests, Postman             | Pendiente de automatizar | Pendiente |
| API reservas              | CP-018         | API                       | Pytest, Requests, Postman             | Pendiente de automatizar | Pendiente |
| Carga básica API          | CP-019         | Performance básica        | Locust                                | Pendiente de implementar | Pendiente |
| Comparación de frameworks | CP-020         | Análisis comparativo      | Todos                                 | Pendiente de documentar  | Pendiente |

---

## Interpretación de estados

### Aprobado

El comportamiento observado coincide con el resultado esperado.

### Fallido

El sistema muestra un comportamiento incorrecto, error visible o respuesta inesperada.

### Con observación

El módulo funciona parcialmente, pero presenta errores, datos incompletos o aspectos a revisar.

### Pendiente

El caso de prueba fue definido, pero todavía no fue ejecutado.

### Pendiente de automatizar

El caso ya fue identificado y será implementado posteriormente con alguno de los frameworks seleccionados.

---

## Uso de la matriz

Esta matriz se actualizará a medida que avance el proyecto.

Cada vez que se implemente una prueba automatizada o se genere evidencia, se podrá actualizar la columna correspondiente para reflejar:

* Framework utilizado.
* Estado real de ejecución.
* Evidencia generada.
* Bug asociado.
* Reporte HTML o captura vinculada.

---

## Observación profesional

La matriz de trazabilidad ayuda a demostrar que el testing no se realiza de forma improvisada, sino siguiendo una relación clara entre funcionalidades, riesgos, casos de prueba, herramientas y resultados.

En este proyecto se utilizará como guía para mantener ordenado el avance entre testing manual, automatización y documentación final.
