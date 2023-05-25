import math
def sigmoide_function(z):
    """Retorna un valor entre 0 y 1
    
    Keyword arguments:
    z:  entrada o suma ponderada de los valores de entrada
    La función sigmoide es una función matemática utilizada en las redes neuronales artificiales como una función de activación para introducir no linealidad en los datos
    No salta de 0 a 1 sino un tenemos un crecimiento entre esos valores.
    f(x) = 1 / (1 + e^(-x))
    """
    
    return (1/(1+math.exp(-z)))

if __name__ == "__main__":
    print(f"La probabilidad es de:{sigmoide_function(10)}")