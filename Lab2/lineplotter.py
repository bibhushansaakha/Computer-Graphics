import matplotlib.pyplot as plt

def drawline(algorithm, x0, y0, x1, y1, name):
    points = algorithm(x0, y0, x1, y1)
    xpoint = [point[0] for point in points]
    ypoint = [point[1] for point in points]
    pltline(xpoint, ypoint, name)

def pltline(xpoint, ypoint, name):
    plt.gcf().canvas.manager.set_window_title(name)
    plt.grid(True)
    plt.plot(xpoint, ypoint, label=name)
    plt.title(name)
    plt.legend()
    plt.show()
