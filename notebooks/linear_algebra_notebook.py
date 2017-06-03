# %%
import numpy

# %% complex numbers
a = numpy.array([1 + 2j, 2 + 3j])
a
a.imag
a.real
a.imag = numpy.array([5, 6])
a

# %% arange, resape and extended slices
a = numpy.arange(10)

# map array onto array with different dimensions.
a.reshape((2,5))

# slice array from index 2 to 5
a[2:5]

# select even indecies
a[::2]

# reverse array
a[::-1]

# even indecies of reversed array
a[::-2]

# %% array generation
numpy.ones(2)
numpy.ones((2,2))
numpy.ones((2,))

numpy.linspace(-2, 2, 5)

numpy.eye(2)
numpy.identity(2)
# %% dot product
# scalars
numpy.dot(2,2)

# arrays
numpy.dot([2, 3], [4, 5])

# complex numbers
numpy.dot(2 + 2j, 2 + 3j)

# complex arrays
numpy.dot([2 + 1j, 3j], [1 + 2j, 3])

# 2D arrays
a = [[1, 0],
     [0, 1]]
b = [[4, 1],
     [2, 2]]
numpy.dot(a, b)

# more that two dimensions
a = numpy.arange(3*4*5*6).reshape((3,4,5,6))
b = numpy.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
numpy.dot(a, b)[2,3,2,1,2,2]
sum(a[2,3,2,:] * b[1,2,:,2])

# %% vdot product (takes complex conjugate of first argument before computing product)
numpy.vdot([2, 3], [4, 5])

# compare with dot
numpy.vdot(2 - 2j, 1 + 3j)
numpy.dot(2 + 2j, 1 + 3j)

numpy.vdot(2 - 1j, 2 - 1j)
numpy.dot(2 + 2j, 2 + 1j)

# compare with dot which is matrix product
a = [[1, 0],
     [0, 1]]
b = [[4, 1],
     [2, 2]]
numpy.vdot(a, b)
1*4 + 0*1 + 0*2 + 1*2

# %% inner product
numpy.inner([2, 3], [4, 5])

# compare with dot and vdot
numpy.inner(2 - 2j, 1 + 3j)
numpy.dot(2 - 2j, 1 + 3j)
numpy.vdot(2 + 2j, 1 + 3j)

numpy.inner([2 - 1j, 2j], [2 - 1j, 1j])
numpy.dot([2 - 1j, 2j], [2 - 1j, 1j])
numpy.vdot([2 + 1j, -2j], [2 - 1j, 1j])

# compare with dot and vdot (inner takes transpose of second argument
a = [[1, 0],
     [0, 1]]
b = [[4, 1],
     [2, 2]]
numpy.inner(a, b)
numpy.dot(a, numpy.transpose(b))
numpy.vdot(a, b)

# compare complex array(inner product takes transpose of second argument.
# To be consistent with scalar and 1D vector work expect it to take conjugate of first argument)
a = [[1+1j, 2j],
     [4j, 1j]]
b = [[2+4j, 1j],
     [2j, 5j]]
numpy.inner(a, numpy.transpose(b))
numpy.dot(a, b)
numpy.vdot(a, b)

# %% outter product
a = numpy.ones((5,))
b = numpy.linspace(-2, 2, 5)
r = numpy.outer(a, b)

c = 1j*numpy.ones((5,))
d = numpy.linspace(-2, 2, 5)
i = numpy.outer(a, b)

r + i

x = numpy.array(['a', 'b', 'c'], dtype=object)
numpy.outer([1, 2, 3], x)

# %% matrix multiply
a = [[1, 0],
     [0, 1]]
b = [[4, 1],
     [2, 2]]
numpy.matmul(a, b)

a = [[1, 0],
     [0, 1]]
b = [1, 2]
numpy.matmul(a, b)

# %% tensor product
