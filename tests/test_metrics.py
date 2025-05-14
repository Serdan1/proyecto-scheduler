import pytest
from src.proceso import Proceso
from src.metrics import Metricas

def test_metricas():
    procesos = [Proceso("p1", 3, 1), Proceso("p2", 2, 2)]
    procesos[0].tiempo_inicio = 0
    procesos[0].     procesos[0].tiempo_fin = 3
    procesos[1].tiempo_inicio = 3
    procesos[1].tiempo_fin = 5
    gantt = [("p1", 0, 3), ("p2", 3, 5)]
    metricas = Metricas.calcular_metricas(procesos, gantt)
    assert metricas['respuesta_promedio'] == 1.5
    assert metricas['espera_promedio'] == 0
    assert metricas['retorno_promedio'] == 4

    