import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from src.repositorio import RepositorioProcesos
from src.proceso import Proceso
from src.algoritmoFCFS import FCFSScheduler
from src.algoritmoRound_Robin import RoundRobinScheduler
from src.metrics import Metricas

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scheduler App")
        self.root.geometry("1000x600")

        self.repo = RepositorioProcesos()

        # Sección superior: Agregar proceso
        self.frame_agregar = ttk.LabelFrame(root, text="Agregar Proceso", padding=10)
        self.frame_agregar.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Label(self.frame_agregar, text="PID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_pid = ttk.Entry(self.frame_agregar)
        self.entry_pid.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_agregar, text="Duración:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_duracion = ttk.Entry(self.frame_agregar)
        self.entry_duracion.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.frame_agregar, text="Prioridad:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_prioridad = ttk.Entry(self.frame_agregar)
        self.entry_prioridad.grid(row=0, column=5, padx=5, pady=5)

        ttk.Button(self.frame_agregar, text="Agregar", command=self.agregar_proceso).grid(row=0, column=6, padx=10, pady=5)

        # Sección izquierda: Cargar JSON
        self.frame_cargar = ttk.LabelFrame(root, text="Cargar JSON", padding=10)
        self.frame_cargar.grid(row=1, column=0, padx=10, pady=5, sticky="ns")

        self.listbox_archivos = tk.Listbox(self.frame_cargar, width=20, height=15)
        self.listbox_archivos.grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(self.frame_cargar, text="Actualizar lista", command=self.actualizar_lista_json).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.frame_cargar, text="Cargar", command=self.cargar_json).grid(row=2, column=0, padx=5, pady=5)

        # Sección central: Lista de procesos
        self.frame_procesos = ttk.LabelFrame(root, text="Procesos", padding=10)
        self.frame_procesos.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        self.tree = ttk.Treeview(self.frame_procesos, columns=("PID", "Duración", "Prioridad", "Tiempo Llegada", "Tiempo Restante", "Tiempo Inicio", "Tiempo Fin"), show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Duración", text="Duración")
        self.tree.heading("Prioridad", text="Prioridad")
        self.tree.heading("Tiempo Llegada", text="T. Llegada")
        self.tree.heading("Tiempo Restante", text="T. Restante")
        self.tree.heading("Tiempo Inicio", text="T. Inicio")
        self.tree.heading("Tiempo Fin", text="T. Fin")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Sección derecha: Planificación
        self.frame_planificar = ttk.LabelFrame(root, text="Planificar", padding=10)
        self.frame_planificar.grid(row=1, column=2, padx=10, pady=5, sticky="ns")

        ttk.Button(self.frame_planificar, text="Planificar FCFS", command=self.planificar_fcfs).grid(row=0, column=0, padx=5, pady=5)

        ttk.Label(self.frame_planificar, text="Quantum (Round-Robin):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantum = ttk.Entry(self.frame_planificar)
        self.entry_quantum.grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.frame_planificar, text="Planificar Round-Robin", command=self.planificar_round_robin).grid(row=3, column=0, padx=5, pady=5)

        # Sección inferior: Resultados (Gantt y métricas)
        self.frame_resultados = ttk.LabelFrame(root, text="Resultados", padding=10)
        self.frame_resultados.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        self.text_resultados = scrolledtext.ScrolledText(self.frame_resultados, width=100, height=10)
        self.text_resultados.grid(row=0, column=0, padx=5, pady=5)

        # Sección inferior: Guardar en JSON
        self.frame_guardar = ttk.LabelFrame(root, text="Guardar en JSON", padding=10)
        self.frame_guardar.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        ttk.Label(self.frame_guardar, text="Nombre del archivo (sin extensión):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_guardar = ttk.Entry(self.frame_guardar)
        self.entry_guardar.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.frame_guardar, text="Guardar", command=self.guardar_json).grid(row=0, column=2, padx=5, pady=5)

        # Configurar pesos para que la interfaz sea redimensionable
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)

        # Actualizar la lista de archivos JSON al inicio
        self.actualizar_lista_json()

    def agregar_proceso(self):
        try:
            pid = self.entry_pid.get()
            duracion = int(self.entry_duracion.get())
            prioridad = int(self.entry_prioridad.get())
            proceso = Proceso(pid, duracion, prioridad)
            self.repo.agregar(proceso)
            self.actualizar_lista_procesos()
            messagebox.showinfo("Éxito", "Proceso agregado correctamente.")
            # Limpiar campos
            self.entry_pid.delete(0, tk.END)
            self.entry_duracion.delete(0, tk.END)
            self.entry_prioridad.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_lista_json(self):
        self.listbox_archivos.delete(0, tk.END)
        archivos = self.repo.listar_archivos_json()
        for archivo in archivos:
            self.listbox_archivos.insert(tk.END, archivo)

    def cargar_json(self):
        seleccion = self.listbox_archivos.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor seleccione un archivo JSON.")
            return
        nombre_archivo = self.listbox_archivos.get(seleccion[0])
        try:
            self.repo.cargar_json(nombre_archivo)
            self.actualizar_lista_procesos()
            messagebox.showinfo("Éxito", f"Datos cargados desde data/{nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

    def actualizar_lista_procesos(self):
        # Limpiar la tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Mostrar procesos
        for p in self.repo.listar():
            self.tree.insert("", tk.END, values=(
                p.pid,
                p.duracion,
                p.prioridad,
                p.tiempo_llegada,
                p.tiempo_restante,
                p.tiempo_inicio,
                p.tiempo_fin
            ))

    def planificar_fcfs(self):
        procesos = self.repo.listar()
        if not procesos:
            messagebox.showerror("Error", "No hay procesos para planificar.")
            return
        scheduler = FCFSScheduler()
        gantt = scheduler.planificar(procesos)
        metricas = Metricas.calcular_metricas(procesos, gantt)
        self.mostrar_resultados(gantt, metricas)
        self.actualizar_lista_procesos()

    def planificar_round_robin(self):
        procesos = self.repo.listar()
        if not procesos:
            messagebox.showerror("Error", "No hay procesos para planificar.")
            return
        try:
            quantum = int(self.entry_quantum.get())
            scheduler = RoundRobinScheduler(quantum)
            gantt = scheduler.planificar(procesos)
            metricas = Metricas.calcular_metricas(procesos, gantt)
            self.mostrar_resultados(gantt, metricas)
            self.actualizar_lista_procesos()
        except ValueError as e:
            messagebox.showerror("Error", f"Error en el quantum: {e}")

    def mostrar_resultados(self, gantt, metricas):
        self.text_resultados.delete(1.0, tk.END)
        self.text_resultados.insert(tk.END, "Diagrama de Gantt:\n")
        self.text_resultados.insert(tk.END, str(gantt) + "\n\n")
        self.text_resultados.insert(tk.END, "Métricas:\n")
        self.text_resultados.insert(tk.END, f"Tiempo de respuesta promedio: {metricas['respuesta_promedio']}\n")
        self.text_resultados.insert(tk.END, f"Tiempo de espera promedio: {metricas['espera_promedio']}\n")
        self.text_resultados.insert(tk.END, f"Tiempo de retorno promedio: {metricas['retorno_promedio']}\n")

    def guardar_json(self):
        nombre_archivo = self.entry_guardar.get()
        if not nombre_archivo:
            messagebox.showerror("Error", "Por favor ingrese un nombre para el archivo.")
            return
        try:
            self.repo.guardar_json(nombre_archivo)
            self.actualizar_lista_json()
            messagebox.showinfo("Éxito", f"Guardado en data/{nombre_archivo}.json")
            self.entry_guardar.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {e}")
            