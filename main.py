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
        print(f"DEBUG: Opción ingresada: '{opcion}'", flush=True)

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
            print("DEBUG: Entrando en la opción 2 (Listar procesos)", flush=True)
            procesos = repo.listar()
            print(f"DEBUG: Número de procesos encontrados: {len(procesos)}", flush=True)
            if not procesos:
                print("No hay procesos registrados.", flush=True)
            else:
                for p in procesos:
                    print(f"PID: {p.pid}, Duración: {p.duracion}, Prioridad: {p.prioridad}, "
                          f"Tiempo Llegada: {p.tiempo_llegada}, Tiempo Restante: {p.tiempo_restante}, "
                          f"Tiempo Inicio: {p.tiempo_inicio}, Tiempo Fin: {p.tiempo_fin}", flush=True)

        elif opcion == '3':
            print("DEBUG: Entrando en la opción 3 (Planificar FCFS)", flush=True)
            procesos = repo.listar()
            if not procesos:
                print("No hay procesos para planificar.", flush=True)
            else:
                scheduler = FCFSScheduler()
                gantt = scheduler.planificar(procesos)
                print("Diagrama de Gantt:", gantt)
                metricas = Metricas.calcular_metricas(procesos, gantt)
                print("Métricas:", metricas)

        elif opcion == '4':
            print("DEBUG: Entrando en la opción 4 (Planificar Round-Robin)", flush=True)
            procesos = repo.listar()
            if not procesos:
                print("No hay procesos para planificar.", flush=True)
            else:
                quantum = int(input("Quantum: "))
                scheduler = RoundRobinScheduler(quantum)
                gantt = scheduler.planificar(procesos)
                print("Diagrama de Gantt:", gantt)
                metricas = Metricas.calcular_metricas(procesos, gantt)
                print("Métricas:", metricas)

        elif opcion == '5':
            nombre_archivo = input("Nombre del archivo JSON (sin extensión): ")
            repo.guardar_json(nombre_archivo)
            print(f"Guardado en data/{nombre_archivo}.json")

        elif opcion == '6':
            print("DEBUG: Entrando en la opción 6 (Cargar JSON)", flush=True)
            # Listar archivos JSON disponibles en la carpeta data/
            archivos_json = repo.listar_archivos_json()
            if not archivos_json:
                print("No hay archivos JSON en la carpeta data/.", flush=True)
            else:
                print("Archivos JSON disponibles:")
                for i, archivo in enumerate(archivos_json, 1):
                    print(f"{i}. {archivo}")
                try:
                    seleccion = int(input("Seleccione el número del archivo a cargar: "))
                    if 1 <= seleccion <= len(archivos_json):
                        nombre_archivo = archivos_json[seleccion - 1]
                        print(f"DEBUG: Intentando cargar el archivo {nombre_archivo}", flush=True)
                        repo.cargar_json(nombre_archivo)
                        print(f"Cargado desde data/{nombre_archivo}", flush=True)
                        # Confirmar que los procesos se cargaron
                        procesos_cargados = repo.listar()
                        print(f"DEBUG: Procesos cargados: {len(procesos_cargados)}", flush=True)
                    else:
                        print("Selección inválida.", flush=True)
                except ValueError:
                    print("Error: Por favor ingrese un número válido.", flush=True)
                except Exception as e:
                    print(f"Error al cargar el archivo: {e}", flush=True)

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
    