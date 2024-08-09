#Primera ventana 
""""
import tkinter as tk

ventana_principal = tk.Tk() #Crear la ventana
ventana_principal.mainloop() #Refrescar a ventana 

"""

""""
import tkinter as tk 

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola Mundo gráfico")
etiqueta.pack() # Ajusta el tamaño
ventana.mainloop()

"""
""""
import tkinter as tk 
ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola soy Andrés Cadena")
etiqueta2= tk.Label(ventana, text="afcadena022@gmail.com")
etiqueta3 = tk.Label(ventana , text="3022964106")
etiqueta.pack()
etiqueta2.pack()
etiqueta3.pack()
ventana.mainloop()

"""

#propiedades de la ventana 
#Title: titulo de la ventana
#geometry: tamaño y ubicacion de la ventana
#resizable: si la ventana se puede redimensionar
#icon: icono de la ventana
#background: color de fondo de la ventana

""""
import tkinter as tk

ventana = tk.Tk()
etiqueta = tk.Label (ventana, text="Hola mundo ")
etiqueta.pack()
ventana.title("Aplicacion GUI con Tkinter")
ventana.geometry("800x600+150+50")#Primero el ancho y después el alto y la posición de la ventana al final 
ventana.resizable(False, True)#Adaptar el contenedor al texto 
ventana.attributes("-alpha", 0.9)#Transparencia
ventana.mainloop()

"""
#Messagebox: cuadros de mensajes
#showinfo() muestra info
#showerror()muestra error
#showwarning()muestra advertencia
""""
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning

ventana = tk.Tk()
ventana.title("showinfo")
showinfo(title="Mensaje", message="Bienvenido")
showerror(title="Error", message="Se detectó virus en su equipo ")
showwarning(title="Advertencia", message="Puedo estar equivocado\nValidecon soporte técnico")
ventana.mainloop()
"""

#askyesno()
"""
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.title("Yes/No")

respuesta = askyesno(title="Pregunta" , message="¿Quieres salir de este programa?")

if respuesta:
    ventana.destroy()
else:
    showinfo(title="Mensaje", message="No se cerrará el programa")
ventana.mainloop()
"""
""""
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.title("Cuestionario")

preguntas = [
    "¿La caja negra de un avión es negra?",
    "¿El sol es una estrella?",
    "¿La Tierra es plana?",
    "¿El agua hierve a 100 grados Celsius?",
    "¿El ser humano puede vivir sin oxígeno?"
]

respuestas_correctas = [False, True, False, True, False]  # Respuestas correctas
puntuacion = 0

for i, pregunta in enumerate(preguntas):
    respuesta = askyesno(title="Pregunta", message=pregunta)
    if respuesta == respuestas_correctas[i]:
        puntuacion += 1

showinfo(title="Resultados", message=f"¡Has obtenido {puntuacion} puntos de 5!")

ventana.mainloop()
"""

#Cambiar colores por parte del usuario
""""
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showinfo


ventana = tk.Tk()
ventana.title("Cambiar Color")

color = askcolor()
ventana["bg"] = color[1]
showinfo(message = f"El color seleccionado fue: {color[0]}")

ventana.mainloop()

"""
#Incluir botón y muestra mensaje por medio de la terminal
"""
import tkinter as tk
from tkinter import ttk

def saludar():
    print("Hola, Gracias por hacer click")

ventana = tk.Tk()
mi_boton = ttk.Button(ventana, text="Click aquí", command=saludar)
mi_boton.pack()
ventana.mainloop()
"""

#Función que crea una caja de texto 
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
    showinfo(message=nombre.get())


ventana = tk.Tk()
nombre = tk.StringVar()

ttk.Entry(ventana, textvariable=nombre).pack()
ttk.Button(ventana, text="aceptar", command=funcion_a_ejecutar).pack()

ventana.mainloop()
"""

#Funcion que reune todo lo visto anteriormente en otras palabras login funcional 
"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# ventana principal
ventana = tk.Tk()
ventana.geometry("300x200+400+200")
ventana.resizable(False, False)
ventana.title('Autenticación de usuario')

# variables para guardar el usuario, el password y la opción de guardar password
usuario = tk.StringVar()
password = tk.StringVar()
check = tk.StringVar()

# función que se ejecuta al dar click en el botón login
def login_click():
    mensaje = f"usuario: {usuario.get()}, password: {password.get()}.\nGuardar password: {check.get()}"
    showinfo(title='Atención', message=mensaje)

# Creando un Frame
fra_login = ttk.Frame(ventana)
fra_login.pack(padx=10, pady=10, fill='x', expand=True)

# usuario
lbl_usuario = ttk.Label(fra_login, text="usuario:")
lbl_usuario.pack(fill='x', expand=True)

txt_usuario = ttk.Entry(fra_login, textvariable=usuario)
txt_usuario.pack(fill='x', expand=True)
txt_usuario.focus()

# password
lbl_password = ttk.Label(fra_login, text="Password:")
lbl_password.pack(fill='x', expand=True)

txt_password = ttk.Entry(fra_login, textvariable=password, show="*")
txt_password.pack(fill='x', expand=True)

# checkbutton
check_guardar = ttk.Checkbutton(fra_login,
                text='guardar password',
                variable=check,
                onvalue='True',
                offvalue='False')
check_guardar.pack(fill='x', expand=True)

# button
btn_login = ttk.Button(fra_login, text="Login", command=login_click)
btn_login.pack(fill='x', expand=True, pady=10)

ventana.mainloop()

"""
#Agregar valores a un diccionario
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_a_ejecutar():
   etiqueta["text"] = nombre.get() + " " + apellido.get()

ventana = tk.Tk()
nombre = tk.StringVar()
apellido = tk.StringVar()

ttk.Entry(ventana, textvariable=nombre).pack(fill='x', expand=True)
ttk.Entry(ventana, textvariable=apellido).pack(fill='x', expand=True)
etiqueta = ttk.Label(ventana)
etiqueta.pack(fill='x', expand=True)
ttk.Button(ventana, text="aceptar", command=funcion_a_ejecutar).pack(fill='x', expand=True)

ventana.mainloop()
"""
#Mostrar botón presionado 

"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def funcion_controladora(param):
    showinfo(message = param)

ventana = tk.Tk()
ttk.Button(ventana, text="1", command= lambda : funcion_controladora("1")).pack()
ttk.Button(ventana, text="0", command= lambda : funcion_controladora("0")).pack()

ventana.mainloop()
"""
#Organizar widgets en filas y columnas
"""
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ttk.Button(ventana, text="1").grid(column=0, row=0)
ttk.Button(ventana, text="2").grid(column=1, row=0)
ttk.Button(ventana, text="3").grid(column=0, row=1)
ttk.Button(ventana, text="4").grid(column=1, row=1)
ttk.Button(ventana, text="5").grid(column=0, row=2)
ttk.Button(ventana, text="6").grid(column=1, row=2)
ventana.mainloop()
"""
#EJERCICIO CALCULADORA
"""
import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Básica")

        # Creamos los campos de texto para la entrada de números
        self.numero1 = tk.Entry(self.ventana, width=10)
        self.numero1.grid(row=0, column=0)

        self.numero2 = tk.Entry(self.ventana, width=10)
        self.numero2.grid(row=1, column=0)

        # Creamos los botones para las operaciones
        self.suma = tk.Button(self.ventana, text="+", command=self.sumar)
        self.suma.grid(row=0, column=1)

        self.resta = tk.Button(self.ventana, text="-", command=self.restar)
        self.resta.grid(row=1, column=1)

        self.multiplicacion = tk.Button(self.ventana, text="*", command=self.multiplicar)
        self.multiplicacion.grid(row=0, column=2)

        self.division = tk.Button(self.ventana, text="/", command=self.dividir)
        self.division.grid(row=1, column=2)

        # Creamos el campo de texto para el resultado
        self.resultado = tk.Label(self.ventana, text="")
        self.resultado.grid(row=2, column=0, columnspan=3)

    def sumar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 + num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def restar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 - num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 * num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def dividir(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            if num2 != 0:
                resultado = num1 / num2
                self.resultado.config(text=f"Resultado: {resultado}")
            else:
                self.resultado.config(text="Error: No se puede dividir por cero")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()
"""

#OTRO EJEMPLO DE CALCULADORA PERO AVANZADA
"""
import tkinter as tk
import math

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Avanzada")

        # Creamos los campos de texto para la entrada de números
        self.numero1 = tk.Entry(self.ventana, width=15)
        self.numero1.grid(row=0, column=0)

        self.numero2 = tk.Entry(self.ventana, width=15)
        self.numero2.grid(row=1, column=0)

        # Creamos los botones para las operaciones
        self.suma = tk.Button(self.ventana, text="+", command=self.sumar)
        self.suma.grid(row=0, column=1)

        self.resta = tk.Button(self.ventana, text="-", command=self.restar)
        self.resta.grid(row=1, column=1)

        self.multiplicacion = tk.Button(self.ventana, text="*", command=self.multiplicar)
        self.multiplicacion.grid(row=0, column=2)

        self.division = tk.Button(self.ventana, text="/", command=self.dividir)
        self.division.grid(row=1, column=2)

        self.potencia = tk.Button(self.ventana, text="^", command=self.potenciar)
        self.potencia.grid(row=0, column=3)

        self.raiz = tk.Button(self.ventana, text="√", command=self.raiz_cuadrada)
        self.raiz.grid(row=1, column=3)

        self.logaritmo = tk.Button(self.ventana, text="log", command=self.logaritmo)
        self.logaritmo.grid(row=0, column=4)

        self.exponencial = tk.Button(self.ventana, text="exp", command=self.exponencial)
        self.exponencial.grid(row=1, column=4)

        # Creamos el campo de texto para el resultado
        self.resultado = tk.Label(self.ventana, text="")
        self.resultado.grid(row=2, column=0, columnspan=5)

    def sumar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 + num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def restar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 - num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def multiplicar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 * num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def dividir(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            if num2 != 0:
                resultado = num1 / num2 
                self.resultado.config(text=f"Resultado: {resultado}")
            else:
                self.resultado.config(text="Error: No se puede dividir por cero")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def potenciar(self):
        try:
            num1 = float(self.numero1.get())
            num2 = float(self.numero2.get())
            resultado = num1 ** num2
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def raiz_cuadrada(self):
        try:
            num1 = float(self.numero1.get())
            resultado = num1 ** 0.5
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def logaritmo(self):
        try:
            num1 = float(self.numero1.get())
            resultado = math.log(num1)
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")

    def exponencial(self):
        try:
            num1 = float(self.numero1.get())
            resultado = math.exp(num1)
            self.resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.resultado.config(text="Error: Ingresa números válidos")
        except OverflowError:
            self.resultado.config(text="Error: El resultado es demasiado grande")
            
    def run(self):
        self.ventana.mainloop()       
        
if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()
    
"""