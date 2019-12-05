from random import *
#--------------------------------ALGORITMO QUICKSORT - autor: Leonel Gonzales Vidales-----------------------------------
class QuickSort:
    A = []
    B = []
    C = []

    def intercambia(self, a, x, y):
        tmp = a[x]
        a[x] = a[y]
        a[y] = tmp

    def Particionar(self, a, p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if (a[j] <= x):
                i = i + 1
                self.intercambia (a, i, j)
        self.intercambia(a, i+1, r)
        return i + 1

    def QuickSort(self, a, p, r):
        if (p < r):
            q = self.Particionar(a, p, r)
            #print (A[p:r])
            self.QuickSort(a, p, q-1)
            self.QuickSort(a, q+1, r)
        return a

    def ordenar(self, a):
        p = 0
        r = len(a) - 1
        q = int((p + r) / 2)
        return self.QuickSort(a, p, r)
#-----------------------------------------------------------------------------------------------------------------------

    def generarAreglos(self):
        for i in range(0,100):
            self.A.append(randrange(1,100))
        for j in range(0,60):
            self.B.append(randrange(1,100))

    def OrdenarArreglos(self):
        ordenar = QuickSort()
        print('Arreglo A:......... ', self.A)
        ordenar.ordenar(self.A)
        print('Arreglo A ordenado: ', self.A)
        print('Arreglo B:......... ', self.B)
        ordenar.ordenar(self.B)
        print('Arreglo B ordenado: ', self.B)
        self.C = self.A
        self.C.extend(self.B)
        print('Arreglo C:......... ', self.C)
        ordenar.ordenar(self.C)
        print('Arreglo C ordenado: ', self.C)

Ordenamiento = QuickSort()
Ordenamiento.generarAreglos()
Ordenamiento.OrdenarArreglos()