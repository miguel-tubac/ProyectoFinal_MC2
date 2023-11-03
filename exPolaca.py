class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor y sin nodos izquierdo y derecho.
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_arbol(expresion):
    if not expresion:
        # Si la expresión está vacía, levanta una excepción de valor.
        raise ValueError("Expresión vacía")

    pila = []

    for elemento in expresion:
        nodo = Nodo(elemento)
        if es_operando(elemento):
            # Si el elemento es un operando, se crea un nodo y se agrega a la pila.
            pila.append(nodo)
        else:
            if len(pila) < 2:
                # Si no hay suficientes operandos para el operador, levanta una excepción de valor.
                raise ValueError("Expresión no válida: no hay suficientes operandos para el operador")
            # Si es un operador, se crean los nodos derecho e izquierdo, se asignan como hijos del nuevo nodo,
            # y el nuevo nodo se agrega a la pila.
            nodo_derecha = pila.pop()
            nodo_izquierda = pila.pop()
            nodo.izquierda = nodo_izquierda
            nodo.derecha = nodo_derecha
            pila.append(nodo)

    if len(pila) != 1:
        # Si al final hay más de un nodo en la pila, levanta una excepción de valor.
        raise ValueError("Expresión no válida: quedan nodos en la pila al final")

    return pila[0]

def es_operando(elemento):
    # Verifica si un elemento es un operando (en este caso, un dígito).
    return elemento.isdigit()

def recorrer_inorden(nodo):
    if nodo:
        # Realiza un recorrido inorden del árbol y muestra los valores de los nodos.
        recorrer_inorden(nodo.izquierda)
        print(nodo.valor, end=' ')
        recorrer_inorden(nodo.derecha)

# Ejemplo de uso
expresion_polaca = ['6', '9', '/', '3', '*' ]
arbol = construir_arbol(expresion_polaca)
recorrer_inorden(arbol)