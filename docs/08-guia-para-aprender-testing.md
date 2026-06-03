# 08 - Guía para Aprender Testing

## Objetivo

Esta guía reúne conceptos básicos y prácticos sobre testing de software, tomando como referencia el proyecto realizado sobre el Sistema de Gestión de Salas UCU.

La idea es que este documento funcione como apoyo de aprendizaje y también como evidencia de comprensión sobre los distintos tipos de pruebas aplicados durante el proyecto.

---

## ¿Qué es el testing de software?

El testing de software es el proceso de analizar, ejecutar y validar un sistema para comprobar si funciona de acuerdo con lo esperado.

No se trata solamente de encontrar errores. También permite:

* Verificar funcionalidades.
* Detectar riesgos.
* Documentar comportamientos.
* Mejorar la calidad del sistema.
* Aportar confianza antes de entregar un producto.
* Entender cómo se comporta una aplicación desde la mirada del usuario.

---

## Testing manual

El testing manual consiste en probar el sistema directamente, interactuando con la interfaz como lo haría un usuario real.

En este proyecto se aplicó testing manual para:

* Explorar el sistema.
* Conocer sus módulos.
* Detectar errores visibles.
* Revisar navegación.
* Observar datos cargados.
* Registrar evidencia inicial.

Antes de automatizar, es importante probar manualmente, porque eso permite entender qué tiene sentido automatizar y qué partes del sistema presentan mayor riesgo.

---

## Testing automatizado

El testing automatizado consiste en escribir scripts o pruebas que ejecutan validaciones de forma automática.

Sirve para:

* Repetir pruebas rápidamente.
* Ahorrar tiempo en regresiones.
* Validar funcionalidades críticas.
* Detectar errores después de cambios.
* Generar reportes.
* Mantener evidencia técnica.

Automatizar no significa probar todo. Lo importante es elegir escenarios que aporten valor.

---

## Testing de API

El testing de API valida la comunicación con el backend.

Permite comprobar:

* Status codes.
* Respuestas JSON.
* Endpoints disponibles.
* Errores de servidor.
* Datos devueltos.
* Integración entre frontend y backend.

En este proyecto se usarán herramientas como Pytest, Requests y Postman para probar endpoints del sistema.

---

## Testing end-to-end

El testing end-to-end valida un flujo completo desde la perspectiva del usuario.

Por ejemplo:

1. Abrir la aplicación.
2. Navegar a un módulo.
3. Completar un formulario.
4. Guardar datos.
5. Verificar que el cambio aparece en pantalla.

En este proyecto se usarán Selenium y Playwright para automatizar pruebas desde el navegador.

---

## Testing funcional

El testing funcional verifica que cada módulo cumpla su propósito.

Ejemplos:

* El módulo Salas debe mostrar salas.
* El módulo Participantes debe mostrar participantes.
* El módulo Reservas debe mostrar reservas.
* El módulo Sanciones debería cargar información sin errores.
* El dashboard debería mostrar métricas sin fallos visibles.

---

## Testing de regresión

El testing de regresión consiste en volver a ejecutar pruebas para verificar que una funcionalidad que antes funcionaba siga funcionando después de cambios.

Es muy importante en proyectos reales porque muchas veces una modificación puede romper algo que ya estaba correcto.

---

## Testing de performance básico

El testing de performance permite observar cómo responde un sistema bajo cierta carga.

En este proyecto se usará Locust para simular usuarios realizando peticiones al backend.

No se buscará hacer una prueba de rendimiento avanzada, sino una primera aproximación para entender tiempos de respuesta y comportamiento del sistema.

---

## Herramientas utilizadas en este proyecto

## Pytest

Framework de testing en Python utilizado principalmente para pruebas de API y validaciones rápidas.

Se usará para comprobar endpoints, status codes y respuestas del backend.

## Selenium

Framework clásico de automatización web.

Se usará con especial profundidad para automatizar navegación, validar elementos visibles y aplicar buenas prácticas como Page Object Model.

## Robot Framework

Framework orientado a pruebas funcionales y de aceptación.

Permite escribir casos de prueba de forma clara y legible.

## Playwright

Herramienta moderna para pruebas end-to-end.

Permite automatizar navegadores de forma rápida y estable.

## Locust

Herramienta para pruebas de carga.

Permite simular usuarios concurrentes y medir respuestas del backend.

## Postman

Herramienta complementaria para explorar y validar APIs de forma manual o semiautomatizada.

---

## Buenas prácticas de testing

Algunas buenas prácticas aplicadas o consideradas en este proyecto:

* Entender el sistema antes de automatizar.
* Documentar lo observado.
* Separar testing manual de testing automatizado.
* Asociar bugs con casos de prueba.
* Generar evidencia.
* Usar nombres claros para los tests.
* Mantener ordenada la estructura del proyecto.
* No automatizar sin criterio.
* Priorizar módulos críticos.
* Comparar herramientas según su utilidad real.

---

## Aprendizaje esperado

Con este proyecto se busca aprender y practicar:

* Cómo analizar un sistema bajo prueba.
* Cómo diseñar casos de prueba.
* Cómo registrar bugs.
* Cómo documentar evidencia.
* Cómo automatizar pruebas de API.
* Cómo automatizar pruebas de interfaz.
* Cómo comparar frameworks.
* Cómo construir un portfolio QA profesional.

---

## Conclusión

El testing es una forma de pensar el software con mirada crítica, curiosa y ordenada.

Este proyecto busca demostrar que un buen tester no solo ejecuta pruebas, sino que observa, analiza, documenta, automatiza, compara herramientas y comunica resultados de forma clara.

La automatización es importante, pero el criterio del tester sigue siendo la base del proceso.
