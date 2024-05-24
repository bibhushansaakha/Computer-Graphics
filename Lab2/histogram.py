import matplotlib.pyplot as plt

def draw_histogram(frequencies, algorithm):
    bar_width = 10
    spacing = 5
    start_x = 0
    for i, frequency in enumerate(frequencies):
        x0 = start_x + i * (bar_width + spacing)
        y0 = 0
        x1 = x0
        y1 = frequency
        points_left = algorithm(x0, y0, x1, y1)
        plt.plot(*zip(*points_left), 'b-')
        points_right = algorithm(x0 + bar_width, y0, x1 + bar_width, y1)
        plt.plot(*zip(*points_right), 'b-')
        points_top = algorithm(x0, y1, x0 + bar_width, y1)
        plt.plot(*zip(*points_top), 'b-')
    plt.xlabel('Bars')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()
