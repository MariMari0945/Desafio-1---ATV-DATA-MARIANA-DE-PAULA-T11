import numpy as np

def calculate(numbers):
    #Checagem da lista para verificar se a mesma contém 9 números
    if len(numbers) != 9:
        raise ValueError("Sua lista deve conter 9 números")
    
    #Transforma a lista em um array 3x3 utilizando numpy
    matrix = np.array(numbers).reshape(3, 3)
    
    #Calcula as estatísticas requeridas para axis 0, axis 1 e da matriz "achatada" (lista)
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }

    return calculations  #Retorno do cálculo do dicionário inserido

#Teste da função 
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

