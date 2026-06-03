# 01 - Sistema a Testear

## Nombre del sistema

Sistema de Gestión de Salas UCU.

## Objetivo del sistema

Aplicación web orientada a la gestión de salas de estudio, participantes, reservas, sanciones y reportes analíticos.

Este sistema será utilizado como aplicación bajo prueba para desarrollar un proyecto de testing manual y automatizado con diferentes frameworks y herramientas.

---

## Tecnologías identificadas

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- FastAPI
- Python
- Swagger / OpenAPI

### Base de datos

- MySQL
- Docker

### Infraestructura

- Docker Compose

---

## URLs del ambiente local

### Frontend

http://localhost:5173

### Backend

http://localhost:8000

### Documentación Swagger

http://localhost:8000/docs

---

## Módulos principales

- Dashboard
- Participantes
- Salas
- Reservas
- Sanciones
- Reportes

---

## Estado inicial del sistema

Durante la exploración inicial se verificó que el sistema puede ejecutarse localmente y que tanto el frontend como el backend responden correctamente.

### Funcionalidades observadas correctamente

- El backend responde en `http://localhost:8000`.
- Swagger se encuentra disponible en `http://localhost:8000/docs`.
- El frontend carga en `http://localhost:5173`.
- El dashboard se visualiza correctamente.
- El módulo Salas muestra datos.
- El módulo Participantes muestra datos.
- El módulo Reservas muestra datos.
- El módulo Reportes carga parcialmente.

---

## Errores o comportamientos detectados inicialmente

Durante la exploración manual se observaron algunos comportamientos que serán documentados y analizados durante el proceso de testing.

### BUG-001 - Error en Dashboard

En el dashboard se muestra un mensaje de error al cargar la sección “Horarios más demandados”.

**Mensaje observado:**  
Error cargando horarios: Error 404 Not Found

### BUG-002 - Error en módulo Sanciones

Al ingresar al módulo Sanciones, el sistema muestra un error de carga.

**Mensaje observado:**  
Error: Failed to fetch

### BUG-003 - Métricas incompletas en Reportes

En el módulo Reportes se muestran algunas métricas como `N/A`, lo que puede indicar datos faltantes, endpoint incompleto o cálculo no disponible.

---

## Motivo de elección del sistema

Este sistema fue elegido porque permite practicar testing sobre una aplicación full stack real con frontend, backend, base de datos y distintos módulos funcionales.

Aunque el sistema es simple, resulta útil para aplicar diferentes tipos de pruebas:

- Pruebas manuales.
- Pruebas funcionales.
- Pruebas de API.
- Pruebas end-to-end.
- Pruebas de regresión.
- Pruebas básicas de carga.
- Documentación de bugs.
- Generación de evidencias.

---

## Rol del proyecto de testing

El objetivo no es modificar ni mejorar el sistema original, sino utilizarlo como caso práctico para demostrar una estrategia completa de QA.

Este repositorio de testing buscará mostrar:

- Análisis inicial del sistema.
- Diseño de plan de pruebas.
- Documentación de casos de prueba.
- Registro de bugs.
- Automatización con diferentes frameworks.
- Evidencias de ejecución.
- Comparación entre herramientas.
- Conclusiones profesionales.