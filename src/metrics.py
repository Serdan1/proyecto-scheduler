from typing import List, Tuple
from .proceso import Proceso
from .scheduler import GanttEntry

class Metricas:
    """Calcula métricas de planificación basadas en el diagrama de Gantt."""
    @staticmethod
    def calcular_metricas(procesos: List[Proceso], gantt: List[GanttEntry]) -> dict:
        """Calcula tiempos de respuesta, espera y retorno promedio."""
        tiempos_respuesta = []
        tiempos_espera = []
        tiempos_retorno = []

        # Crear un diccionario para mapear PID a proceso
        pid_to_proceso = {p.pid: p for p in procesos}

        # Calcular tiempos de espera usando el diagrama de Gantt
        tiempos_espera_procesos = {p.pid: 0 for p in procesos}
        tiempos_ultima_ejecucion = {p.pid: p.tiempo_llegada for p in procesos}

        for i, (pid, inicio, fin) in enumerate(gantt):
            espera = inicio - tiempos_ultima_ejecucion[pid]
            tiempos_espera_procesos[pid] += espera
            tiempos_ultima_ejecucion[pid] = fin

        for proceso in procesos:
            tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
            tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
            tiempo_espera = tiempos_espera_procesos[proceso.pid]

            tiempos_respuesta.append(tiempo_respuesta)
            tiempos_espera.append(tiempo_espera)
            tiempos_retorno.append(tiempo_retorno)

        return {
            'respuesta_promedio': sum(tiempos_respuesta) / len(tiempos_respuesta) if tiempos_respuesta else 0,
            'espera_promedio': sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0,
            'retorno_promedio': sum(tiempos_retorno) / len(tiempos_retorno) if tiempos_retorno else 0
        }
    