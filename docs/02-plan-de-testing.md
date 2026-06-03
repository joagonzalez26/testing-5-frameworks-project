# 02 - Plan de Testing

## Objetivo del plan

El objetivo de este plan es definir una estrategia de testing manual y automatizado sobre el Sistema de Gestión de Salas UCU, utilizando diferentes frameworks y herramientas para validar el comportamiento general del sistema desde una mirada funcional, técnica y exploratoria.

Este proyecto busca demostrar no solo la ejecución de pruebas, sino también la forma de trabajo aplicada durante el proceso: análisis inicial, documentación, identificación de riesgos, automatización, evidencia, comparación de herramientas y conclusiones profesionales.

---

## Sistema bajo prueba

Sistema de Gestión de Salas UCU.

Ambiente local:

* Frontend: http://localhost:5173
* Backend: http://localhost:8000
* Swagger: http://localhost:8000/docs
* Base de datos: MySQL en Docker
* Backend: FastAPI
* Frontend: React / Vite

---

## Alcance del testing

Se probarán los módulos principales visibles del sistema:

* Dashboard
* Participantes
* Salas
* Reservas
* Sanciones
* Reportes

También se validarán endpoints disponibles desde Swagger y comportamientos observados desde la interfaz web.

---

## Fuera de alcance

En esta etapa no se buscará modificar el código fuente del sistema original ni corregir sus errores internos.

El sistema será tratado como una aplicación bajo prueba. El foco estará en analizarlo, probarlo, documentar comportamientos y automatizar escenarios relevantes.

No se incluyen en esta primera etapa:

* Despliegue en producción.
* Pruebas de seguridad avanzadas.
* Testing de base de datos en profundidad.
* Refactorización del sistema original.
* Corrección de bugs del sistema.

---

## Tipos de prueba a realizar

### Pruebas manuales

Se realizará una exploración inicial del sistema desde la interfaz web, observando módulos disponibles, comportamientos esperados, errores visibles y flujos principales.

### Pruebas funcionales

Se validará que las funciones principales del sistema respondan de acuerdo con lo esperado: carga de datos, navegación, visualización de tablas, formularios y reportes.

### Pruebas de API

Se probarán endpoints del backend mediante Pytest, Requests y Postman, verificando status codes, respuestas JSON y disponibilidad de servicios.

### Pruebas end-to-end

Se automatizarán flujos desde el navegador utilizando Selenium y Playwright.

### Pruebas de aceptación

Se utilizará Robot Framework para documentar y ejecutar pruebas más legibles desde una perspectiva funcional.

### Pruebas básicas de carga

Se utilizará Locust para simular usuarios concurrentes sobre endpoints seleccionados del backend.

---

## Frameworks y herramientas seleccionadas

### Pytest

Se utilizará para pruebas de API y validaciones técnicas del backend.

### Selenium

Se trabajará con especial profundidad por ser una herramienta clásica y muy demandada en el mercado QA. Se aplicará para automatizar navegación, validaciones visuales, formularios y flujos de usuario desde navegador.

### Robot Framework

Se utilizará para expresar pruebas funcionales de forma clara, legible y cercana a documentación de aceptación.

### Playwright

Se utilizará para pruebas end-to-end modernas, con foco en estabilidad, velocidad y automatización web actual.

### Locust

Se utilizará para pruebas básicas de carga y rendimiento sobre endpoints del backend.

### Postman

Se utilizará como herramienta complementaria para exploración, documentación y validación manual de APIs.

---

## Criterios de entrada

Para comenzar las pruebas, se deben cumplir las siguientes condiciones:

* El backend debe estar corriendo en `http://localhost:8000`.
* Swagger debe estar disponible en `http://localhost:8000/docs`.
* El frontend debe estar corriendo en `http://localhost:5173`.
* La base de datos MySQL debe estar activa mediante Docker.
* El proyecto de testing debe tener el entorno virtual configurado.
* Las dependencias de testing deben estar instaladas correctamente.

---

## Criterios de salida

La etapa de testing se considerará finalizada cuando:

* Se hayan documentado los módulos principales del sistema.
* Se hayan registrado los casos de prueba principales.
* Se hayan reportado los bugs encontrados.
* Se hayan ejecutado pruebas manuales.
* Se hayan automatizado pruebas básicas con los cinco frameworks seleccionados.
* Se hayan generado evidencias y reportes.
* Se haya realizado una comparación entre frameworks.
* Se hayan documentado conclusiones y aprendizajes.

---

## Riesgos identificados

Durante la exploración inicial se detectaron algunos comportamientos que pueden impactar en el testing:

* El módulo Sanciones muestra error `Failed to fetch`.
* El dashboard muestra error 404 en la sección de horarios más demandados.
* El módulo Reportes muestra algunas métricas como `N/A`.
* Algunos endpoints pueden estar incompletos o no responder como espera el frontend.
* El sistema tiene una interfaz simple, por lo que algunos flujos pueden ser limitados.
* Locust mostró un warning relacionado con `greenlet` al consultar la versión usando Python 3.14.

Estos puntos serán tratados como parte del análisis y la documentación del proyecto.

---

## Enfoque de trabajo

El proyecto se desarrollará de forma progresiva, priorizando claridad, evidencia y aprendizaje.

La idea no es automatizar por automatizar, sino entender qué se está probando, por qué se prueba y qué valor aporta cada herramienta dentro del proceso de QA.

Se buscará mantener una mirada curiosa, completa y profesional, documentando tanto los resultados como las decisiones tomadas durante el camino.
