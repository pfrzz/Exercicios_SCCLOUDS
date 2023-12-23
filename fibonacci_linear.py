def fibonacci_linear(n):
    if n < 0:
        print(mensagem_erro)
        return

    anterior, atual = 0, 1
    
    for contagem in range(n):
        termo = anterior
        anterior, atual = atual, anterior + atual

    print(mensagem + str(anterior))

mensagem = "O número nessa posição é: "
mensagem_erro = "O index precisa ser positivo."

try:
    n = int(input("Qual index na sequência de Fibonacci você quer? "))
    fibonacci_linear(n)
except ValueError:
    print("Por favor, digite um número inteiro válido.")