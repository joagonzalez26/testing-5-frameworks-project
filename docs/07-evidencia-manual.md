# 07 - Evidencia Manual

## Objetivo

Este documento registra la evidencia obtenida durante la exploración manual inicial del Sistema de Gestión de Salas UCU.

La finalidad es dejar constancia de los módulos revisados, comportamientos observados, errores detectados y primeras conclusiones antes de avanzar con la automatización mediante frameworks.

---

## Ambiente de prueba

* Sistema bajo prueba: Sistema de Gestión de Salas UCU
* Frontend: http://localhost:5173
* Backend: http://localhost:8000
* Swagger: http://localhost:8000/docs
* Base de datos: MySQL en Docker
* Navegador: Google Chrome
* Sistema operativo: macOS
* Ejecución local: Docker Compose + Vite

---

## Resumen de exploración manual

Durante la exploración inicial se verificó que el sistema podía ejecutarse localmente y que sus módulos principales eran accesibles desde la interfaz web.

Se revisaron los siguientes módulos:

* Dashboard
* Salas
* Participantes
* Reservas
* Sanciones
* Reportes
* Swagger / documentación API

---

## Evidencia EM-001 - Backend disponible

### Módulo

Backend

### Acción realizada

Se ingresó a la URL local del backend y se verificó que respondiera correctamente.

### Resultado observado

El backend respondió en `http://localhost:8000`.

### Estado

Aprobado.

### Caso relacionado

CP-001.

---

## Evidencia EM-002 - Swagger disponible

### Módulo

Backend / API

### Acción realizada

Se ingresó a `http://localhost:8000/docs` para revisar la documentación generada por FastAPI.

### Resultado observado

Swagger cargó correctamente y mostró los endpoints disponibles del sistema.

### Estado

Aprobado.

### Caso relacionado

CP-002.

---

## Evidencia EM-003 - Frontend disponible

### Módulo

Frontend

### Acción realizada

Se ingresó a `http://localhost:5173` desde el navegador.

### Resultado observado

La interfaz web cargó correctamente y permitió navegar por los módulos principales.

### Estado

Aprobado.

### Caso relacionado

CP-003.

---

## Evidencia EM-004 - Dashboard

### Módulo

Dashboard

### Acción realizada

Se revisó el panel principal del sistema, observando tarjetas, métricas y secciones disponibles.

### Resultado observado

El dashboard mostró información general del sistema, reservas activas, reservas del día, total de reservas y turnos populares.

También se observó un error visible en la sección “Horarios más demandados”.

### Estado

Con observación.

### Caso relacionado

CP-004 y CP-005.

### Bug relacionado

BUG-001.

---

## Evidencia EM-005 - Módulo Salas

### Módulo

Salas

### Acción realizada

Se ingresó al módulo Salas desde el menú lateral.

### Resultado observado

El sistema mostró correctamente una tabla con salas cargadas, incluyendo información como nombre, edificio, capacidad, tipo y acciones disponibles.

### Estado

Aprobado.

### Caso relacionado

CP-006.

---

## Evidencia EM-006 - Módulo Participantes

### Módulo

Participantes

### Acción realizada

Se ingresó al módulo Participantes desde el menú lateral.

### Resultado observado

El sistema mostró correctamente una tabla con participantes registrados, incluyendo datos como CI, nombre, apellido, email y acciones disponibles.

### Estado

Aprobado.

### Caso relacionado

CP-007.

---

## Evidencia EM-007 - Módulo Reservas

### Módulo

Reservas

### Acción realizada

Se ingresó al módulo Reservas desde el menú lateral.

### Resultado observado

El sistema mostró correctamente reservas existentes, con datos de sala, edificio, fecha, hora, participantes, estado y acciones disponibles.

### Estado

Aprobado.

### Caso relacionado

CP-008.

---

## Evidencia EM-008 - Módulo Sanciones

### Módulo

Sanciones

### Acción realizada

Se ingresó al módulo Sanciones desde el menú lateral.

### Resultado observado

El sistema no logró cargar correctamente la información y mostró el mensaje:

`Error: Failed to fetch`

### Estado

Fallido.

### Caso relacionado

CP-009.

### Bug relacionado

BUG-002.

---

## Evidencia EM-009 - Módulo Reportes

### Módulo

Reportes

### Acción realizada

Se ingresó al módulo Reportes para revisar métricas, gráficos o datos analíticos.

### Resultado observado

El módulo cargó parcialmente. Algunas secciones mostraron datos, pero ciertas métricas aparecieron como `N/A`.

### Estado

Con observación.

### Caso relacionado

CP-010.

### Bug relacionado

BUG-003.

---

## Evidencia EM-010 - Navegación general

### Módulo

Navegación lateral

### Acción realizada

Se utilizó el menú lateral para navegar entre Dashboard, Participantes, Salas, Reservas, Sanciones y Reportes.

### Resultado observado

La navegación general funcionó correctamente, aunque algunos módulos presentaron errores internos de carga.

### Estado

Con observación.

### Caso relacionado

CP-011.

---

## Resumen de resultados manuales

| Evidencia | Módulo        | Estado          | Caso relacionado | Bug relacionado |
| --------- | ------------- | --------------- | ---------------- | --------------- |
| EM-001    | Backend       | Aprobado        | CP-001           | -               |
| EM-002    | Swagger       | Aprobado        | CP-002           | -               |
| EM-003    | Frontend      | Aprobado        | CP-003           | -               |
| EM-004    | Dashboard     | Con observación | CP-004 / CP-005  | BUG-001         |
| EM-005    | Salas         | Aprobado        | CP-006           | -               |
| EM-006    | Participantes | Aprobado        | CP-007           | -               |
| EM-007    | Reservas      | Aprobado        | CP-008           | -               |
| EM-008    | Sanciones     | Fallido         | CP-009           | BUG-002         |
| EM-009    | Reportes      | Con observación | CP-010           | BUG-003         |
| EM-010    | Navegación    | Con observación | CP-011           | -               |

---

## Observación personal de testing

La exploración manual permitió entender mejor el sistema antes de automatizar. Se pudo comprobar que varios módulos funcionan correctamente, pero también se detectaron errores visibles que deben ser documentados como parte del proceso QA.

Esta etapa confirma la importancia de no comenzar directamente por la automatización. Primero es necesario observar, navegar, interpretar el comportamiento del sistema y definir qué casos tienen mayor valor para ser automatizados.

---

## Próximos pasos

A partir de esta evidencia manual, se avanzará con:

* Automatización de pruebas API con Pytest.
* Pruebas de navegación con Selenium.
* Pruebas funcionales con Robot Framework.
* Pruebas end-to-end con Playwright.
* Pruebas básicas de carga con Locust.
* Validación complementaria de API con Postman.
