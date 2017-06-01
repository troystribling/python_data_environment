# %%
import numpy

# %% complex numbers
a = numpy.array([1 + 2j, 2 + 3j])
a
a.imag
a.real
a.imag = numpy.array([5, 6])
a

# %% arange


# %%
# dot product
# scalars
numpy.dot(2,2)

# arrays
numpy.dot([2, 3], [4, 5])

# complex numbers
numpy.dot(2 + 2j, 1 + 3j)
numpy.dot(2 + 1j, 2 - 1j)

# complex arrays
numpy.dot([2 + 1j, 3j], [1 + 2j, 3])

# 2D arrays
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
numpy.dot(a, b)
