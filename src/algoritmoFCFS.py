from typing import List
from .scheduler import Scheduler, GanttEntry
from .proceso import Proceso

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
    