import json
import os
from typing import List, Optional
from .proceso import Proceso

class RepositorioProcesos:
    """Gestiona el conjunto de procesos con persistencia en JSON."""
    def __init__(self):
        self.procesos: List[Proceso] = []
        # Ruta absoluta a la carpeta data/
        self.data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
        # Asegurarse de que la carpeta data/ exista
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def agregar(self, proceso: Proceso) -> None:
        """Agrega un proceso, verifica unicidad de PID."""
        if any(p.pid == proceso.pid for p in self.procesos):
            raise ValueError(f"El PID {proceso.pid} ya existe")
        self.procesos.append(proceso)
        print(f"DEBUG: Proceso agregado: {proceso.pid}, Total procesos: {len(self.procesos)}", flush=True)

    def listar(self) -> List[Proceso]:
        """Devuelve la lista de procesos."""
        print(f"DEBUG: Listando procesos, Total: {len(self.procesos)}", flush=True)
        return self.procesos

    def eliminar(self, pid: str) -> None:
        """Elimina un proceso por su PID."""
        self.procesos = [p for p in self.procesos if p.pid != pid]
        print(f"DEBUG: Proceso eliminado: {pid}, Total procesos: {len(self.procesos)}", flush=True)

    def obtener(self, pid: str) -> Optional[Proceso]:
        """Obtiene un proceso por su PID."""
        for proceso in self.procesos:
            if proceso.pid == pid:
                return proceso
        return None

    def guardar_json(self, nombre_archivo: str) -> None:
        """Guarda los procesos en un archivo JSON en la carpeta data/."""
        ruta_archivo = os.path.join(self.data_dir, f"{nombre_archivo}.json")
        print(f"DEBUG: Guardando en {ruta_archivo}", flush=True)
        with open(ruta_archivo, 'w') as f:
            json.dump([p.to_dict() for p in self.procesos], f, indent=2)
        print(f"DEBUG: Guardado exitoso en {ruta_archivo}", flush=True)

    def cargar_json(self, nombre_archivo: str) -> None:
        """Carga procesos desde un archivo JSON en la carpeta data/."""
        ruta_archivo = os.path.join(self.data_dir, nombre_archivo)
        if not nombre_archivo.endswith('.json'):
            ruta_archivo += '.json'
        print(f"DEBUG: Intentando cargar desde {ruta_archivo}", flush=True)
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe")
        with open(ruta_archivo, 'r') as f:
            datos = json.load(f)
            print(f"DEBUG: Datos cargados: {datos}", flush=True)
            self.procesos = [Proceso.from_dict(d) for d in datos]
        print(f"DEBUG: Procesos cargados: {len(self.procesos)}", flush=True)

    def listar_archivos_json(self) -> List[str]:
        """Devuelve una lista de archivos JSON en la carpeta data/."""
        print(f"DEBUG: Listando archivos en {self.data_dir}", flush=True)
        archivos = [f for f in os.listdir(self.data_dir) if f.endswith('.json')]
        print(f"DEBUG: Archivos JSON encontrados: {archivos}", flush=True)
        return archivos
    