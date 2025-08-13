








import numpy as np














matrice = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

mat = np.array(matrice)

print(mat)

print(type(mat))





# le code
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
mat = np.array(matrice)
mat.dtype, mat.itemsize, mat.nbytes





# le code
print(mat.shape)
print(mat.size, mat.shape[0] * mat.shape[1])
print(mat.ndim, len(mat.shape))





# le code
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice)

print(mat.min(), mat.max())
print(mat.dtype)


# le code avec type
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice, dtype=np.int8)
mat


# le code avec erreur
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
try:
    mat = np.array(matrice, dtype=np.uint8)
    # soit affichage du tableau avec les négatifs convertis implicitement par complément à 2
    # soit échec: "Python integer -128 out of bounds for uint8"
    mat
except OverflowError as e:
    print(e)





# votre code ici





# le code
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]

mat = np.array(l)
print(    mat     )
mat1 = mat.astype(np.int8) # des conversions sont effectuées
print(    mat1    )
print(    mat     )





# le code
l = [-1, 2, 3]
mat = np.array(l) # vous laissez numpy inférer le type
print(    mat    )
print(    mat*100    )
print(    mat.dtype    )


# le code
l = [-1, 2, 3]
mat = np.array(l, np.int8) # vous imposez le type
print(    mat    )
print(    mat*100    )











# le code
zorro = np.zeros(shape=(4, 5))
zorro


# le second code
zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
zorro1





# votre code ici








# votre code ici





# exemple avec arange
# comme avec le range() de Python
# la deuxième borne est exclue
np.arange(0, 5)


# exemple avec linspace
from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 30)
Y = np.sin(X)
plt.plot(X, Y)





# pour éviter l'affichage superflu, ajoutez un ;
plt.plot(X, Y);








# le code
borne_inf = 10
borne_sup = 20
np.random.randint(borne_inf, borne_sup)


# le code
np.random.randint(10, 20, size=(2, 3, 5))





# le code
np.random.rand()


# le code
np.random.randn(2, 3, 1)





# votre code ici





# le code
%timeit 1 + 1


# le code
%timeit -n 10000 1 + 1


%%timeit
a = 1
a + 1





# votre code ici
