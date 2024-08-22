import tkinter as tk
from tkinter import messagebox

def crear_tablero(ventana):
    # Color de fondo para los widgets
    color_fondo = "#2c3e50"

    # Variables globales
    jugador_actual = "X"
    botones = [[None]*3 for _ in range(3)]

    def manejar_click(fila, columna):
        nonlocal jugador_actual

        # Cambiar el texto del botón si está vacío
        if botones[fila][columna].cget("text") == "":
            botones[fila][columna].config(text=jugador_actual)
            
            # Verificar el resultado del juego
            if verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡Jugador {jugador_actual} gana!")
                ventana.destroy()
            elif verificar_empate():
                messagebox.showinfo("Fin del juego", "¡Empate!")
                ventana.destroy()
            else:
                # Alternar el turno del jugador
                jugador_actual = "O" if jugador_actual == "X" else "X"

    def verificar_ganador():
        for i in range(3):
            # Verificar filas y columnas
            if botones[i][0].cget("text") == botones[i][1].cget("text") == botones[i][2].cget("text") != "":
                return True
            if botones[0][i].cget("text") == botones[1][i].cget("text") == botones[2][i].cget("text") != "":
                return True

        # Verificar diagonales
        if botones[0][0].cget("text") == botones[1][1].cget("text") == botones[2][2].cget("text") != "":
            return True
        if botones[0][2].cget("text") == botones[1][1].cget("text") == botones[2][0].cget("text") != "":
            return True
        
        return False

    def verificar_empate():
        for fila in botones:
            for boton in fila:
                if boton.cget("text") == "":
                    return False
        return True

    # Crear el tablero en la ventana dada
    for fila in range(3):
        for columna in range(3):
            boton = tk.Button(ventana, text="", width=10, height=3, bg=color_fondo, fg="white", font=("Arial", 16),command=lambda f=fila, c=columna: manejar_click(f, c))
            boton.grid(row=fila, column=columna, sticky="nsew")
            botones[fila][columna] = boton

    # Configurar el color de fondo de la ventana
    ventana.config(bg=color_fondo)

    # Configurar el peso de las filas y columnas
    for i in range(3):
        ventana.grid_rowconfigure(i, weight=1)
        ventana.grid_columnconfigure(i, weight=1)
