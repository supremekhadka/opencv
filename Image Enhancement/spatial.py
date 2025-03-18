import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

image = cv2.imread('mountain.JPG', cv2.IMREAD_GRAYSCALE)

scale_factor = 0.01
image = cv2.resize(image, (0, 0), fx=scale_factor, fy=scale_factor)

image.shape

plt.imshow(image, cmap='gray')

image = image.astype(np.float32) / 255.0

h, w = image.shape

x, y = np.meshgrid(np.arange(w), np.arange(h))
y = h - y

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection = '3d')

ax.plot_surface(x, y, image, cmap='gray', edgecolor='none')
ax.set_xlabel("X (Width)")
ax.set_ylabel("Y (Height)")
ax.set_zlabel("Intensity")
ax.set_title("Spatial Domain 3D Visualization")
ax.view_init(elev=60, azim=120)

plt.show()