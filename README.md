# Proyecto Scheduler

Este proyecto implementa un simulador de planificación de procesos para un sistema operativo, desarrollado en Python utilizando programación orientada a objetos. El programa permite gestionar procesos, planificar su ejecución con algoritmos como FCFS (First-Come, First-Served) y Round-Robin, calcular métricas de rendimiento, y persistir los datos en archivos JSON. Originalmente diseñado con una interfaz de línea de comandos (CLI), ahora incluye una interfaz gráfica (GUI) desarrollada con Tkinter para una interacción más visual e intuitiva. También cuenta con pruebas unitarias y una estructura profesional del proyecto.

## Descripción

El proyecto modela un entorno simplificado de un sistema operativo donde se pueden:
- Registrar y gestionar procesos con atributos como PID, duración, prioridad, tiempo de llegada, tiempo restante, tiempo de inicio y tiempo de fin.
- Planificar la ejecución de procesos usando algoritmos FCFS y Round-Robin.
- Generar un diagrama de Gantt y calcular métricas (tiempo de respuesta, espera y retorno promedio).
- Guardar y cargar procesos desde archivos JSON almacenados en la carpeta `data/`.
- Analizar datos cargados desde archivos JSON mediante una interfaz gráfica.

El programa utiliza una interfaz gráfica (GUI) desarrollada con Tkinter, permitiendo una interacción más amigable con las mismas funcionalidades.

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`:
  - `pytest>=7.0.0` (para ejecutar pruebas unitarias)
- Tkinter (incluido con Python por defecto)

## Instalación

1. Clona el repositorio desde GitHub:
   ```bash
   git clone https://github.com/Serdan1/proyecto-scheduler.git
   cd proyecto-scheduler

## Uso

Ejecución del programa
Asegúrate de que el entorno virtual esté activado (si lo creaste).

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
