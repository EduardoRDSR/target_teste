#1)
def is_fibonacci_number(n):
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    def is_fibonacci(n):
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

    def generate_fibonacci_sequence(limit):
        sequence = [0, 1]
        while sequence[-1] < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

    if n < 0:
        return f"{n} não pertence à sequência de Fibonacci."
    
    fibonacci_sequence = generate_fibonacci_sequence(n)
    
    if n in fibonacci_sequence:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        if is_fibonacci(n):
            return f"{n} pertence à sequência de Fibonacci."
        else:
            return f"{n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = is_fibonacci_number(numero)
print(resultado)

#2)
def contar_letra_a(texto):
    texto_minusculo = texto.lower()

    quantidade_a = texto_minusculo.count('a')

    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto_usuario = input("Informe uma string: ")
contar_letra_a(texto_usuario)

#3)
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)