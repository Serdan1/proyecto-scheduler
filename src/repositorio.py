import json
import csv
import os
from typing import List, Optional
from .proceso import Proceso

class RepositorioProcesos:
    """Gestiona el conjunto de procesos con persistencia en JSON/CSV."""
    def __init__(self):
        self.procesos: List[Proceso] = []
        self.data_dir = "data"  # Carpeta donde se guardarán los archivos

    def agregar(self, proceso: Proceso) -> None:
        """Agrega un proceso, verifica unicidad de PID."""
        if any(p.pid == proceso.pid for p in self.procesos):
            raise ValueError(f"El PID {proceso.pid} ya existe")
        self.procesos.append(proceso)

    def listar(self) -> List[Proceso]:
        """Devuelve la lista de procesos."""
        print(f"DEBUG: Dentro de RepositorioProcesos.listar(), self.procesos = {self.procesos}", flush=True)
        return self.procesos

    def eliminar(self, pid: str) -> None:
        """Elimina un proceso por su PID."""
        self.procesos = [p for p in self.procesos if p.pid != pid]

    def obtener(self, pid: str) -> Optional[Proceso]:
        """Obtiene un proceso por su PID."""
        for proceso in self.procesos:
            if proceso.pid == pid:
                return proceso
        return None

    def guardar_json(self, nombre_archivo: str) -> None:
        """Guarda los procesos en un archivo JSON en la carpeta data/, incluyendo todos los atributos."""
        # Asegurarse de que la carpeta data/ exista
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(self.data_dir, nombre_archivo)
        if not nombre_archivo.endswith('.json'):
            ruta_archivo += '.json'

        # Serializamos explícitamente todos los atributos
        procesos_dict = [
            {
                "pid": p.pid,
                "duracion": p.duracion,
                "prioridad": p.prioridad,
                "tiempo_llegada": p.tiempo_llegada,
                "tiempo_restante": p.tiempo_restante,
                "tiempo_inicio": p.tiempo_inicio,
                "tiempo_fin": p.tiempo_fin
            }
            for p in self.procesos
        ]
        with open(ruta_archivo, 'w') as f:
            json.dump(procesos_dict, f, indent=2)

    def cargar_json(self, nombre_archivo: str) -> None:
        """Carga procesos desde un archivo JSON en la carpeta data/ y maneja atributos faltantes."""
        # Construir la ruta completa del archivo
        ruta_archivo = os.path.join(self.data_dir, nombre_archivo)
        if not nombre_archivo.endswith('.json'):
            ruta_archivo += '.json'

        print(f"DEBUG: Abriendo el archivo {ruta_archivo}", flush=True)
        print(f"DEBUG: Ruta absoluta del archivo: {os.path.abspath(ruta_archivo)}", flush=True)
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
        with open(ruta_archivo, 'r') as f:
            datos = json.load(f)
            print(f"DEBUG: Datos cargados del JSON: {datos}", flush=True)
            self.procesos = []
            for d in datos:
                # Proporcionamos valores por defecto para atributos faltantes
                proceso = Proceso(
                    pid=d['pid'],
                    duracion=d['duracion'],
                    prioridad=d['prioridad'],
                    tiempo_llegada=d.get('tiempo_llegada', 0),
                    tiempo_restante=d.get('tiempo_restante', d['duracion']),  # Si falta, usar duracion
                    tiempo_inicio=d.get('tiempo_inicio', None),
                    tiempo_fin=d.get('tiempo_fin', None)
                )
                self.procesos.append(proceso)
            print(f"DEBUG: Procesos después de cargar: {self.procesos}", flush=True)

    def listar_archivos_json(self) -> List[str]:
        """Devuelve una lista de archivos JSON en la carpeta data/."""
        print(f"DEBUG: Buscando archivos en la carpeta {self.data_dir}", flush=True)
        print(f"DEBUG: Ruta absoluta de data/: {os.path.abspath(self.data_dir)}", flush=True)
        if not os.path.exists(self.data_dir):
            print(f"DEBUG: La carpeta {self.data_dir} no existe.", flush=True)
            return []
        try:
            archivos = [f for f in os.listdir(self.data_dir) if f.endswith('.json')]
            print(f"DEBUG: Archivos JSON encontrados: {archivos}", flush=True)
            return archivos
        except Exception as e:
            print(f"DEBUG: Error al listar archivos: {e}", flush=True)
            return []

    def guardar_csv(self, archivo: str) -> None:
        """Guarda los procesos en un archivo CSV."""
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad', 'tiempo_llegada'])
            for p in self.procesos:
                writer.writerow([p.pid, p.duracion, p.prioridad, p.tiempo_llegada])

    def cargar_csv(self, archivo: str) -> None:
        """Carga procesos desde un archivo CSV."""
        self.procesos = []
        with open(archivo, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                proceso = Proceso(
                    pid=row['pid'],
                    duracion=int(row['duracion']),
                    prioridad=int(row['prioridad']),
                    tiempo_llegada=int(row['tiempo_llegada'])
                )
                self.procesos.append(proceso)
                