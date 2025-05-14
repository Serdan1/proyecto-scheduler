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

        for proceso in procesos:
            tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
            tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
            tiempo_espera = tiempo_retorno - proceso.duracion

            tiempos_respuesta.append(tiempo_respuesta)
            tiempos_espera.append(tiempo_espera)
            tiempos_retorno.append(tiempo_retorno)

        return {
            'respuesta_promedio': sum(tiempos_respuesta) / len(tiempos_respuesta) if tiempos_respuesta else 0,
            'espera_promedio': sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0,
            'retorno_promedio': sum(tiempos_retorno) / len(tiempos_retorno) if tiempos_retorno else 0
        }
    