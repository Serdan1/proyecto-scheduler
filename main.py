import tkinter as tk
from src.gui import SchedulerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()
    