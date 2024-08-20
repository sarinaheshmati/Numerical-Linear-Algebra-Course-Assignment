import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the oval
a = 2  # semi-major axis
b = 1  # semi-minor axis
theta = np.linspace(0, 2*np.pi, 200)  # angle parameter
x = a * np.cos(theta)
y = b * np.sin(theta)

# Define the orthogonal matrix
M = np.array([[0, -1], [1, 0]])  # 90-degree rotation matrix

# Transform the oval by multiplying its points by the matrix
points = np.column_stack([x, y])
transformed_points = points @ M

# Plot the original and transformed ovals
fig, ax = plt.subplots()
ax.plot(x, y, label='Original Oval')
ax.plot(transformed_points[:, 0], transformed_points[:, 1], label='Transformed Oval')
ax.axis('equal')
ax.legend()
plt.show()
