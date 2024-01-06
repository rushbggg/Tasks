import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

file_path = '2d_scalar_field.csv'
data = pd.read_csv(file_path)

# reshape the data into a grid
grid_x, grid_y = np.mgrid[min(data['x']):max(data['x']):100j, min(data['y']):max(data['y']):100j]
grid_z = griddata((data['x'], data['y']), data['S'], (grid_x, grid_y), method='cubic')

#create an overall view

##2D figure
plt.figure()
plt.contourf(grid_x, grid_y, grid_z)
plt.colorbar()
plt.title('Projection of S on XY Grid')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

##3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis')

fig.colorbar(surf)
ax.set_title('3D Surface Plot of S over XY Grid')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('S Value')
plt.show()

# gradient descent for searching critical points

## introduce Gaussian filter for smoothing
smoothed_z = gaussian_filter(grid_z, sigma=1)

## define a function to compute the gradient and Hessian
def func(Z):
    Zx, Zy = np.gradient(Z)
    Zxx, Zxy = np.gradient(Zx)
    Zyx, Zyy = np.gradient(Zy)
    return Zx, Zy, Zxx, Zyy, Zxy

Zx, Zy, Zxx, Zyy, Zxy = func(smoothed_z)

## gradient descent
gradient_magnitude = np.sqrt(Zx**2 + Zy**2)
threshold = 0.01
zgp = gradient_magnitude < threshold #zero gradient points

## identify the critical points
min, max, saddle = [], [], []

for i in range(grid_x.shape[0]):
    for j in range(grid_x.shape[1]):
        if zgp[i, j]:
            Hessian = np.array([[Zxx[i, j], Zxy[i, j]], [Zxy[i, j], Zyy[i, j]]])
            eigenvalues = np.linalg.eigvals(Hessian)
            if np.all(eigenvalues > 0):
                min.append((grid_x[i, j], grid_y[i, j], smoothed_z[i, j]))
            elif np.all(eigenvalues < 0):
                max.append((grid_x[i, j], grid_y[i, j], smoothed_z[i, j]))
            elif np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
                saddle.append((grid_x[i, j], grid_y[i, j], smoothed_z[i, j]))

minima = np.array(min)
maxima = np.array(max)
saddle_points = np.array(saddle)

print(minima,maxima,saddle_points)

## plot the iso-contours for specific isovalues (0, 1, 2) with marked minima, maxima, and saddle points
plt.figure(figsize=(12, 10))

contours = plt.contour(grid_x, grid_y, grid_z, levels=[0, 1, 2], cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8, fmt='%1.1f')

plt.scatter(minima[:, 0], minima[:, 1], color='red', marker='x', label='Minima')
plt.scatter(maxima[:, 0], maxima[:, 1], color='blue', marker='+', label='Maxima')
plt.scatter(saddle_points[:, 0], saddle_points[:, 1], color='green', marker='o', label='Saddle Points')

plt.title('Iso-Contours for Isovalues 0, 1, 2 with Marked Minima, Maxima, and Saddle Points')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(contours, label='Scalar Value (S)')
plt.legend()
plt.grid(True)
plt.show()
