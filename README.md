# Tester Automation - QA & Frameworks

<img width="1920" height="1080" alt="Black and White Minimalist Creative Portfolio Presentation" src="https://github.com/user-attachments/assets/cd67b58e-d930-4e1d-9398-18e1269f9c10" />

---

Proyecto personal de QA Automation donde probé un sistema real usando cinco herramientas: **Pytest**, **Selenium**, **Robot Framework**, **Playwright** y **Locust**.

La idea de este proyecto fue entender el sistema, después probarlo manualmente, documentar errores, generar evidencia y finalmente automatizar pruebas con distintos enfoques.

---

## Nota personal

Este proyecto lo armé tambíen con la idea de ayudar personas que quieran introducirse al mundo del testing automatizado.

acá se vé un proceso completo: mirar el sistema con criterio, detectar comportamientos raros, documentar lo que encontré y después automatizar pruebas que realmente tengan sentido.

---

## Sistema bajo prueba

El sistema utilizado fue un **Sistema de Gestión de Salas UCU**, ejecutado en entorno local.

Ambiente utilizado:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- Base de datos: MySQL en Docker

Módulos analizados:

- Dashboard
- Participantes
- Salas
- Reservas
- Sanciones
- Reportes

---

## Objetivo del proyecto

El objetivo principal fue construir una práctica completa de testing, combinando documentación, análisis manual y automatización.

Se trabajó sobre:

- Análisis del sistema bajo prueba.
- Plan de testing.
- Estrategia de testing.
- Casos de prueba.
- Matriz de trazabilidad.
- Reporte de bugs.
- Evidencia manual.
- Automatización con cinco herramientas.
- Reportes HTML.
- Capturas de evidencia.
- Comparación final entre frameworks.

---

## Frameworks utilizados

<img width="674" height="347" alt="XD" src="https://github.com/user-attachments/assets/c91a4d9b-bb0f-413f-8463-590365b93b34" />

---

## Estructura del proyecto

```text
testing-5-frameworks-project/
├── docs/
├── framework-1-pytest/
├── framework-2-selenium/
├── framework-3-robot-framework/
├── framework-4-playwright/
├── framework-5-locust/
├── evidencias-generales/
├── conclusiones/
├── README.md
└── requirements.txt
```

---

## Documentación incluida

Dentro de la carpeta `docs/` se encuentran los documentos principales del proceso QA:

- Sistema a testear.
- Plan de testing.
- Estrategia de testing.
- Casos de prueba.
- Matriz de trazabilidad.
- Reporte de bugs.
- Evidencia manual.
- Guía para aprender testing.

---

## Bugs detectados

Durante la exploración manual se encontraron errores reales del sistema:

- Error 404 en la sección “Horarios más demandados” del Dashboard.
- Error `Failed to fetch` en el módulo Sanciones.
- Métricas incompletas o valores `N/A` en Reportes.

Estos errores fueron documentados y luego usados como parte de las pruebas automatizadas.

---

## Pruebas realizadas

### Pytest

Se utilizó para validar la API del sistema.

Incluye:

- Verificación del backend.
- Verificación de Swagger.
- Validación de OpenAPI JSON.
- Validación de endpoints principales.

Comando:

```bash
python -m pytest framework-1-pytest/tests -v
```

---

### Selenium

Se utilizó para automatizar pruebas desde la interfaz web.

Incluye:

- Navegación entre módulos.
- Validación de tablas.
- Validación de textos visibles.
- Capturas de evidencia.
- Capturas automáticas ante fallos.
- Pruebas sobre bugs visibles.
- Primer enfoque con Page Object Model.

Comando:

```bash
python -m pytest framework-2-selenium/tests -v
```

---

### Robot Framework

Se utilizó para crear pruebas funcionales legibles, más cercanas a documentación ejecutable.

Incluye:

- Navegación por módulos.
- Validación de contenido visible.
- Capturas.
- Reportes automáticos de Robot Framework.

Comando:

```bash
robot -d framework-3-robot-framework/reports framework-3-robot-framework/tests
```

---

### Playwright

Se utilizó como alternativa moderna para pruebas E2E.

Incluye:

- Navegación entre módulos.
- Validación de tablas.
- Capturas full page.
- Capturas ante fallos.
- Ejecución con navegador visible.
- Traces de Playwright.
- Comparación directa con Selenium.

Comando:

```bash
python -m pytest framework-4-playwright/tests -v
```

Ejecución con navegador visible:

```bash
python -m pytest framework-4-playwright/tests -v --headed
```

Ejecución con traces:

```bash
python -m pytest framework-4-playwright/tests -v --tracing=on
```

---

### Locust

Se utilizó para una primera prueba básica de carga sobre la API.

Incluye:

- Simulación de usuarios concurrentes.
- Medición de requests por segundo.
- Tiempos de respuesta.
- Percentiles.
- Reporte HTML.
- Análisis básico de estabilidad.

Comando con interfaz web:

```bash
locust -f framework-5-locust/locustfile.py --host http://localhost:8000
```

Comando headless con reporte:

```bash
locust -f framework-5-locust/locustfile.py --host http://localhost:8000 --headless -u 10 -r 2 -t 30s --html framework-5-locust/reports/reporte-locust.html
```

---

## Evidencias y reportes

El proyecto incluye:

- Capturas generadas por Selenium.
- Capturas generadas por Playwright.
- Capturas generadas por Robot Framework.
- Reportes HTML de Pytest.
- Reportes HTML de Selenium.
- Reportes de Robot Framework.
- Reporte HTML de Playwright.
- Reporte HTML de Locust.
- Traces de Playwright.
- Documentación de bugs y evidencia manual.

---

## Aprendizajes principales

Con este proyecto se puede ver:

- Cómo analizar un sistema antes de automatizar.
- Cómo diseñar casos de prueba.
- Cómo registrar bugs.
- Cómo documentar evidencia.
- Cómo probar APIs con Pytest.
- Cómo automatizar UI con Selenium.
- Cómo escribir pruebas funcionales con Robot Framework.
- Cómo trabajar E2E con Playwright.
- Cómo iniciar pruebas de carga con Locust.
- Cómo comparar herramientas según su utilidad real.

---

## Autor

**Joaquín Lorenzo González**  
**+54 3537564663**
