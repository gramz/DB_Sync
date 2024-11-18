# Database Synchronization Tool

Herramienta para sincronizar datos entre SQL Server y MySQL.

## Características

- Sincronización bidireccional entre SQL Server y MySQL
- Mapeo flexible de tablas y campos
- Programación de sincronización automática
- Sistema de logging detallado
- Manejo de errores robusto

## Requisitos

- Python 3.8 o superior
- SQL Server ODBC Driver
- Acceso a bases de datos SQL Server y MySQL

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/db_sync.git
   cd db_sync
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Copiar y configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

## Uso

1. Configurar el mapeo de tablas en `src/config/table_mappings.py`
2. Ejecutar el sincronizador:
   ```bash
   python main.py
   ```

## Desarrollo

1. Instalar dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Ejecutar pruebas:
   ```bash
   pytest
   ```

3. Verificar estilo de código:
   ```bash
   pylint src/
   black src/
   ```
# Database Synchronization Tool

Herramienta para sincronizar datos entre SQL Server y MySQL.

## Características

- Sincronización bidireccional entre SQL Server y MySQL
- Mapeo flexible de tablas y campos
- Programación de sincronización automática
- Sistema de logging detallado
- Manejo de errores robusto

## Requisitos

- Python 3.8 o superior
- SQL Server ODBC Driver
- Acceso a bases de datos SQL Server y MySQL

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/db_sync.git
   cd db_sync
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Copiar y configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

## Uso

1. Configurar el mapeo de tablas en `src/config/table_mappings.py`
2. Ejecutar el sincronizador:
   ```bash
   python main.py
   ```

## Desarrollo

1. Instalar dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Ejecutar pruebas:
   ```bash
   pytest
   ```

3. Verificar estilo de código:
   ```bash
   pylint src/
   black src/
   ```

## Licencia

MIT
