from src.repositorio import RepositorioProcesos
from src.proceso import Proceso
from src.algoritmoFCFS import FCFSScheduler
from src.algoritmoRound_Robin import RoundRobinScheduler
from src.metrics import Metricas

def main():
    """Interfaz CLI para gestionar procesos y planificar."""
    repo = RepositorioProcesos()
    while True:
        print("\n1. Agregar proceso")
        print("2. Listar procesos")
        print("3. Planificar (FCFS)")
        print("4. Planificar (Round-Robin)")
        print("5. Guardar (JSON)")
        print("6. Cargar (JSON)")
        print("7. Guardar (CSV)")
        print("8. Cargar (CSV)")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            pid = input("PID: ")
            duracion = int(input("Duración: "))
            prioridad = int(input("Prioridad: "))
            try:
                repo.agregar(Proceso(pid, duracion, prioridad))
                print("Proceso agregado.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            print("DEBUG: Entrando en la opción 2 (Listar procesos)")  # Mensaje de depuración
            procesos = repo.listar()
            print(f"DEBUG: Número de procesos encontrados: {len(procesos)}")  # Ver cuántos procesos hay
            if not procesos:
                print("No hay procesos registrados.")
            else:
                for p in procesos:
                    print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}, "
                        f"Tiempo Llegada: {p.tiempo_llegada}, Tiempo Restante: {p.tiempo_restante}, "
                        f"Tiempo Inicio: {p.tiempo_inicio}, Tiempo Fin: {p.tiempo_fin}")

        elif opcion == '3':
            scheduler = FCFSScheduler()
            gantt = scheduler.planificar(repo.listar())
            print("Diagrama de Gantt:", gantt)
            metricas = Metricas.calcular_metricas(repo.listar(), gantt)
            print("Métricas:", metricas)

        elif opcion == '4':
            quantum = int(input("Quantum: "))
            scheduler = RoundRobinScheduler(quantum)
            gantt = scheduler.planificar(repo.listar())
            print("Diagrama de Gantt:", gantt)
            metricas = Metricas.calcular_metricas(repo.listar(), gantt)
            print("Métricas:", metricas)

        elif opcion == '5':
            archivo = input("Nombre del archivo JSON: ")
            repo.guardar_json(archivo)
            print("Guardado en JSON.")

        elif opcion == '6':
            archivo = input("Nombre del archivo JSON: ")
            repo.cargar_json(archivo)
            print("Cargado desde JSON.")

        elif opcion == '7':
            archivo = input("Nombre del archivo CSV: ")
            repo.guardar_csv(archivo)
            print("Guardado en CSV.")

        elif opcion == '8':
            archivo = input("Nombre del archivo CSV: ")
            repo.cargar_csv(archivo)
            print("Cargado desde CSV.")

        elif opcion == '9':
            break

if __name__ == "__main__":
    main()

