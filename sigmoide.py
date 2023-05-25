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
    """
    A partir de la función sigmoide_function, se construira el siguiente perceptron basandonos en el caso
    de predecir si la persona va a viajar o no contemplando variables booleanas las cuales son:
    dinero,tiempo y clima
    """
    inputs = [0,1,1]
    weights = [2,1,2]
    total = 0
    for i in range (len(inputs)):
        total += inputs[i]*weights[i]
    # definimos un umbral de si el resultado es mayor a 0.5 se viaja
    probability = sigmoide_function(total)
    if probability>0.5:
        print(f'probabilidad:{probability} => Viajamos 😁')
    else:
        print(f'probabilidad:{probability}  =>No viajamos 😔')
