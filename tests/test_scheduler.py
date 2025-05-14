import pytest
from src.proceso import Proceso
from src.algoritmoFCFS import FCFSScheduler
from src.algoritmoRound_Robin import RoundRobinScheduler  # Cambiado de algoritmoRound-Robin a algoritmoRound_Robin

def test_fcfs_scheduler():
    procesos = [Proceso("p1", 3, 1), Proceso("p2", 2, 2)]
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(procesos)
    assert gantt == [("p1", 0, 3), ("p2", 3, 5)]

def test_round_robin_scheduler():
    procesos = [Proceso("p1", 4, 1), Proceso("p2", 3, 2)]
    scheduler = RoundRobinScheduler(quantum=2)
    gantt = scheduler.planificar(procesos)
    assert gantt == [("p1", 0, 2), ("p2", 2, 4), ("p1", 4, 6), ("p2", 6, 7)]
    