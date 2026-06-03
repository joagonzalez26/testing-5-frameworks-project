Testing 5 Frameworks Project

Proyecto de QA Automation desarrollado para practicar y documentar pruebas de software utilizando cinco herramientas principales: Pytest, Selenium, Robot Framework, Playwright y Locust.

Este proyecto nace como una práctica personal y profesional para fortalecer mi perfil como QA / Automation Tester. La idea fue tomar un sistema real corriendo en entorno local, analizarlo como tester, documentar su comportamiento, detectar bugs, generar evidencias y automatizar pruebas con distintos enfoques.

Objetivo del proyecto

El objetivo principal fue construir un proyecto completo de testing, no solo ejecutar pruebas aisladas.

Se trabajó sobre:

Análisis del sistema bajo prueba.
Plan de testing.
Casos de prueba.
Reporte de bugs.
Evidencia manual.
Matriz de trazabilidad.
Automatización con cinco frameworks.
Reportes HTML.
Capturas de evidencia.
Comparación final entre herramientas.
Sistema bajo prueba

El sistema utilizado fue un Sistema de Gestión de Salas UCU, ejecutado en entorno local.

Ambiente utilizado:

Frontend: http://localhost:5173
Backend: http://localhost:8000
Swagger: http://localhost:8000/docs
Base de datos: MySQL en Docker

Módulos analizados:

Dashboard
Participantes
Salas
Reservas
Sanciones
Reportes
Frameworks utilizados
Framework	Enfoque	Resultado
Pytest	Pruebas de API	6 tests passed
Selenium	Automatización UI clásica	9 tests passed
Robot Framework	Pruebas funcionales legibles	7 tests passed
Playwright	Pruebas E2E modernas	12 tests passed
Locust	Pruebas básicas de carga	0% fallos
Estructura del proyecto
docs/: documentación principal del proceso QA.
framework-1-pytest/: pruebas de API con Pytest y Requests.
framework-2-selenium/: automatización web con Selenium.
framework-3-robot-framework/: pruebas funcionales con Robot Framework.
framework-4-playwright/: pruebas E2E modernas con Playwright.
framework-5-locust/: pruebas básicas de carga con Locust.
evidencias-generales/: espacio para evidencias generales.
conclusiones/: comparación final entre frameworks.
Documentación incluida

Dentro de docs/ se incluye:

Sistema a testear.
Plan de testing.
Estrategia de testing.
Casos de prueba.
Matriz de trazabilidad.
Reporte de bugs.
Evidencia manual.
Guía para aprender testing.
Resultados principales

Durante el proyecto se validaron distintos aspectos del sistema:

Disponibilidad del backend.
Carga de Swagger.
Respuesta de endpoints principales.
Carga del frontend.
Navegación entre módulos.
Visualización de tablas.
Bugs visibles desde la interfaz.
Métricas incompletas.
Errores en módulos específicos.
Comportamiento básico del backend bajo carga.

También se generaron capturas, reportes HTML y documentación para cada framework.

Bugs detectados

Durante la exploración inicial se detectaron errores reales del sistema:

Error 404 en la sección “Horarios más demandados” del Dashboard.
Error Failed to fetch en el módulo Sanciones.
Métricas incompletas o valores N/A en Reportes.

Estos errores fueron documentados y luego utilizados como parte de las pruebas automatizadas.

Cómo ejecutar las pruebas
Pytest

python -m pytest framework-1-pytest/tests -v

Selenium

python -m pytest framework-2-selenium/tests -v

Robot Framework

robot -d framework-3-robot-framework/reports framework-3-robot-framework/tests

Playwright

python -m pytest framework-4-playwright/tests -v

Locust

locust -f framework-5-locust/locustfile.py --host http://localhost:8000

Modo headless con reporte:

locust -f framework-5-locust/locustfile.py --host http://localhost:8000 --headless -u 10 -r 2 -t 30s --html framework-5-locust/reports/reporte-locust.html

Evidencias y reportes

El proyecto incluye:

Capturas generadas por Selenium.
Capturas generadas por Playwright.
Capturas generadas por Robot Framework.
Reportes HTML de Pytest.
Reportes HTML de Selenium.
Reportes de Robot Framework.
Reportes HTML de Playwright.
Reporte HTML de Locust.
Traces de Playwright.
Aprendizajes principales

Este proyecto me permitió practicar una forma más completa de trabajo QA:

Pensar antes de automatizar.
Analizar un sistema real.
Documentar casos de prueba.
Registrar bugs.
Asociar pruebas con evidencia.
Automatizar API.
Automatizar interfaz web.
Comparar herramientas.
Interpretar resultados.
Generar documentación útil para portfolio.
Conclusión

Este proyecto demuestra una estrategia inicial completa de QA Automation aplicada sobre un sistema real.

No se trata solo de ejecutar herramientas, sino de mostrar un proceso: analizar, probar manualmente, documentar, automatizar, generar evidencia y comparar resultados.

El objetivo final es fortalecer mi perfil como QA / Automation Tester y construir un portfolio profesional con proyectos reales, documentados y explicados.

Autor

Joaquín González
Estudiante de Analista en Sistemas de Computación
Perfil orientado a QA Automation, testing manual, automatización, documentación técnica y desarrollo de software.