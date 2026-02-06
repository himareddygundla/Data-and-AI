import numpy as np

# Create 3D array
a = np.arange(1, 25).reshape(2, 3, 4)

# Print first layer
print(a[0])

# Print last layer
print(a[-1])

# Print element at layer=1, row=2, column=3 (1-based indexing)
print(a[0, 1, 2])

# Print first row of all layers
print(a[:, 0, :])

# Print last row of all layers
print(a[:, -1, :])