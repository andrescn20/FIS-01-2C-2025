import matplotlib.pyplot as plt

def dibujar_fuerzas(vectores, fuerza_neta):
    fig, ax = plt.subplots()

    # Dibujar el bloque en el centro (en 0,0)
    ax.plot(0, 0, 'ks', markersize=20)  # 'k' = black, square marker

    # Dibujar cada fuerza
    for i, (fx, fy) in enumerate(vectores):
        ax.quiver(0, 0, fx, fy, angles='xy', scale_units='xy', scale=1, color='blue',
                  label=f'Fuerza {i+1}' if i == 0 else None)  # solo mostrar una etiqueta para evitar repetición

    # Dibujar la fuerza neta en rojo
    ax.quiver(0, 0, fuerza_neta[0], fuerza_neta[1], angles='xy', scale_units='xy', scale=1, color='red', label='Fuerza neta')

    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    plt.title("Fuerzas aplicadas sobre el bloque")
    plt.xlabel("Fx")
    plt.ylabel("Fy")
    plt.show()


# --- Llamado de ejemplo ---
# Tres fuerzas aplicadas al bloque
vectores = [
    (10, 0),     # Fuerza 1: 10N en el eje x
    (-4, 5),     # Fuerza 2: 4N hacia la izquierda y 5N hacia arriba
    (3, -2)      # Fuerza 3: 3N a la derecha y 2N hacia abajo
]

# Suma de componentes:
# Fx_total = 10 + (-4) + 3 = 9
# Fy_total = 0 + 5 + (-2) = 3
fuerza_neta = (9, 3)

dibujar_fuerzas(vectores, fuerza_neta)
