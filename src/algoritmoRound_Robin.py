from typing import List
from .scheduler import Scheduler, GanttEntry
from .proceso import Proceso

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
    