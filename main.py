import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations
import random 
# Puntos en el espacio 3D
# points = [random.sample(range(-100,100), 3), random.sample(range(-10,10), 3), random.sample(range(-10,10), 3), random.sample(range(-10,10), 3), random.sample(range(-10,10), 3)]
# print(points)
points = []
for i in range(random.randint(5,10)):
    points.append((random.randint(-100,100),random.randint(-100,100),random.randint(-100,100)))
    # points.append(random.sample(range(-100,100), 3))
# Obtener las coordenadas x, y, z por separado
x = [point[0] for point in points]
y = [point[1] for point in points]
z = [point[2] for point in points]

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar los puntos
ax.scatter(x, y, z, c='red', marker='o')

# Dibujar las líneas para cada combinación de puntos posibles
for combination in combinations(points, 2):
    print("Combinación ", combination)
    line_x = [combination[0][0], combination[1][0]]
    print("Linea x ",line_x)
    line_y = [combination[0][1], combination[1][1]]
    print("Linea y ",line_y)
    line_z = [combination[0][2], combination[1][2]]
    print("Linea z ",line_z)
    ax.plot(line_x, line_y, line_z, c='blue')

# Etiquetar los puntos
for i, point in enumerate(points):
    ax.text(point[0], point[1], point[2], f'Star{i+1}', color='black')

# Configurar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
