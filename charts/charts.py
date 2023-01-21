import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()  #obtenemos cordenadas desde matlib
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()