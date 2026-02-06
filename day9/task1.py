import numpy as np

# create numbers from 1 to 24
a = np.arange(1, 25)

# reshape into 3D array
a = a.reshape(2, 3, 4)

# print array and shape
print(a)
print("Shape:", a.shape)
