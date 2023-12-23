def eh_primo(num, divisor=2):
    if num < 2:
        return False
    if divisor > num // 2:
        return True
    if num % divisor == 0:
        return False 
    return eh_primo(num, divisor + 1)
    
def numeros_ate(n):
    primos = []
    for i in range(2, n + 1):
        if eh_primo(i):
            primos.append(i)
    return primos
    
try: 
    n = int(input("Digite um número: "))
    if n > 1:
        result = numeros_ate(n)
        print(f"Os números primos até {n} são: {result}")
    else: 
        print(f"Por favor, digite um número maior que 1.")
        
except ValueError:
    print("Por favor, digite um número inteiro válido")