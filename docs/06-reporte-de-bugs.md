# 06 - Reporte de Bugs

## Objetivo

Este documento registra los errores, comportamientos inesperados y observaciones detectadas durante la exploración inicial del Sistema de Gestión de Salas UCU.

El objetivo no es corregir el sistema original, sino documentar los hallazgos como parte del proceso profesional de QA.

---

## Ambiente de prueba

* Sistema bajo prueba: Sistema de Gestión de Salas UCU
* Frontend: http://localhost:5173
* Backend: http://localhost:8000
* Swagger: http://localhost:8000/docs
* Base de datos: MySQL en Docker
* Navegador utilizado: Google Chrome
* Sistema operativo: macOS

---

## BUG-001 - Error 404 en sección “Horarios más demandados”

### Módulo

Dashboard

### Severidad

Media

### Prioridad

Media

### Tipo de error

Error de integración frontend/backend o endpoint no encontrado.

### Descripción

Al ingresar al dashboard, la sección “Horarios más demandados” muestra un error visible en pantalla.

### Pasos para reproducir

1. Levantar backend y base de datos con Docker.
2. Levantar frontend con Vite.
3. Ingresar a `http://localhost:5173`.
4. Observar la sección “Horarios más demandados” dentro del dashboard.

### Resultado esperado

El sistema debería mostrar los horarios más demandados o, en caso de no existir datos, un mensaje controlado para el usuario.

### Resultado obtenido

El sistema muestra el mensaje:

`Error cargando horarios: Error 404 Not Found`

### Estado

Abierto

### Caso de prueba relacionado

CP-005

### Observación QA

El error indica que el frontend intenta consultar un recurso que no existe, no está implementado o no coincide con la ruta definida en el backend.

---

## BUG-002 - Error “Failed to fetch” en módulo Sanciones

### Módulo

Sanciones

### Severidad

Alta

### Prioridad

Alta

### Tipo de error

Error de carga de datos / posible endpoint inexistente o problema de conexión.

### Descripción

Al ingresar al módulo Sanciones, el sistema no muestra datos y presenta un mensaje de error visible.

### Pasos para reproducir

1. Ingresar a `http://localhost:5173`.
2. Seleccionar el módulo Sanciones desde el menú lateral.
3. Observar el comportamiento de la pantalla.

### Resultado esperado

El sistema debería mostrar el listado de sanciones o un mensaje controlado indicando que no existen datos cargados.

### Resultado obtenido

El sistema muestra el mensaje:

`Error: Failed to fetch`

### Estado

Abierto

### Caso de prueba relacionado

CP-009

### Observación QA

El error puede estar relacionado con un endpoint no disponible, una ruta incorrecta, un problema de CORS o una falla en la comunicación entre frontend y backend.

---

## BUG-003 - Métricas incompletas en módulo Reportes

### Módulo

Reportes

### Severidad

Baja / Media

### Prioridad

Media

### Tipo de error

Datos incompletos o cálculo no disponible.

### Descripción

El módulo Reportes carga parcialmente, pero algunas métricas se muestran como `N/A`.

### Pasos para reproducir

1. Ingresar a `http://localhost:5173`.
2. Seleccionar el módulo Reportes.
3. Observar las tarjetas y métricas principales.

### Resultado esperado

El sistema debería mostrar métricas completas y coherentes en base a los datos disponibles.

### Resultado obtenido

Algunas métricas aparecen como:

`N/A`

### Estado

Abierto

### Caso de prueba relacionado

CP-010

### Observación QA

Este comportamiento puede indicar falta de datos, endpoint incompleto, cálculo no implementado o ausencia de manejo visual para valores nulos.

---

## Resumen de bugs encontrados

| ID      | Módulo    | Descripción                          | Severidad    | Prioridad | Estado  |
| ------- | --------- | ------------------------------------ | ------------ | --------- | ------- |
| BUG-001 | Dashboard | Error 404 en horarios más demandados | Media        | Media     | Abierto |
| BUG-002 | Sanciones | Error Failed to fetch                | Alta         | Alta      | Abierto |
| BUG-003 | Reportes  | Métricas incompletas N/A             | Baja / Media | Media     | Abierto |

---

## Observación general

Durante la exploración inicial, el sistema logró ejecutarse correctamente y varios módulos funcionaron de forma esperada. Sin embargo, se detectaron errores visibles en algunos módulos, principalmente relacionados con carga de datos, endpoints o manejo de respuestas incompletas.

Estos bugs serán utilizados como parte del proyecto de testing para:

* Documentar hallazgos reales.
* Asociar errores con casos de prueba.
* Automatizar validaciones.
* Generar evidencia.
* Comparar cómo distintos frameworks detectan o validan comportamientos incorrectos.

---

## Conclusión inicial

La existencia de errores visibles convierte al sistema en un caso útil para practicar testing realista. El objetivo del proyecto no será ocultar estos problemas, sino registrarlos correctamente y usarlos como evidencia de análisis QA.
