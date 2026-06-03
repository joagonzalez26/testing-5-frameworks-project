## Comparación de Frameworks

# Objetivo

Este documento presenta una comparación general entre los cinco frameworks utilizados en el proyecto: Pytest, Selenium, Robot Framework, Playwright y Locust.

La finalidad es registrar qué aporta cada herramienta, en qué tipo de pruebas se utilizó, qué aprendí durante el proceso y cómo se complementan dentro de una estrategia QA más completa.

# Resumen general
Framework	Enfoque principal	Uso en el proyecto
Pytest	Pruebas de API y backend	Validación de endpoints principales
Selenium	Automatización web clásica	Navegación, tablas, bugs visibles y capturas
Robot Framework	Pruebas funcionales legibles	Casos funcionales expresados como documentación
Playwright	Automatización E2E moderna	Navegación, tablas, bugs, capturas y traces
Locust	Pruebas de carga	Simulación de usuarios concurrentes sobre la API
Pytest

# Pytest fue utilizado para validar la capa de API del sistema.

Permitió comprobar que el backend estuviera disponible, que Swagger cargara correctamente y que los endpoints principales respondieran con status code exitoso.

Aportes principales
Rápido de ejecutar.
Ideal para pruebas de API.
Simple de combinar con Requests.
Muy útil para smoke tests.
Fácil de integrar con reportes HTML.
Aprendizaje

Pytest me permitió entender la importancia de validar primero la base técnica del sistema antes de avanzar con pruebas de interfaz.

# Selenium

Selenium fue uno de los bloques más importantes del proyecto.

Se utilizó para automatizar pruebas desde la interfaz real del navegador, validando navegación, módulos principales, tablas, textos visibles, bugs detectados y capturas de evidencia.

Aportes principales
Automatización web clásica.
Muy utilizado en el mercado QA.
Permite interactuar con navegadores reales.
Compatible con Pytest.
Permite aplicar Page Object Model.
Útil para generar capturas como evidencia.
Aprendizaje

Selenium me ayudó a comprender mejor cómo automatizar desde la mirada del usuario final. También me permitió practicar buenas prácticas como fixtures, conftest.py, Page Object inicial, parametrización y capturas automáticas ante fallos.

# Robot Framework

Robot Framework fue utilizado para escribir pruebas funcionales de una forma más legible.

A diferencia de Selenium puro con Python, Robot permite que los casos se lean casi como documentación funcional ejecutable.

Aportes principales
Sintaxis clara.
Casos fáciles de leer.
Reportes automáticos muy completos.
Buena herramienta para pruebas funcionales.
Útil para comunicar escenarios a perfiles técnicos y no técnicos.
Aprendizaje

Robot Framework me permitió ver otra forma de automatizar pruebas, más orientada a documentación y aceptación funcional.

# Playwright

Playwright fue trabajado como una alternativa moderna a Selenium para pruebas end-to-end.

Se utilizó para validar navegación, módulos principales, tablas, bugs visibles, capturas full page y traces de ejecución.

Aportes principales
Ejecución rápida.
Esperas automáticas.
Sintaxis moderna.
Buen soporte para pruebas E2E.
Capturas full page.
Traces para depuración.
Muy útil para comparar con Selenium.
Aprendizaje

Playwright me permitió entender una forma más moderna de automatizar pruebas web. En comparación con Selenium, se sintió más rápido y directo para ciertos escenarios.

# Locust

Locust fue utilizado para realizar una prueba básica de carga sobre la API del sistema.

Se simularon usuarios concurrentes consultando endpoints principales del backend, observando requests, fallos, tiempos promedio, percentiles y requests por segundo.

Aportes principales
Simulación de usuarios concurrentes.
Medición de tiempos de respuesta.
Visualización de estadísticas.
Reporte HTML.
Buena introducción al performance testing.
Aprendizaje

Locust me permitió comprender que el testing no se limita a validar si una función anda o no, sino también a observar cómo responde el sistema ante cierta carga.

# Comparación entre Selenium y Playwright

Selenium y Playwright fueron los dos frameworks más importantes para automatización de interfaz.

Selenium

Selenium representa una herramienta clásica, madura y muy conocida en el mercado laboral QA. Es ideal para aprender automatización web desde sus fundamentos y comprender cómo interactuar con elementos reales del navegador.

Playwright

Playwright representa una herramienta más moderna, rápida y cómoda para pruebas end-to-end. Sus esperas automáticas, capturas full page y traces facilitan mucho el análisis y la depuración.

# Conclusión comparativa

Selenium me parece fundamental para aprender y fortalecer mi perfil QA Automation porque sigue siendo muy demandado. Playwright, en cambio, me parece una herramienta moderna que suma mucho valor para proyectos actuales.

Ambos se complementan muy bien: Selenium aporta base clásica y mercado; Playwright aporta velocidad, modernidad y experiencia E2E más avanzada.

# Qué aprendí del proyecto

Este proyecto me permitió practicar una forma de trabajo más completa como tester:

Analizar un sistema antes de automatizar.
Documentar el sistema bajo prueba.
Crear un plan de testing.
Diseñar casos de prueba.
Registrar bugs reales.
Generar evidencia manual.
Automatizar pruebas de API.
Automatizar pruebas de interfaz.
Generar reportes.
Comparar frameworks.
Interpretar resultados.
Pensar el testing como proceso, no solo como ejecución de scripts.
Conclusión final

- Este proyecto demuestra una estrategia QA completa en etapa inicial, combinando testing manual, automatización, documentación, evidencia y análisis comparativo.

- No se trató solamente de ejecutar herramientas, sino tambíen de entender qué aporta cada una y cómo pueden formar parte de un proceso profesional de aseguramiento de calidad.

- El resultado final es un proyecto útil para aprendizaje, práctica y portfolio profesional como QA Automation Tester.

# Con mucho gusto, Joaquín Lorenzo Gonzalez ;)

