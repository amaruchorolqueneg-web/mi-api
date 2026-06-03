# Mi API REST con FastAPI

API REST completa construida con FastAPI, SQLAlchemy y autenticación JWT.

## Tecnologías
- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib + Bcrypt

## Estructura del proyecto

mi-api/
├── app/
│   ├── auth.py
│   ├── database/
│   │   └── database.py
│   ├── models/
│   │   ├── tarea.py
│   │   └── usuario.py
│   ├── schemas/
│   │   ├── tarea.py
│   │   └── usuario.py
│   └── routers/
│       ├── tareas.py
│       └── auth.py
├── main.py
└── requirements.txt

## Instalación

```bash
git clone https://github.com/amaruchorolqueneg-web/mi-api.git
cd mi-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Correr el servidor

```bash
uvicorn main:app --reload
```

Entrá a `http://127.0.0.1:8000/docs` para ver la documentación interactiva.

## Endpoints

### Autenticación
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | /register | Registrar usuario |
| POST | /login | Iniciar sesión y obtener token |

### Tareas (requieren autenticación)
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /tareas | Listar todas las tareas |
| POST | /tareas | Crear una tarea |
| GET | /tareas/{id} | Obtener una tarea |
| PUT | /tareas/{id} | Actualizar una tarea |
| DELETE | /tareas/{id} | Borrar una tarea |

## Uso

### 1. Registrarse
```json
POST /register
{
    "email": "usuario@gmail.com",
    "password": "123456"
}
```

### 2. Loguearse
```json
POST /login
{
    "username": "usuario@gmail.com",
    "password": "123456"
}
```

### 3. Usar el token
Copiá el `access_token` de la respuesta y usalo en el header:

### 4. Crear una tarea
```json
POST /tareas
{
    "titulo": "Estudiar Python",
    "descripcion": "Ver FastAPI",
    "completada": false
}
```
