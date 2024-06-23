import matplotlib.pyplot as plt

def graficar_cuadrado(ax, x, y, tamano):
    # Definir las coordenadas del cuadrado
    cuadrado = [[x, y], [x + tamano, y], [x + tamano, y + tamano], [x, y + tamano], [x, y]]
    # Dibujar el cuadrado
    ax.plot(*zip(*cuadrado), color='black')

def graficar_rectangulo(ax, x, y, ancho, alto):
    # Definir las coordenadas del rectángulo
    rectangulo = [[x, y], [x + ancho, y], [x + ancho, y + alto], [x, y + alto], [x, y]]
    # Dibujar el rectángulo
    ax.plot(*zip(*rectangulo), color='black')

def graficar_triangulo(ax, x, y, base, altura):
    # Definir las coordenadas del triángulo
    triangulo = [[x, y], [x + base / 2, y + altura], [x - base / 2, y + altura], [x, y]]
    # Dibujar el triángulo
    ax.plot(*zip(*triangulo), color='black')

def graficar_rombo(ax, x, y, lado):
    # Definir las coordenadas del rombo
    rombo = [[x, y], [x + lado / 2, y + lado], [x, y + 2 * lado], [x - lado / 2, y + lado], [x, y]]
    # Dibujar el rombo
    ax.plot(*zip(*rombo), color='black')

def main():
    # Crear una figura y un eje
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    ax.grid(True)

    # Graficar las figuras
    graficar_cuadrado(ax, -100, 50, 50)
    graficar_rectangulo(ax, -50, 0, 50, 30)
    graficar_triangulo(ax, 0, -50, 50, 50)
    graficar_rombo(ax, 50, -100, 50)

    # Mostrar la figura
    plt.show()

if __name__ == "__main__":
    main()
