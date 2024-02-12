import numpy as np

# Erstelle ein 2D Array mit numpy
array = np.array([[1, 2, 3], [4, 5, 6]])

# Zeige die Form des Arrays
print("Shape des Arrays:", array.shape)

# Darstellung des Arrays
print("Das Array:")
print(array)

# Zugriff auf Elemente und Manipulation der Form
# Zugriff auf das Element in der ersten Zeile und ersten Spalte
element = array[0, 0]
print("Element an Position (0, 0):", element)

# Ändere die Form des Arrays zu (3, 2)
reshaped_array = array.reshape(3, 2)
print("Neue Form des Arrays (3, 2):")
print(reshaped_array)

# Erstelle ein 1D Array und zeige seine Form
one_d_array = np.array([1, 2, 3, 4, 5])
print("1D Array:", one_d_array)
print("Shape des 1D Arrays:", one_d_array.shape)
