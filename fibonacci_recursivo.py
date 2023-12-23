def fibonacci_recursivo(n):
    if n <=0:
        return 0 
    elif n == 1:
        return 1
    else: 
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
        

mensagem = "O número nessa posição é: "
mensagem_erro = "O index precisa ser positivo."

try:
    n = int(input("Qual index na sequência de Fibonacci você quer? "))
    if n < 0: 
        print(mensagem_erro)
    else:
        resultado = fibonacci_recursivo(n)
    print(mensagem + str(resultado))
except ValueError:
    print("Por favor, digite um número inteiro válido.")