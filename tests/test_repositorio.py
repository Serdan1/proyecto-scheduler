import pytest
import os
from src.repositorio import RepositorioProcesos
from src.proceso import Proceso

@pytest.fixture
def repo():
    return RepositorioProcesos()

def test_agregar_proceso(repo):
    repo.agregar(Proceso("p1", 5, 1))
    assert len(repo.listar()) == 1

def test_pid_duplicado(repo):
    repo.agregar(Proceso("p1", 5, 1))
    with pytest.raises(ValueError):
        repo.agregar(Proceso("p1", 3, 2))

def test_guardar_cargar_json(repo):
    repo.agregar(Proceso("p1", 5, 1))
    repo.guardar_json("test.json")
    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json("test.json")
    assert len(nuevo_repo.listar()) == 1
    os.remove("test.json")

    