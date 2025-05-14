from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]  # (pid, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    """Interfaz abstracta para planificadores de CPU."""
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

class FCFSScheduler(Scheduler):
    """Planificador First-Come, First-Served."""
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        tiempo_actual = 0
        for proceso in procesos:
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_fin = tiempo_actual + proceso.duracion
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual = proceso.tiempo_fin
        return gantt

class RoundRobinScheduler(Scheduler):
    """Planificador Round-Robin con quantum configurable."""
    def __init__(self, quantum: int):
        if not isinstance(quantum, int) or quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt = []
        tiempo_actual = 0
        cola = [p for p in procesos]
        for p in cola:
            p.tiempo_restante = p.duracion  # Reiniciar tiempo restante

        while cola:
            proceso = cola.pop(0)
            if proceso.tiempo_inicio is None:
                proceso.tiempo_inicio = tiempo_actual
            tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
            gantt.append((proceso.pid, tiempo_actual, tiempo_actual + tiempo_ejecucion))
            proceso.tiempo_restante -= tiempo_ejecucion
            tiempo_actual += tiempo_ejecucion
            if proceso.tiempo_restante > 0:
                cola.append(proceso)
            else:
                proceso.tiempo_fin = tiempo_actual
        return gantt
    
    