# proyecto-scheduler

https://github.com/Serdan1/proyecto-scheduler.git


# Proyecto Scheduler

Este proyecto implementa un simulador de planificación de procesos para un sistema operativo, desarrollado en Python utilizando programación orientada a objetos. El programa permite gestionar procesos, planificar su ejecución con algoritmos como FCFS (First-Come, First-Served) y Round-Robin, calcular métricas de rendimiento, y persistir los datos en archivos JSON y CSV. Incluye pruebas unitarias y una estructura profesional del proyecto.

## Descripción

El proyecto modela un entorno simplificado de un sistema operativo donde se pueden:
- Registrar y gestionar procesos con atributos como PID, duración y prioridad.
- Planificar la ejecución de procesos usando algoritmos FCFS y Round-Robin.
- Generar un diagrama de Gantt y calcular métricas (tiempo de respuesta, espera y retorno promedio).
- Guardar y cargar procesos desde archivos JSON y CSV.
- Ejecutar pruebas unitarias para verificar el funcionamiento.

El programa incluye una interfaz CLI (línea de comandos) para interactuar con las funcionalidades.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt` (principalmente `pytest` para las pruebas)

## Instalación

1. Clona el repositorio desde GitHub:
   ```bash
   git clone https://github.com/Serdan1/proyecto-scheduler.git
   cd proyecto-scheduler

2. Instala las dependencias:
pip install -r requirements.txt


## Uso

Ejecuta el programa principal:

python main.py

## Diagrama de flujo: Cargar, listar y planificar procesos

```mermaid
flowchart TD
    A[Inicio: Usuario quiere cargar y planificar procesos] --> B[Seleccionar opción 6: Cargar JSON]
    B --> C[Listar archivos JSON en data/]
    C --> D{¿Hay archivos JSON disponibles?}
    D -- Sí --> E[Mostrar lista de archivos JSON]
    E --> F[Seleccionar un archivo de la lista]
    F --> G{¿Archivo seleccionado válido?}
    G -- Sí --> H[Cargar archivo JSON con RepositorioProcesos]
    H --> I{¿Carga exitosa?}
    I -- Sí --> J[Seleccionar opción 2: Listar procesos]
    J --> K[Obtener procesos de RepositorioProcesos]
    K --> L{¿Hay procesos cargados?}
    L -- Sí --> M[Mostrar lista de procesos]
    M --> N[Seleccionar opción 3: Planificar con FCFS]
    N --> O[Obtener procesos de RepositorioProcesos]
    O --> P[Planificar con FCFSScheduler]
    P --> Q[Generar diagrama de Gantt]
    Q --> R[Calcular métricas con Metricas]
    R --> S[Mostrar Gantt y métricas]
    S --> T[Éxito: Planificación completada]
    D -- No --> U[Error: No hay archivos JSON]
    G -- No --> V[Error: Selección inválida]
    I -- No --> W[Error: Fallo al cargar archivo]
    L -- No --> X[Error: No hay procesos cargados]
    U --> Z[Fin]
    V --> Z[Fin]
    W --> Z[Fin]
    X --> Z[Fin]
    T --> Z[Fin]
