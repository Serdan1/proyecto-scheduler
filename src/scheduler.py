from abc import ABC, abstractmethod
from typing import List, Tuple
from .proceso import Proceso

GanttEntry = Tuple[str, int, int]  # (pid, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    """Interfaz abstracta para planificadores de CPU."""
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass
    