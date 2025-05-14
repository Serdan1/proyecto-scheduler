import json
import csv
from typing import List, Optional
from .proceso import Proceso

class RepositorioProcesos:
    """Gestiona el conjunto de procesos con persistencia en JSON/CSV."""
    def __init__(self):
        self.procesos: List[Proceso] = []

    def agregar(self, proceso: Proceso) -> None:
        """Agrega un proceso, verifica unicidad de PID."""
        if any(p.pid == proceso.pid for p in self.procesos):
            raise ValueError(f"El PID {proceso.pid} ya existe")
        self.procesos.append(proceso)

    def listar(self) -> List[Proceso]:
        """Devuelve la lista de procesos."""
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

    def guardar_json(self, archivo: str) -> None:
        """Guarda los procesos en un archivo JSON, incluyendo todos los atributos."""
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
        with open(archivo, 'w') as f:
            json.dump(procesos_dict, f, indent=2)

    def cargar_json(self, archivo: str) -> None:
        """Carga procesos desde un archivo JSON y maneja atributos faltantes."""
        with open(archivo, 'r') as f:
            datos = json.load(f)
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
                