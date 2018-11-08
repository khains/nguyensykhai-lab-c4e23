from matplotlib import pyplot
x = [18, 4, 2]
y = ["PC", "MAC", "Linux"]
pyplot.pie(x, labels = y, autopct = "%.1f%%", shadow=True, explode=[0, 0.15, 0])
pyplot.title("PC vs MAC vs Linux usege")
pyplot.axis("equal")
pyplot.show()