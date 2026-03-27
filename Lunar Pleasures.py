import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("moon.jpg", cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (800, 800))

edges = cv2.Canny(img, 50, 150)
edges = edges / 255.0
edges = edges ** 0.5

step = 6
amplitude = 6
offset = 0

plt.figure(figsize=(8, 8), facecolor='black')

width = edges.shape[1]
center = width // 2
mask = np.exp(-((np.arange(width) - center)**2) / (2*(width/4)**2))

for i in range(0, edges.shape[0], step):
    row = edges[i]

    row = np.convolve(row, np.ones(7)/7, mode='same')
    row[row < 0.15] = 0

    row = row * mask

    x = np.arange(len(row))
    x = (x - center) * 0.6 + center

    y = row * amplitude + offset

    plt.plot(x, y, color='white', linewidth=0.8)

    offset += 1.1

plt.gca().invert_yaxis()
plt.axis("off")
plt.tight_layout()

plt.savefig("moon_lines.png", facecolor='black', dpi=300)

plt.show()