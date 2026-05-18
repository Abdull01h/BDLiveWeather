import matplotlib.pyplot as plt


def draw_graph(temps):

    plt.plot(temps)

    plt.title("Temperature Graph")

    plt.xlabel("Time")

    plt.ylabel("Temperature")

    plt.grid(True)

    plt.show()
