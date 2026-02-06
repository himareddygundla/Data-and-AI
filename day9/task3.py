import numpy as np

# Create 3D array from 1 to 24 and reshape
a = np.arange(1, 25).reshape(2, 3, 4)

print("Original Array:")
print(a)
print("Shape:", a.shape)

# 1. Print all elements greater than 10
print("\nElements greater than 10:")
print(a[a > 10])

# 2. Count how many elements are even
even_count = np.sum(a % 2 == 0)
print("\nNumber of even elements:", even_count)

# 3. Replace all values less than 10 with 0
a[a < 10] = 0
print("\nArray after replacing values < 10 with 0:")
print(a)