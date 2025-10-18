# Sistema de Gestión y Priorización del Transporte Universitario — Universidad de La Guajira


# Autores: 
- Cristian David Muñoz Hernández  
- Jaime Rafael González Ballesta  

---

# Descripción general

    Rutas_Uniguajiraes una aplicación web desarrollada en Django cuyo propósito es **optimizar el uso del transporte universitario** de la Universidad de La Guajira (sede Riohacha).  
El sistema permite **registrar rutas, estudiantes, reservas y buses**, aplicando un **algoritmo de priorización** que otorga los cupos disponibles a los estudiantes con **mejor promedio académico** y **mayor vulnerabilidad socioeconómica (SISBEN A o B)**.

Este proyecto busca aportar una herramienta tecnológica que fomente la equidad, la eficiencia y la inclusión en el acceso al transporte institucional.

---
 # Estructura del proyecto

administracion/ # Gestión administrativa, rutas y reportes
│
estudiantes/ # Registro de estudiantes y sus datos académicos
│
reservas/ # Módulo de solicitudes y asignación de cupos
│
rutas/ # Información de las rutas disponibles y sus buses
│
transporte_universitario/ # Proyecto principal (configuración Django)

# Funcionalidades principales

| Estudiante: 

-Registro de estudiantes.

-Almacenamiento de promedio académico y grupo SISBEN.

-Visualización de sus reservas activas.

| Rutas:

- Creación y edición de rutas universitarias.

- Definición de capacidad por buseta (40 asientos por defecto).

- Estado de la ruta (Activa / En mantenimiento).

# Reservas

- Registro de solicitudes de transporte por parte de los estudiantes.

- Estados de la reserva: Aceptada, En espera o Rechazada.

- Control de capacidad de cada ruta.

# Administración

- Acceso al panel de Django Admin.

- Gestión de rutas, estudiantes, reservas y buses.

- Visualización de reportes de capacidad y ocupación.

- Autoriza las reservas. Cambia el estado (Aceptada, En espera o Rechazada)

# Caso de uso principal: Asignación de transporte

Actor principal: Estudiante
Actor secundario: Administrador
Propósito: Permitir que un estudiante reserve un cupo de transporte universitario con prioridad basada en su desempeño académico y nivel socioeconómico.

Flujo principal:

El estudiante solicita un cupo.

El administrador revisa la disponibilidad

Si hay espacio, la reserva se marca como “Aceptada”.

Si no hay cupos, pasa a “En espera”.

El administrador puede revisar o modificar el estado desde el panel.

Postcondición:
La reserva queda registrada en el sistema y puede consultarse desde el panel de administración.

# Tecnologías usadas: 

Python: 3.13.7
Django: 5.2.6

    Este proyecto busca aplicar Django en una solución práctica para la
Uniguajira, integrando programación avanzada, algoritmos de priorización y
gestión de datos en un entorno web. El resultado esperado es un sistema que
promueva la permanencia, la equidad y la eficiencia en el servicio de transporte
estudiantil.

Universidad de La Guajira – Programa de Ingeniería de Sistemas
Asignatura: Programación Avanzada
Docente: Bryan J. Otero Arrieta
Periodo: 2025-II