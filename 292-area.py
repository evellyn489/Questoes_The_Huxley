def triangulo(a, c):
    area = (a * c)/2
    return area

def circulo(c):
    area = 3.14159 * c**2
    return area

def trapezio(a, b, c):
    area = ((a + b) * c)/2
    return area

def quadrado(b):
    area = b**2
    return area

def retangulo(a, b):
    area = a * b
    return area

a, b, c = [float(x) for x in input().split()]

print(f'TRIANGULO: {triangulo(a, c):.3f}')
print(f'CIRCULO: {circulo(c):.3f}')
print(f'TRAPEZIO: {trapezio(a, b, c):.3f}')
print(f'QUADRADO: {quadrado(b):.3f}')
print(f'RETANGULO: {retangulo(a, b):.3f}')