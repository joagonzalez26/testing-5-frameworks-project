# Framework 5 - Locust

## Objetivo

Este bloque utiliza **Locust** para realizar pruebas básicas de carga sobre la API del Sistema de Gestión de Salas UCU.

Locust permite simular usuarios concurrentes realizando peticiones HTTP al backend, con el objetivo de observar tiempos de respuesta, cantidad de solicitudes, errores y comportamiento general del sistema bajo una carga controlada.

---

## Tipo de pruebas realizadas

* Prueba básica de carga.
* Simulación de usuarios concurrentes.
* Validación de endpoints principales del backend.
* Medición de tiempos de respuesta.
* Medición de requests por segundo.
* Identificación de fallos durante la ejecución.
* Generación de reporte HTML.

---

## Endpoints probados

* `GET /`
* `GET /openapi.json`
* `GET /participantes/`
* `GET /salas/`
* `GET /reservas/`

---

## Archivo principal

* `framework-5-locust/locustfile.py`

---

## Ejecución con interfaz web

Para ejecutar Locust con interfaz web:

`locust -f framework-5-locust/locustfile.py --host http://localhost:8000`

Luego se abre:

`http://localhost:8089`

Configuración utilizada:

* Usuarios: `10`
* Ramp up: `2 usuarios por segundo`
* Host: `http://localhost:8000`

---

## Ejecución en modo headless

Para ejecutar Locust sin interfaz web y generar reporte HTML:

`locust -f framework-5-locust/locustfile.py --host http://localhost:8000 --headless -u 10 -r 2 -t 30s --html framework-5-locust/reports/reporte-locust.html`

Parámetros utilizados:

* `-u 10`: simula 10 usuarios.
* `-r 2`: agrega 2 usuarios por segundo.
* `-t 30s`: ejecuta la prueba durante 30 segundos.
* `--html`: genera un reporte HTML.

---

## Resultado de la prueba con interfaz web

Resultado observado:

* Total de requests: `710`
* Fallos: `0`
* Porcentaje de fallos: `0.00%`
* Tiempo promedio agregado: `12 ms`
* Tiempo mínimo agregado: `1 ms`
* Tiempo máximo agregado: `51 ms`
* Mediana agregada: `17 ms`
* Requests por segundo: `5.00`

---

## Resultado de la prueba headless

Resultado observado:

* Total de requests: `142`
* Fallos: `0`
* Porcentaje de fallos: `0.00%`
* Tiempo promedio agregado: `12 ms`
* Tiempo mínimo agregado: `1 ms`
* Tiempo máximo agregado: `24 ms`
* Mediana agregada: `16 ms`
* Requests por segundo: `4.78`

---

## Percentiles observados

En la prueba headless, los percentiles agregados fueron:

* Percentil 50: `16 ms`
* Percentil 75: `20 ms`
* Percentil 90: `22 ms`
* Percentil 95: `22 ms`
* Percentil 99: `23 ms`
* Máximo: `24 ms`

Estos valores indican que la mayoría de las respuestas se mantuvieron en tiempos bajos y estables durante la prueba.

---

## Reporte generado

El reporte HTML generado se encuentra en:

`framework-5-locust/reports/reporte-locust.html`

---

## Observación QA

Locust permitió validar el comportamiento del backend ante una carga básica de usuarios concurrentes.

Durante la ejecución no se registraron fallos, lo cual indica que los endpoints principales respondieron correctamente bajo el escenario probado.

Los tiempos de respuesta fueron bajos y estables. Los endpoints `/`, `/openapi.json`, `/participantes/`, `/reservas/` y `/salas/` respondieron sin errores durante la prueba.

---

## Conclusión

La prueba realizada no representa una evaluación avanzada de rendimiento, pero sí una primera aproximación útil para comprobar estabilidad básica del backend.

El sistema respondió correctamente ante 10 usuarios concurrentes, sin errores y con tiempos de respuesta adecuados para un entorno local.

---

## Aprendizaje

Con este bloque practiqué:

* Cómo definir usuarios simulados con Locust.
* Cómo crear tareas con distintos pesos.
* Cómo ejecutar Locust con interfaz web.
* Cómo ejecutar Locust en modo headless.
* Cómo generar reportes HTML.
* Cómo interpretar requests por segundo.
* Cómo interpretar fallos.
* Cómo analizar tiempos promedio, máximos, mínimos y percentiles.
* Cómo documentar una prueba básica de carga.

---

## Estado del bloque

Estado actual: **completado en etapa inicial**.

Próximas posibles mejoras:

* Aumentar la cantidad de usuarios simulados.
* Probar escenarios con mayor duración.
* Separar endpoints por criticidad.
* Simular flujos más realistas.
* Agregar pruebas sobre endpoints POST, PUT o DELETE.
* Comparar resultados entre distintas cargas.
* Definir criterios de aceptación de performance.
