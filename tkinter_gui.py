import tkinter as tk
import logica_clips

def obtener_estrategia():
    equipo_estado = equipo_estado_var.get()
    rival_estado = rival_estado_var.get()
    tiempo = tiempo_var.get()

    logica_clips.env.reset()  # Reiniciar el entorno CLIPS

    # Afirmar los hechos seleccionados
    logica_clips.env.assert_string(f"(Equipo_estado (Equipo_A_estado {equipo_estado}))")
    if equipo_estado in ["delanteros_rapidos", "mediocampistas_creativos", "defensa_fuerte"]:
        logica_clips.env.assert_string(f"(Rival_estado (Equipo_B_estado {rival_estado}))")
    else:
        logica_clips.env.assert_string(f"(Tiempo (Tiempo_restante {tiempo}))")

    logica_clips.env.run() #Ejecutar las reglas CLIPS

    estrategia = None
    for fact in logica_clips.env.facts():
        if fact.template.name == "Estrategia":
            estrategia = fact['Estrategia_equipo_A']
            break

    if estrategia:
        cuadro_texto_estrategia.delete("1.0", tk.END)
        cuadro_texto_estrategia.insert(tk.END, estrategia)
    else:
        cuadro_texto_estrategia.delete("1.0", tk.END)
        cuadro_texto_estrategia.insert(tk.END, "No se encontró estrategia.")

def actualizar_rival_estado(*args):
    equipo_estado = equipo_estado_var.get()
    if equipo_estado in ["delanteros_rapidos", "mediocampistas_creativos", "defensa_fuerte"]:
        rival_estado_label.grid(row=0, column=2, sticky="w")
        rival_estado_menu.grid(row=0, column=3, sticky="w")
        tiempo_label.grid_forget()
        tiempo_menu.grid_forget()
    else:
        rival_estado_label.grid_forget()
        rival_estado_menu.grid_forget()
        tiempo_label.grid(row=0, column=2, sticky="w")
        tiempo_menu.grid(row=0, column=3, sticky="w")

ventana = tk.Tk()
ventana.title("Sistema Experto de Fútbol")

# Variables para almacenar las selecciones
equipo_estado_var = tk.StringVar(ventana)
rival_estado_var = tk.StringVar(ventana)
tiempo_var = tk.StringVar(ventana)

# Opciones para las selecciones
equipo_estados = ["perdiendo", "ganando_por_1_gol", "ganando_por_3_goles", "delanteros_rapidos", "mediocampistas_creativos", "defensa_fuerte"]
rival_estados = ["defensas_lentos", "mediocampo_debil", "delanteros_debiles"]
tiempos = ["corto", "largo"]

# Etiquetas y menús desplegables
tk.Label(ventana, text="Estado del Equipo A:").grid(row=0, column=0, sticky="w")
equipo_estado_menu = tk.OptionMenu(ventana, equipo_estado_var, *equipo_estados)
equipo_estado_menu.grid(row=0, column=1, sticky="w")

# Cuadro de texto para mostrar la estrategia
cuadro_texto_estrategia = tk.Text(ventana, height=5, width=50)
cuadro_texto_estrategia.grid(row=1, column=0, columnspan=4)

rival_estado_label = tk.Label(ventana, text="Estado del Equipo B:")
rival_estado_menu = tk.OptionMenu(ventana, rival_estado_var, *rival_estados)

tiempo_label = tk.Label(ventana, text="Tiempo Restante:")
tiempo_menu = tk.OptionMenu(ventana, tiempo_var, *tiempos)

# Botón para obtener la estrategia
boton_obtener = tk.Button(ventana, text="Obtener Estrategia", command=obtener_estrategia)
boton_obtener.grid(row=2, column=0, columnspan=4)

# Inicializar CLIPS
logica_clips.inicializar_clips()

# Configurar el comando de actualización
equipo_estado_var.trace("w", actualizar_rival_estado)

# Llamar a la función de actualización al inicio
actualizar_rival_estado()

ventana.mainloop()