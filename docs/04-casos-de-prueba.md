# 04 - Casos de Prueba

## Objetivo

Este documento reúne los casos de prueba iniciales definidos para el Sistema de Gestión de Salas UCU.

Los casos están pensados para cubrir una primera etapa de testing manual y luego servir como base para automatizar pruebas con Pytest, Selenium, Robot Framework, Playwright, Locust y Postman.

---

## Estado de los casos

Los estados utilizados serán:

* **Aprobado:** el comportamiento observado coincide con lo esperado.
* **Fallido:** el comportamiento observado no coincide con lo esperado.
* **Con observación:** el sistema funciona parcialmente o muestra datos incompletos.
* **Pendiente de automatizar:** el caso fue identificado, pero todavía no fue implementado en código.

---

## CP-001 - Verificar que el backend responde

**Módulo:** Backend
**Tipo de prueba:** API / Smoke test
**Prioridad:** Alta
**Herramientas sugeridas:** Pytest, Requests, Postman

### Precondiciones

* Docker debe estar corriendo.
* El backend debe estar levantado en `http://localhost:8000`.

### Pasos

1. Abrir el navegador o ejecutar una petición GET a `http://localhost:8000`.
2. Observar la respuesta del backend.

### Resultado esperado

El backend debe responder correctamente indicando que la API está funcionando.

### Resultado observado

El backend respondió correctamente con el mensaje de API funcionando.

### Estado

Aprobado.

---

## CP-002 - Verificar disponibilidad de Swagger

**Módulo:** Backend / Documentación API
**Tipo de prueba:** API / Documentación
**Prioridad:** Alta
**Herramientas sugeridas:** Manual, Postman, Pytest

### Precondiciones

* El backend debe estar corriendo en `http://localhost:8000`.

### Pasos

1. Ingresar a `http://localhost:8000/docs`.
2. Verificar que se cargue la documentación Swagger.
3. Revisar que se muestren los endpoints disponibles.

### Resultado esperado

Swagger debe cargar correctamente y mostrar los endpoints del sistema.

### Resultado observado

Swagger cargó correctamente y mostró endpoints de participantes, salas, reservas y otros módulos.

### Estado

Aprobado.

---

## CP-003 - Verificar carga del frontend

**Módulo:** Frontend
**Tipo de prueba:** Smoke test / UI
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* El frontend debe estar levantado en `http://localhost:5173`.
* El backend debe estar disponible.

### Pasos

1. Abrir `http://localhost:5173`.
2. Verificar que la aplicación cargue.
3. Observar si se muestra el menú lateral y el dashboard.

### Resultado esperado

La aplicación debe cargar correctamente y mostrar la interfaz principal.

### Resultado observado

El frontend cargó correctamente y mostró el dashboard principal.

### Estado

Aprobado.

---

## CP-004 - Verificar carga del Dashboard

**Módulo:** Dashboard
**Tipo de prueba:** Funcional / UI
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright

### Precondiciones

* Frontend y backend deben estar corriendo.
* La aplicación debe estar abierta en el navegador.

### Pasos

1. Ingresar al dashboard.
2. Verificar las tarjetas principales.
3. Revisar la tabla de últimas reservas.
4. Observar si aparecen mensajes de error.

### Resultado esperado

El dashboard debe mostrar datos generales del sistema, métricas y últimas reservas sin errores.

### Resultado observado

El dashboard cargó y mostró reservas activas, reservas de hoy, total de reservas y turnos populares.
También mostró un error en la sección “Horarios más demandados”.

### Estado

Con observación.

---

## CP-005 - Detectar error en horarios más demandados

**Módulo:** Dashboard
**Tipo de prueba:** Funcional / Error visible
**Prioridad:** Media
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* El dashboard debe estar visible.

### Pasos

1. Ingresar al dashboard.
2. Revisar la sección “Horarios más demandados”.
3. Observar el mensaje mostrado por la interfaz.

### Resultado esperado

El sistema debería mostrar los horarios con mayor demanda o un mensaje controlado si no hay datos.

### Resultado observado

El sistema muestra el mensaje: `Error cargando horarios: Error 404 Not Found`.

### Estado

Fallido.

### Bug asociado

BUG-001.

---

## CP-006 - Verificar listado de salas

**Módulo:** Salas
**Tipo de prueba:** Funcional / UI
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* El frontend debe estar cargado.
* El backend debe responder correctamente.

### Pasos

1. Ingresar al módulo Salas.
2. Verificar que se muestre la tabla de salas.
3. Revisar columnas como nombre, edificio, capacidad, tipo y acciones.

### Resultado esperado

El sistema debe mostrar el listado de salas disponibles.

### Resultado observado

El módulo Salas cargó correctamente y mostró datos de salas existentes.

### Estado

Aprobado.

---

## CP-007 - Verificar listado de participantes

**Módulo:** Participantes
**Tipo de prueba:** Funcional / UI
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* El sistema debe estar corriendo.
* El módulo Participantes debe estar disponible en el menú lateral.

### Pasos

1. Ingresar al módulo Participantes.
2. Verificar que se muestre la tabla.
3. Revisar columnas como CI, nombre, apellido, email y acciones.

### Resultado esperado

El sistema debe mostrar el listado de participantes registrados.

### Resultado observado

El módulo Participantes cargó correctamente y mostró participantes existentes.

### Estado

Aprobado.

---

## CP-008 - Verificar listado de reservas

**Módulo:** Reservas
**Tipo de prueba:** Funcional / UI
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* El sistema debe estar corriendo.
* Deben existir reservas cargadas en la base de datos.

### Pasos

1. Ingresar al módulo Reservas.
2. Verificar que se muestre la tabla de reservas.
3. Revisar columnas como sala, edificio, fecha, hora, participantes, estado y acciones.

### Resultado esperado

El sistema debe mostrar el listado de reservas registradas.

### Resultado observado

El módulo Reservas cargó correctamente y mostró reservas existentes.

### Estado

Aprobado.

---

## CP-009 - Verificar módulo Sanciones

**Módulo:** Sanciones
**Tipo de prueba:** Funcional / Error visible
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework, Pytest

### Precondiciones

* El frontend debe estar corriendo.
* El backend debe estar disponible.

### Pasos

1. Ingresar al módulo Sanciones desde el menú lateral.
2. Verificar si se carga el listado.
3. Observar mensajes de error en pantalla.

### Resultado esperado

El sistema debería mostrar el listado de sanciones o un mensaje controlado si no existen datos.

### Resultado observado

El sistema muestra el mensaje: `Error: Failed to fetch`.

### Estado

Fallido.

### Bug asociado

BUG-002.

---

## CP-010 - Verificar módulo Reportes

**Módulo:** Reportes
**Tipo de prueba:** Funcional / UI
**Prioridad:** Media
**Herramientas sugeridas:** Selenium, Playwright

### Precondiciones

* El sistema debe estar corriendo.
* Deben existir datos de reservas en la base de datos.

### Pasos

1. Ingresar al módulo Reportes.
2. Verificar las tarjetas de métricas.
3. Revisar gráficos o listados.
4. Observar valores incompletos o errores visibles.

### Resultado esperado

El módulo Reportes debería mostrar métricas analíticas completas y coherentes.

### Resultado observado

El módulo Reportes cargó parcialmente. Algunas métricas se muestran como `N/A`, aunque sí se observan datos en otras secciones.

### Estado

Con observación.

### Bug asociado

BUG-003.

---

## CP-011 - Verificar navegación lateral

**Módulo:** Navegación general
**Tipo de prueba:** UI / E2E
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* La aplicación debe estar cargada en el navegador.

### Pasos

1. Ingresar al dashboard.
2. Hacer clic en Participantes.
3. Hacer clic en Salas.
4. Hacer clic en Reservas.
5. Hacer clic en Sanciones.
6. Hacer clic en Reportes.

### Resultado esperado

Cada opción del menú lateral debe redirigir al módulo correspondiente.

### Resultado observado

La navegación general funciona, aunque algunos módulos muestran errores internos al cargar datos.

### Estado

Con observación.

---

## CP-012 - Crear nueva sala

**Módulo:** Salas
**Tipo de prueba:** Funcional / CRUD
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Pytest, Postman

### Precondiciones

* El módulo Salas debe estar disponible.
* El backend debe permitir crear salas.

### Pasos

1. Ingresar al módulo Salas.
2. Presionar el botón “Nueva sala”.
3. Completar los datos solicitados.
4. Guardar la sala.
5. Verificar que aparezca en el listado.

### Resultado esperado

La sala debe crearse correctamente y mostrarse en la tabla.

### Estado

Pendiente de ejecutar.

---

## CP-013 - Editar sala existente

**Módulo:** Salas
**Tipo de prueba:** Funcional / CRUD
**Prioridad:** Media
**Herramientas sugeridas:** Selenium, Playwright, Pytest

### Precondiciones

* Debe existir al menos una sala cargada.

### Pasos

1. Ingresar al módulo Salas.
2. Seleccionar una sala existente.
3. Presionar “Editar”.
4. Modificar un dato.
5. Guardar cambios.
6. Verificar que el dato actualizado se refleje en la tabla.

### Resultado esperado

La sala debe actualizarse correctamente.

### Estado

Pendiente de ejecutar.

---

## CP-014 - Crear nuevo participante

**Módulo:** Participantes
**Tipo de prueba:** Funcional / CRUD
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Pytest, Postman

### Precondiciones

* El módulo Participantes debe estar disponible.

### Pasos

1. Ingresar al módulo Participantes.
2. Presionar “Nuevo participante”.
3. Completar los datos solicitados.
4. Guardar el participante.
5. Verificar que aparezca en la tabla.

### Resultado esperado

El participante debe registrarse correctamente y visualizarse en el listado.

### Estado

Pendiente de ejecutar.

---

## CP-015 - Crear nueva reserva

**Módulo:** Reservas
**Tipo de prueba:** Funcional / Flujo principal
**Prioridad:** Alta
**Herramientas sugeridas:** Selenium, Playwright, Robot Framework

### Precondiciones

* Debe existir al menos una sala disponible.
* Debe existir al menos un participante.
* El módulo Reservas debe estar disponible.

### Pasos

1. Ingresar al módulo Reservas.
2. Presionar “Nueva reserva”.
3. Seleccionar sala.
4. Seleccionar fecha y horario.
5. Asociar participantes.
6. Guardar la reserva.
7. Verificar que aparezca en la tabla.

### Resultado esperado

La reserva debe crearse correctamente y mostrarse en el listado de reservas.

### Estado

Pendiente de ejecutar.

---

## CP-016 - Validar endpoint de participantes

**Módulo:** API Participantes
**Tipo de prueba:** API
**Prioridad:** Alta
**Herramientas sugeridas:** Pytest, Requests, Postman

### Precondiciones

* El backend debe estar activo.

### Pasos

1. Enviar una petición GET al endpoint de participantes.
2. Verificar el status code.
3. Validar que la respuesta tenga estructura JSON.

### Resultado esperado

El endpoint debe responder con status code exitoso y devolver datos de participantes.

### Estado

Pendiente de automatizar.

---

## CP-017 - Validar endpoint de salas

**Módulo:** API Salas
**Tipo de prueba:** API
**Prioridad:** Alta
**Herramientas sugeridas:** Pytest, Requests, Postman

### Precondiciones

* El backend debe estar activo.

### Pasos

1. Enviar una petición GET al endpoint de salas.
2. Verificar el status code.
3. Validar que la respuesta tenga estructura JSON.

### Resultado esperado

El endpoint debe responder correctamente y devolver datos de salas.

### Estado

Pendiente de automatizar.

---

## CP-018 - Validar endpoint de reservas

**Módulo:** API Reservas
**Tipo de prueba:** API
**Prioridad:** Alta
**Herramientas sugeridas:** Pytest, Requests, Postman

### Precondiciones

* El backend debe estar activo.

### Pasos

1. Enviar una petición GET al endpoint de reservas.
2. Verificar el status code.
3. Validar que la respuesta tenga estructura JSON.

### Resultado esperado

El endpoint debe responder correctamente y devolver datos de reservas.

### Estado

Pendiente de automatizar.

---

## CP-019 - Prueba de carga básica sobre API

**Módulo:** Backend
**Tipo de prueba:** Performance básica
**Prioridad:** Media
**Herramientas sugeridas:** Locust

### Precondiciones

* El backend debe estar activo.
* Deben seleccionarse endpoints estables.

### Pasos

1. Configurar un escenario simple en Locust.
2. Simular múltiples usuarios consultando endpoints.
3. Observar tiempos de respuesta y errores.

### Resultado esperado

El backend debe responder de forma estable ante una carga básica.

### Estado

Pendiente de implementar.

---

## CP-020 - Comparar comportamiento entre frameworks

**Módulo:** Proyecto QA
**Tipo de prueba:** Análisis comparativo
**Prioridad:** Media
**Herramientas sugeridas:** Pytest, Selenium, Robot Framework, Playwright, Locust

### Precondiciones

* Deben haberse ejecutado pruebas con varios frameworks.

### Pasos

1. Revisar qué casos fueron automatizados con cada herramienta.
2. Comparar facilidad de uso.
3. Comparar claridad de reportes.
4. Comparar estabilidad.
5. Documentar aprendizajes.

### Resultado esperado

El proyecto debe incluir una comparación clara entre frameworks y conclusiones personales/profesionales.

### Estado

Pendiente de documentar.

---

## Resumen inicial

| ID     | Módulo                  | Estado                   |
| ------ | ----------------------- | ------------------------ |
| CP-001 | Backend                 | Aprobado                 |
| CP-002 | Swagger                 | Aprobado                 |
| CP-003 | Frontend                | Aprobado                 |
| CP-004 | Dashboard               | Con observación          |
| CP-005 | Horarios más demandados | Fallido                  |
| CP-006 | Salas                   | Aprobado                 |
| CP-007 | Participantes           | Aprobado                 |
| CP-008 | Reservas                | Aprobado                 |
| CP-009 | Sanciones               | Fallido                  |
| CP-010 | Reportes                | Con observación          |
| CP-011 | Navegación              | Con observación          |
| CP-012 | Crear sala              | Pendiente                |
| CP-013 | Editar sala             | Pendiente                |
| CP-014 | Crear participante      | Pendiente                |
| CP-015 | Crear reserva           | Pendiente                |
| CP-016 | API participantes       | Pendiente de automatizar |
| CP-017 | API salas               | Pendiente de automatizar |
| CP-018 | API reservas            | Pendiente de automatizar |
| CP-019 | Carga básica API        | Pendiente de implementar |
| CP-020 | Comparación frameworks  | Pendiente de documentar  |

---

## Observación final

Estos casos representan la base inicial del proceso de testing. A medida que se avance con cada framework, los casos podrán ampliarse, automatizarse y vincularse con evidencias concretas.

El objetivo es que este documento funcione como guía de trabajo y como trazabilidad entre análisis manual, automatización y resultados finales.
