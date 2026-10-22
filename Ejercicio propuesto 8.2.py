import tkinter as tk
from tkinter import messagebox
import statistics

class CalculadoraNotasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas Estudiantiles")
        self.root.geometry("400x520")
        self.root.config(padx=20, pady=20)
        
        # Título principal
        tk.Label(
            root, 
            text="Ingreso de Notas (5 calificaciones)", 
            font=("Arial", 12, "bold")
        ).pack(pady=10)
        
        # Contenedor para las entradas de las 5 notas
        self.entries = []
        for i in range(5):
            frame = tk.Frame(root)
            frame.pack(fill="x", pady=5)
            
            tk.Label(frame, text=f"Nota {i+1}:", width=10, anchor="w", font=("Arial", 10)).pack(side="left")
            
            entry = tk.Entry(frame, width=15, font=("Arial", 10))
            entry.pack(side="right", expand=True, fill="x")
            self.entries.append(entry)
        
        # Contenedor para los botones (Calcular y Limpiar)
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)
        
        btn_calcular = tk.Button(
            btn_frame, 
            text="Calcular Estadísticas", 
            bg="#2196F3", 
            fg="white", 
            font=("Arial", 10, "bold"), 
            command=self.calcular_estadisticas
        )
        btn_calcular.pack(side="left", padx=5)
        
        btn_limpiar = tk.Button(
            btn_frame, 
            text="Limpiar", 
            bg="#f44336", 
            fg="white", 
            font=("Arial", 10, "bold"), 
            command=self.limpiar_campos
        )
        btn_limpiar.pack(side="left", padx=5)
        
        # Sección de resultados en la parte inferior
        tk.Label(root, text="Resultados:", font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 5))
        
        self.lbl_promedio = tk.Label(root, text="• Promedio: -", font=("Arial", 10))
        self.lbl_promedio.pack(anchor="w", pady=2)
        
        self.lbl_desviacion = tk.Label(root, text="• Desviación estándar: -", font=("Arial", 10))
        self.lbl_desviacion.pack(anchor="w", pady=2)
        
        self.lbl_mayor = tk.Label(root, text="• Mayor nota: -", font=("Arial", 10))
        self.lbl_mayor.pack(anchor="w", pady=2)
        
        self.lbl_menor = tk.Label(root, text="• Menor nota: -", font=("Arial", 10))
        self.lbl_menor.pack(anchor="w", pady=2)

    def validar_y_obtener_notas(self):
        """Valida las entradas y retorna una lista de floats o None si falla una validación."""
        notas = []
        for i, entry in enumerate(self.entries, start=1):
            texto = entry.get().strip()
            
            # Alerta cuando una nota no ha sido ingresada
            if not texto:
                messagebox.showwarning(
                    "Campo Incompleto", 
                    f"Es obligatorio ingresar las cinco notas.\nFalta la Nota {i}."
                )
                return None
            
            # Alerta cuando se ingresa un valor no numérico
            try:
                valor = float(texto)
                notas.append(valor)
            except ValueError:
                messagebox.showerror(
                    "Dato No Numérico", 
                    f"El valor ingresado en la Nota {i} ('{texto}') no es numérico."
                )
                return None
                
        return notas

    def calcular_estadisticas(self):
        notas = self.validar_y_obtener_notas()
        if notas is None:
            return  # Se interrumpe la ejecución si falla alguna validación
        
        # Cálculos estadísticos
        promedio = statistics.mean(notas)
        desviacion = statistics.stdev(notas) if len(notas) > 1 else 0.0
        mayor = max(notas)
        menor = min(notas)
        
        # Actualización de la interfaz
        self.lbl_promedio.config(text=f"• Promedio: {promedio:.2f}")
        self.lbl_desviacion.config(text=f"• Desviación estándar: {desviacion:.2f}")
        self.lbl_mayor.config(text=f"• Mayor nota: {mayor:.2f}")
        self.lbl_menor.config(text=f"• Menor nota: {menor:.2f}")

    def limpiar_campos(self):
        """Limpia todas las cajas de texto y restablece las etiquetas de resultados."""
        for entry in self.entries:
            entry.delete(0, tk.END)
        
        self.lbl_promedio.config(text="• Promedio: -")
        self.lbl_desviacion.config(text="• Desviación estándar: -")
        self.lbl_mayor.config(text="• Mayor nota: -")
        self.lbl_menor.config(text="• Menor nota: -")
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraNotasApp(root)
    root.mainloop()