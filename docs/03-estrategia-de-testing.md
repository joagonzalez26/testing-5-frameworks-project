# 03 - Estrategia de Testing

## Objetivo de la estrategia

El objetivo de esta estrategia es definir cómo se va a abordar el proceso de testing del Sistema de Gestión de Salas UCU utilizando diferentes frameworks y herramientas.

La idea principal no es automatizar pruebas de forma aislada, sino construir un proceso de QA ordenado, documentado y progresivo, donde cada herramienta cumpla un rol claro dentro del proyecto.

Este trabajo busca reflejar una forma de testing curiosa, completa, humana y profesional: primero entendiendo el sistema, luego explorándolo manualmente, documentando comportamientos, identificando riesgos y finalmente automatizando escenarios relevantes.

---

## Enfoque general

El proyecto se organiza en dos grandes etapas:

### 1. Testing manual y exploratorio

Antes de automatizar, se realiza una exploración manual del sistema para entender:

* Qué módulos tiene.
* Qué funcionalidades están disponibles.
* Qué datos muestra.
* Qué errores aparecen desde la interfaz.
* Qué flujos son más importantes.
* Qué partes conviene automatizar.

Esta etapa es clave porque permite pensar como usuario y como tester antes de escribir código.

### 2. Testing automatizado con frameworks

Después de la exploración manual, se automatizan pruebas seleccionadas con diferentes herramientas, según el tipo de validación que se quiera realizar.

No todos los frameworks resuelven el mismo problema. Por eso, cada uno será usado con un propósito específico.

---

## Frameworks seleccionados

## Framework 1 - Pytest

Pytest será utilizado principalmente para pruebas de API y validaciones técnicas del backend.

Se usará para:

* Verificar que el backend responde correctamente.
* Probar endpoints principales.
* Validar status codes.
* Validar respuestas JSON.
* Automatizar pruebas rápidas y repetibles.

Pytest será la base para comprobar que la API funciona correctamente antes de avanzar con pruebas más complejas de interfaz.

---

## Framework 2 - Selenium

Selenium será uno de los frameworks más importantes del proyecto.

Se trabajará con especial profundidad porque es una herramienta clásica, muy utilizada en el mercado QA y muy valiosa para automatización web.

Se usará para:

* Automatizar navegación en el navegador.
* Validar que las páginas cargan correctamente.
* Probar módulos visibles del sistema.
* Interactuar con botones, tablas y formularios.
* Validar errores visibles en pantalla.
* Generar evidencia mediante capturas.
* Aplicar buenas prácticas como Page Object Model.

La idea no será hacer una prueba básica con Selenium, sino aprender a estructurar automatización de forma más profesional.

---

## Framework 3 - Robot Framework

Robot Framework será utilizado para pruebas funcionales y de aceptación.

Se usará para escribir pruebas más legibles, cercanas a documentación funcional, permitiendo expresar escenarios de una forma clara para perfiles técnicos y no técnicos.

Se usará para:

* Crear casos de prueba con lenguaje más descriptivo.
* Validar flujos principales del sistema.
* Generar reportes propios de Robot Framework.
* Comparar su claridad frente a otros frameworks.

Robot Framework ayudará a mostrar otra forma de documentar y ejecutar pruebas automatizadas.

---

## Framework 4 - Playwright

Playwright será utilizado para pruebas end-to-end modernas.

Se usará para:

* Automatizar flujos de usuario desde el navegador.
* Validar navegación entre módulos.
* Comprobar elementos visibles.
* Ejecutar pruebas web de forma rápida y estable.
* Comparar su experiencia con Selenium.

Playwright permitirá analizar una alternativa más moderna para automatización web.

---

## Framework 5 - Locust

Locust será utilizado para pruebas básicas de carga y rendimiento.

Se usará para:

* Simular usuarios concurrentes.
* Enviar múltiples peticiones al backend.
* Medir tiempos de respuesta.
* Observar el comportamiento del sistema bajo carga simple.

No se buscará hacer performance testing avanzado, sino una primera aproximación práctica al rendimiento de APIs.

---

## Herramienta complementaria - Postman

Postman será utilizado como herramienta complementaria para testing de APIs.

Aunque no se lo considera un framework de Python, se incluirá por su uso frecuente en entornos reales de QA.

Se usará para:

* Explorar endpoints.
* Crear una colección de pruebas manuales de API.
* Documentar requests importantes.
* Validar respuestas del backend.
* Comparar pruebas manuales de API con pruebas automatizadas usando Pytest.

---

## Criterio para elegir qué automatizar

No se automatizará todo el sistema de manera indiscriminada.

Se priorizarán escenarios que aporten valor:

* Funcionalidades críticas.
* Módulos principales.
* Flujos repetitivos.
* Endpoints importantes.
* Errores visibles.
* Validaciones fáciles de repetir.
* Casos que sirvan para comparar frameworks.

La automatización se usará como una herramienta para mejorar el proceso de testing, no como un fin en sí mismo.

---

## Estrategia por capas

El testing se organizará por capas:

### Capa 1 - API

Validar que el backend responde correctamente.

Herramientas:

* Pytest
* Requests
* Postman

### Capa 2 - Interfaz web

Validar que el usuario puede navegar e interactuar con el sistema.

Herramientas:

* Selenium
* Playwright
* Robot Framework

### Capa 3 - Performance básica

Validar el comportamiento del backend ante múltiples peticiones.

Herramienta:

* Locust

### Capa 4 - Documentación y evidencia

Registrar resultados, bugs, capturas, reportes y conclusiones.

Documentos:

* Casos de prueba.
* Reporte de bugs.
* Evidencia manual.
* Comparación de frameworks.
* Lecciones aprendidas.

---

## Enfoque profesional

Este proyecto busca mostrar una forma de trabajo realista:

* Primero se analiza el sistema.
* Luego se explora manualmente.
* Después se documentan hallazgos.
* Luego se automatizan pruebas importantes.
* Finalmente se comparan herramientas y se sacan conclusiones.

El objetivo es que el repositorio no solo muestre código, sino también criterio, orden, aprendizaje y forma de trabajo profesional como QA Automation Tester.
