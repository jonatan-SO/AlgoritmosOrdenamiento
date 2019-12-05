# Algoritmos de ordenamiento

La ordenación o clasificación de datos (sort, en inglés) es una operación consistente en disponer
un conjunto —estructura— de datos en algún determinado orden con respecto a uno de los
campos de los elementos del conjunto. Por ejemplo, cada elemento del conjunto de datos de una
guía telefónica tiene un campo nombre, un campo dirección y un campo número de teléfono;
la guía telefónica está dispuesta en orden alfabético de nombres. Los elementos numéricos se
pueden ordenar en orden creciente o decreciente de acuerdo al valor numérico del elemento. En
terminología de ordenación, el elemento por el cual está ordenado un conjunto de datos (o se está
buscando) se denomina clave.

![ComplejidadAlgoritmosOrdenacion](http://www.leonet.mx/imagenes/complejidad_algoritmos_ordenamiento.png)

## Quicksort

El algoritmo conocido como *quicksort* (ordenación rápida) recibe su nombre de su autor, Tony
Hoare. La idea del algoritmo es simple, se basa en la división en particiones de la lista a ordenar,
por ello se puede considerar que aplica la técnica "divide y vencerás". El método es, posiblemente,
el más pequeño de código, más rápido, más elegante y más interesante y eficiente de
los algoritmos conocidos de ordenación.

Este método se basa en dividir los *n* elementos de la lista a ordenar en dos partes o particiones
separadas por un elemento: una partición izquierda, un elemento central denominado pivote
o elemento de partición y una partición derecha. La partición o división se hace de tal forma
que todos los elementos de la primera sublista (partición izquierda) sean menores que todos
los elementos de la segunda sublista (partición derecha). Las dos sublistas se ordenan entonces
independientemente.

Para dividir la lista en particiones (sublistas) se elige uno de los elementos de la lista y se
utiliza como pivote o elemento de partición. Si se elige una lista cualquiera con los elementos
en orden aleatorio, se puede elegir cualquier elemento de la lista como pivote, por ejemplo, el
primer elemento de la lista. Si la lista tiene algún orden parcial que se conoce, se puede tomar
otra decisión para escogerlo. Idealmente, el pivote se debe elegir de modo que se divida la lista
exactamente por la mitad de acuerdo al tamaño relativo de las claves. Por ejemplo, si se tiene
una lista de enteros de 1 a 10, 5 o 6 serían pivotes ideales, mientras que 1 o 10 serían elecciones
“pobres” de pivotes.

Una vez que el pivote ha sido elegido, se utiliza para ordenar el resto de la lista en dos sublistas:
una tiene todas las claves menores que el pivote y la otra, todos los elementos (claves) mayores o iguales que el pivote (o al revés). Estas dos listas parciales se ordenan recursivamente
utilizando el mismo algoritmo; es decir, se llama sucesivamente al propio algoritmo quicksort.
La lista final ordenada se consigue concatenando la primera sublista, el pivote y la segunda lista,
en ese orden, en una única lista. La primera etapa de quicksort es la división o “particionado”
recursivo de la lista hasta que todas las sublistas constan de sólo un elemento.

Algoritmo:

```
Inicio
    Si lista tiene más de un elemento
        Particionar la lista en dos sublistas (Sublista Izquierda y Sublista Derecha)
        Aplicar el algoritmo QuickSort() a Sublist Izquierda
        Aplicar Algoritmo QuickSort() a Sublista Derecha
        Combinar las 2 listas ordenadas
    Fin Si
FIN
```

Pseudocódigo:

```
QuickSort(A,p,r)
Inicio
    Si p < r entonces // Si la lista tiene más de un elemento
        q =Particionar(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
    Fin Si
Fin

Particionar(A,p,r)
Inicio
    x=A[r]
    i=p-1
    para j=p hasta r-1
        Si A[j]<=x
            i=i+1
            intercambiar A[i] con A[j]
        Fin Si
    Fin para
    intercambiar A[i+1] con A[r]
    retornar i+1
Fin
```


Ejemplo:

![quicksort-example](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)

Fuente:

Baka, B. (2017). Python Data Structures and Algorithms. Birmingham, Reino Unido: Packtpub.

Cormen, T. (2013). Algorithms Unlocked. Cambridge: IT Press.

Cormen, T., Leiserson, C., Rivest, R., & Clifford, S. (2009). Introduction to Algorithms. Cambridge: The MIT Press.

Joyanes-Aguilar, L., & Zahonero-Martinez, I. (2008). Estructuras de datos en Java. Madrid, España: McGraw-Hill.

