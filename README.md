# Beer System API

## Dependencias

- **FastAPI**
- **Uvicorn**
- **Dependency Injector**
- **Pytest**
- **Pytest-mock**
- **Pydantic**

## Requisitos Previos

1. **Python**: Asegúrate de tener instalado **Python 3.9 o superior**.
2. **Pip**: Verifica que tienes instalado el manejador de paquetes `pip`.

## Configuración del Entorno

### 1. Crear un Entorno Virtual

Se recomienda usar un entorno virtual para mantener las dependencias del proyecto aisladas.

```bash
python -m venv venv
```

### 2. Activar el Entorno Virtual

- **Windows**:

```bash
venv\\Scripts\\activate
```

- **Mac/Linux**:

```bash
source venv/bin/activate
```

### 3. Instalar Dependencias

Una vez activado el entorno virtual, instala las dependencias listadas en el archivo **requirements.txt**:

```bash
pip install -r requirements.txt
```

## Arrancar Proyecto

### 1. Arrancar el Servidor

Ejecuta el servidor FastAPI con Uvicorn.

```bash
uvicorn app.main:application --reload
```

### 1. Acceder a la API

Una vez que el servidor esté corriendo, accede a la documentación interactiva en:

- **Swagger**: http://127.0.0.1:8000/docs
- **Redoc**: http://127.0.0.1:8000/redoc

## Pruebas

Ejecuta los tests para validar la funcionalidad del proyecto.

```bash
pytest
```
