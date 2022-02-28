from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

z = np.array(
    [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    ]
)
x, y = np.meshgrid(range(z.shape[1]), range(z.shape[0]))

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z)
plt.title("z as 3d height map")
plt.show()

# show hight map in 2d
plt.figure()
plt.title("z as 2d heat map")
p = plt.imshow(z)
plt.colorbar(p)
plt.show()
