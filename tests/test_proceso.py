import pytest
from src.proceso import Proceso

def test_proceso_valido():
    p = Proceso("p1", 5, 1)
    assert p.pid == "p1"
    assert p.duracion == 5
    assert p.prioridad == 1
    assert p.tiempo_restante == 5

def test_proceso_pid_invalido():
    with pytest.raises(ValueError):
        Proceso("", 5, 1)

def test_proceso_duracion_invalida():
    with pytest.raises(ValueError):
        Proceso("p1", 0, 1)
        