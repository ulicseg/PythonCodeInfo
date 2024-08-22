import tkinter as tk
from tateti import crear_tablero
from caracruz import cargar_juego_caracruz
from piedrapapeltijera import cargar_juego_piedrapapeltijera

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("TKINTER")
ventana.geometry("500x350")
ventana.config(bg="#2c3e50")

def cerrar_ventana():
    """Cierra la ventana principal."""
    ventana.destroy()

def abrir_tateti():
    """Abre la ventana del juego Tateti."""
    ventana_tateti = tk.Toplevel(ventana)
    ventana_tateti.title("Tateti")
    ventana_tateti.geometry("300x300")
    crear_tablero(ventana_tateti)

def abrir_caracruz():
    """Abre la ventana del juego Cara o Cruz."""
    ventana_caracruz = tk.Toplevel(ventana)
    ventana_caracruz.title("Cara o Cruz")
    ventana_caracruz.geometry("500x500")
    cargar_juego_caracruz(ventana_caracruz)

def abrir_piedrapapeltijera():
    """Abre la ventana del juego Piedra, Papel o Tijeras."""
    ventana_piedrapapeltijera = tk.Toplevel(ventana)
    cargar_juego_piedrapapeltijera(ventana_piedrapapeltijera)

# Configurar etiquetas y botones en el menú principal
texto = tk.Label(ventana, text="Menú de Juegos", font=("Consolas", 28, "bold", "underline"), bg="#2c3e50", fg="white")
texto.pack(side="top", pady=20)

boton_Tateti = tk.Button(ventana, text="Tatetí", font=("Consolas", 16), bg="#2980b9", fg="white", command=abrir_tateti)
boton_CaraCruz = tk.Button(ventana, text="Cara o Cruz", font=("Consolas", 16), bg="#2980b9", fg="white", command=abrir_caracruz)
boton_piedrapapeltijera = tk.Button(ventana, text="Piedra, Papel o Tijeras", font=("Consolas", 16), bg="#2980b9", fg="white", command=abrir_piedrapapeltijera)
boton_salir = tk.Button(ventana, text="Salir", font=("Consolas", 16), bg="#c0392b", fg="white", command=cerrar_ventana)

boton_Tateti.pack(pady=10)
boton_CaraCruz.pack(pady=10)
boton_piedrapapeltijera.pack(pady=10)
boton_salir.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
