from dataclasses import dataclass
from typing import Optional

@dataclass
class Proceso:
    """Representa un proceso del sistema con atributos y validaciones."""
    pid: str
    duracion: int
    prioridad: int
    tiempo_llegada: int = 0
    tiempo_restante: Optional[int] = None
    tiempo_inicio: Optional[int] = None
    tiempo_fin: Optional[int] = None

    def __post_init__(self):
        """Valida los atributos al crear el proceso."""
        if not self.pid or not isinstance(self.pid, str):
            raise ValueError("El PID debe ser un string no vacío")
        if not isinstance(self.duracion, int) or self.duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo")
        if not isinstance(self.prioridad, int):
            raise ValueError("La prioridad debe ser un entero")
        self.tiempo_restante = self.duracion if self.tiempo_restante is None else self.tiempo_restante

    def to_dict(self):
        """Convierte el proceso a un diccionario para serialización."""
        return {
            "pid": self.pid,
            "duracion": self.duracion,
            "prioridad": self.prioridad,
            "tiempo_llegada": self.tiempo_llegada,
            "tiempo_restante": self.tiempo_restante,
            "tiempo_inicio": self.tiempo_inicio,
            "tiempo_fin": self.tiempo_fin
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Crea un proceso a partir de un diccionario (deserialización)."""
        return cls(
            pid=data['pid'],
            duracion=data['duracion'],
            prioridad=data['prioridad'],
            tiempo_llegada=data.get('tiempo_llegada', 0),
            tiempo_restante=data.get('tiempo_restante', data['duracion']),
            tiempo_inicio=data.get('tiempo_inicio', None),
            tiempo_fin=data.get('tiempo_fin', None)
        )
    