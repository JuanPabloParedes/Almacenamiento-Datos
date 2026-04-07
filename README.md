# Almacenamiento-Datos

## Sistema Web de Reservas de Salas por Facultad

## Descripción

Este proyecto tiene como objetivo el diseño e implementación de la base de datos que soporta el backend del Sistema Web de Reservas de Salas de Reuniones por Facultad.  

La solución busca centralizar la gestión de salas dentro de una institución universitaria, reemplazando procesos manuales basados en calendarios compartidos.  

Se enfoca en garantizar la integridad, consistencia y trazabilidad de la información, permitiendo una administración eficiente de usuarios, salas y reservas.

---

## Objetivos del Proyecto

- Diseñar un modelo de datos robusto (conceptual, lógico y físico).
- Implementar una base de datos relacional y documental.
- Gestionar usuarios con roles definidos (Docente y Secretaria).
- Administrar salas de reuniones por facultad.
- Controlar reservas evitando conflictos de horario.
- Garantizar auditoría y trazabilidad de todas las acciones.
- Facilitar consultas analíticas y reportes históricos.

---

## Alcance

### El proyecto cubre:

- Modelado conceptual de la base de datos.
- Modelado lógico e implementación en SQL.
- Construcción de consultas de complejidad media-alta.
- Desarrollo de objetos almacenados:
  - Procedimientos
  - Funciones
  - Triggers
- Modelado de base de datos documental (NoSQL).
- Construcción de agregaciones para análisis de datos.

### No incluye:

- Desarrollo de frontend.
- Implementación completa del sistema web.

---

## Funcionalidades Principales

### Gestión de Usuarios

- Registro, actualización e inactivación de usuarios.
- Roles:
  - DOCENTE
  - SECRETARIA
- Asociación de usuarios a una facultad.

### Gestión de Salas

- Registro de salas por facultad.
- Información almacenada:
  - Identificador
  - Nombre o código
  - Recursos disponibles (proyector, mesas, etc.)
  - Estado (habilitada/deshabilitada)
  - Observaciones

### Gestión de Reservas

- Creación, modificación y cancelación de reservas.
- Información clave:
  - Sala
  - Usuario
  - Fecha y rango horario
  - Estado de la reserva

### Reglas de Negocio

- Horario permitido: 7:00 a.m. – 9:30 p.m.
- Prohibición de solapamiento de reservas por sala.
- Restricciones por rol:
  - Docentes: reservan y cancelan sus propias reservas.
  - Secretarias: pueden gestionar reservas dentro de su facultad.

### Auditoría y Trazabilidad

- Registro de eventos:
  - Creación
  - Modificación
  - Cancelación
- Almacenamiento de:
  - Usuario responsable
  - Fecha y hora de la acción

---

## Modelo de Datos

El diseño del sistema contempla:

- Integridad referencial entre entidades.
- Control de estados y validaciones.
- Estructuras optimizadas para consultas.
- Soporte para escalabilidad.
- Capacidad de análisis histórico.

---

## Consultas y Análisis

El sistema incluye:

- Consultas SQL de nivel medio-alto orientadas a análisis.
- Generación de reportes por rango de fechas.
- Agregaciones en base de datos documental.

---

## Tecnologías Utilizadas

- SQL (Bases de datos relacionales)
- NoSQL (Bases de datos documentales)
- Modelado de datos (conceptual y lógico)
- Procedimientos almacenados
- Funciones y triggers
- Git y GitHub

---

## Hitos del Proyecto

| Semana | Fecha       | Entrega |
|--------|------------|--------|
| 6      | 04/03/2026 | Modelado conceptual | 
| 11     | 13/04/2026 | Modelo lógico, implementación, consultas y objetos almacenados |
| 17     | 25/05/2026 | Modelo documental y agregaciones |

---

## Trabajo en Equipo

Este proyecto se desarrolla de manera colaborativa, promoviendo:

- Responsabilidad individual y colectiva.
- Participación activa de todos los integrantes.
- Uso de herramientas de control de versiones.
- Organización del código y documentación en GitHub.
