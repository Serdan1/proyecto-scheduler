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

        