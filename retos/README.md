# 🧩 Reto: Extender CRUD 

## 🎯 Objetivo

Ampliar el sistema de gestión de usuarios implementando un nuevo modelo que permita enriquecer los datos del usuario, estableciendo una relación útil para futuras fases del sistema.

---

## 📚 Contexto

La implementación actual cuenta con un CRUD de usuarios que permite:

- Crear usuarios
- Consultarlos individual o colectivamente
- Actualizar sus datos
- Eliminar un registro

Este reto propone mejorar la estructura y lógica del backend, agregando una nueva entidad relacionada a los usuarios que permita gestionar información adicional y relevante.

---

## 🛠️ Requerimientos del Reto

### 1. Modelado

Diseñar e implementar un nuevo modelo, que debe contener al menos:

- Rol (Ej: estudiante, docente, administrador)
- Estado del registro facial (Ej: registrado, pendiente, fallido)
- Fecha de creación

Debes proponer incluir al menos un campo más.

### 2. Relación

Establecer una relación adecuada entre el usuario y esta nueva entidad (uno a uno o uno a muchos - Investigar la mejor forma).

### 3. Endpoints

Implementar los endpoints necesarios para:

- Crear y asociar una ficha o perfil al usuario
- Consultar dicha ficha por usuario
- Modificar los datos adicionales
- Eliminar

---


## 🧪 Ejemplo de respuesta esperada al traer un usuario

```json
{
  "id": "c3e12c90-ffe4-11ee-8c6a-5c4d2af40c2e",
  "nombre": "María González",
  "email": "maria@ejemplo.com",
  "perfil": {
    "rol": "docente",
    "estado_rostro": "pendiente",
    "creado_en": "2025-03-25T10:32:00"
  }
}
