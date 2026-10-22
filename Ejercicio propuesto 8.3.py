import tkinter as tk
from tkinter import messagebox
import math


# 1. CLASE BASE: FiguraGeometrica
class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    @property
    def volumen(self) -> float:
        return self._volumen

    @volumen.setter
    def volumen(self, valor: float):
        self._volumen = valor

    @property
    def superficie(self) -> float:
        return self._superficie

    @superficie.setter
    def superficie(self, valor: float):
        self._superficie = valor


# 2. CLASES DE FIGURAS GEOMÉTRICAS (JERARQUÍA)
class Cilindro(FiguraGeometrica):
    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return math.pi * self.altura * (self.radio ** 2)

    def calcular_superficie(self) -> float:
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * (self.radio ** 2)
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self) -> float:
        return 4.0 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return ((self.base ** 2) * self.altura) / 3.0

    def calcular_superficie(self) -> float:
        area_base = self.base ** 2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado


class Cubo(FiguraGeometrica):
    def __init__(self, lado: float):
        super().__init__()
        self.lado = lado
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return self.lado ** 3

    def calcular_superficie(self) -> float:
        return 6.0 * (self.lado ** 2)


class Prisma(FiguraGeometrica):
    def __init__(self, base: float, ancho: float, altura: float):
        super().__init__()
        self.base = base
        self.ancho = ancho
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self) -> float:
        return self.base * self.ancho * self.altura

    def calcular_superficie(self) -> float:
        return 2.0 * (self.base * self.ancho + self.base * self.altura + self.ancho * self.altura)



# DIBUJO ILUSTRATIVO EN CANVAS DE TKINTER

def dibujar_figura(canvas, tipo):
    canvas.delete("all")
    if tipo == "cilindro":
        canvas.create_oval(30, 15, 110, 45, outline="#1F4E78", width=2, fill="#EAECEE")
        canvas.create_line(30, 30, 30, 110, fill="#1F4E78", width=2)
        canvas.create_line(110, 30, 110, 110, fill="#1F4E78", width=2)
        canvas.create_oval(30, 95, 110, 125, outline="#1F4E78", width=2, fill="#EAECEE")
    elif tipo == "esfera":
        canvas.create_oval(20, 20, 120, 120, outline="#1F4E78", width=2, fill="#EAECEE")
        canvas.create_oval(20, 55, 120, 85, outline="#595959", width=1, dash=(4, 4))
    elif tipo == "piramide":
        canvas.create_polygon(70, 15, 20, 110, 120, 110, outline="#1F4E78", fill="#EAECEE", width=2)
        canvas.create_line(70, 15, 60, 125, fill="#1F4E78", width=2)
        canvas.create_line(20, 110, 60, 125, fill="#1F4E78", width=2)
        canvas.create_line(120, 110, 60, 125, fill="#1F4E78", width=2)
    elif tipo == "cubo":
        canvas.create_rectangle(25, 45, 95, 115, outline="#1F4E78", width=2, fill="#EAECEE")
        canvas.create_rectangle(45, 25, 115, 95, outline="#1F4E78", width=2)
        canvas.create_line(25, 45, 45, 25, fill="#1F4E78", width=2)
        canvas.create_line(95, 45, 115, 25, fill="#1F4E78", width=2)
        canvas.create_line(25, 115, 45, 95, fill="#1F4E78", width=2)
        canvas.create_line(95, 115, 115, 95, fill="#1F4E78", width=2)
    elif tipo == "prisma":
        canvas.create_rectangle(15, 55, 95, 115, outline="#1F4E78", width=2, fill="#EAECEE")
        canvas.create_rectangle(35, 25, 115, 85, outline="#1F4E78", width=2)
        canvas.create_line(15, 55, 35, 25, fill="#1F4E78", width=2)
        canvas.create_line(95, 55, 115, 25, fill="#1F4E78", width=2)
        canvas.create_line(15, 115, 35, 85, fill="#1F4E78", width=2)
        canvas.create_line(95, 115, 115, 85, fill="#1F4E78", width=2)


# 3. VENTANAS INDIVIDUALES

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("420x230")
        self.resizable(False, False)

        cvs = tk.Canvas(self, width=140, height=140, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        cvs.place(x=15, y=15)
        dibujar_figura(cvs, "cilindro")

        tk.Label(self, text="Radio (cm):").place(x=170, y=20, width=100, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=275, y=20, width=120, height=23)

        tk.Label(self, text="Altura (cm):").place(x=170, y=50, width=100, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=275, y=50, width=120, height=23)

        self.btn_calcular = tk.Button(self, text="Calcular", bg="#1F4E78", fg="white", font=("Arial", 9, "bold"), command=self.calcular)
        self.btn_calcular.place(x=275, y=85, width=120, height=26)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_volumen.place(x=170, y=125, width=230, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_superficie.place(x=170, y=155, width=230, height=23)

    def calcular(self):
        try:
            r = float(self.campo_radio.get())
            h = float(self.campo_altura.get())
            obj = Cilindro(r, h)
            self.lbl_volumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato numérico", parent=self)


class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("420x210")
        self.resizable(False, False)

        cvs = tk.Canvas(self, width=140, height=140, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        cvs.place(x=15, y=15)
        dibujar_figura(cvs, "esfera")

        tk.Label(self, text="Radio (cm):").place(x=170, y=20, width=100, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=275, y=20, width=120, height=23)

        self.btn_calcular = tk.Button(self, text="Calcular", bg="#1F4E78", fg="white", font=("Arial", 9, "bold"), command=self.calcular)
        self.btn_calcular.place(x=275, y=55, width=120, height=26)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_volumen.place(x=170, y=100, width=230, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_superficie.place(x=170, y=130, width=230, height=23)

    def calcular(self):
        try:
            r = float(self.campo_radio.get())
            obj = Esfera(r)
            self.lbl_volumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato numérico", parent=self)


class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("420x250")
        self.resizable(False, False)

        cvs = tk.Canvas(self, width=140, height=140, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        cvs.place(x=15, y=15)
        dibujar_figura(cvs, "piramide")

        tk.Label(self, text="Base (cm):").place(x=170, y=20, width=100, height=23)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=275, y=20, width=120, height=23)

        tk.Label(self, text="Altura (cm):").place(x=170, y=50, width=100, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=275, y=50, width=120, height=23)

        tk.Label(self, text="Apotema (cm):").place(x=170, y=80, width=100, height=23)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=275, y=80, width=120, height=23)

        self.btn_calcular = tk.Button(self, text="Calcular", bg="#1F4E78", fg="white", font=("Arial", 9, "bold"), command=self.calcular)
        self.btn_calcular.place(x=275, y=115, width=120, height=26)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_volumen.place(x=170, y=155, width=230, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_superficie.place(x=170, y=185, width=230, height=23)

    def calcular(self):
        try:
            b = float(self.campo_base.get())
            h = float(self.campo_altura.get())
            a = float(self.campo_apotema.get())
            obj = Piramide(b, h, a)
            self.lbl_volumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato numérico", parent=self)


class VentanaCubo(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cubo")
        self.geometry("420x210")
        self.resizable(False, False)

        cvs = tk.Canvas(self, width=140, height=140, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        cvs.place(x=15, y=15)
        dibujar_figura(cvs, "cubo")

        tk.Label(self, text="Lado (cm):").place(x=170, y=20, width=100, height=23)
        self.campo_lado = tk.Entry(self)
        self.campo_lado.place(x=275, y=20, width=120, height=23)

        self.btn_calcular = tk.Button(self, text="Calcular", bg="#1F4E78", fg="white", font=("Arial", 9, "bold"), command=self.calcular)
        self.btn_calcular.place(x=275, y=55, width=120, height=26)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_volumen.place(x=170, y=100, width=230, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_superficie.place(x=170, y=130, width=230, height=23)

    def calcular(self):
        try:
            l = float(self.campo_lado.get())
            obj = Cubo(l)
            self.lbl_volumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato numérico", parent=self)


class VentanaPrisma(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Prisma Rectangular")
        self.geometry("420x250")
        self.resizable(False, False)

        cvs = tk.Canvas(self, width=140, height=140, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        cvs.place(x=15, y=15)
        dibujar_figura(cvs, "prisma")

        tk.Label(self, text="Base (cm):").place(x=170, y=20, width=100, height=23)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=275, y=20, width=120, height=23)

        tk.Label(self, text="Ancho (cm):").place(x=170, y=50, width=100, height=23)
        self.campo_ancho = tk.Entry(self)
        self.campo_ancho.place(x=275, y=50, width=120, height=23)

        tk.Label(self, text="Altura (cm):").place(x=170, y=80, width=100, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=275, y=80, width=120, height=23)

        self.btn_calcular = tk.Button(self, text="Calcular", bg="#1F4E78", fg="white", font=("Arial", 9, "bold"), command=self.calcular)
        self.btn_calcular.place(x=275, y=115, width=120, height=26)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_volumen.place(x=170, y=155, width=230, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): -", anchor="w", font=("Arial", 9, "bold"))
        self.lbl_superficie.place(x=170, y=185, width=230, height=23)

    def calcular(self):
        try:
            b = float(self.campo_base.get())
            a = float(self.campo_ancho.get())
            h = float(self.campo_altura.get())
            obj = Prisma(b, a, h)
            self.lbl_volumen.config(text=f"Volumen (cm3): {obj.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {obj.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato numérico", parent=self)

# 4. VENTANA PRINCIPAL

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Figuras Geométricas")
        self.geometry("520x150")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        tk.Label(self, text="Seleccione una figura geométrica:", font=("Arial", 11, "bold")).pack(pady=15)

        frame_btns = tk.Frame(self)
        frame_btns.pack(pady=5)

        tk.Button(frame_btns, text="Cilindro", width=10, command=lambda: VentanaCilindro(self)).pack(side="left", padx=5)
        tk.Button(frame_btns, text="Esfera", width=10, command=lambda: VentanaEsfera(self)).pack(side="left", padx=5)
        tk.Button(frame_btns, text="Pirámide", width=10, command=lambda: VentanaPiramide(self)).pack(side="left", padx=5)
        tk.Button(frame_btns, text="Cubo", width=10, command=lambda: VentanaCubo(self)).pack(side="left", padx=5)
        tk.Button(frame_btns, text="Prisma", width=10, command=lambda: VentanaPrisma(self)).pack(side="left", padx=5)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()