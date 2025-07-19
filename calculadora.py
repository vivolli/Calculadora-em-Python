def mensagem(msg):
    print('=' * 42)
    print(msg.center(42))
    print('=' * 42)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        print("Erro: Raiz quadrada de número negativo não é permitida.")
        return None
    return a ** 0.5  

def menu():
    try:
        print("Escolha uma operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Sair")
        print("=" * 42)
        choice = int(input("Digite sua escolha (1-7): "))
        print("=" * 42)
        return choice
    except (ValueError, TypeError, IndexError):
        print("Opção inválida. Por favor, escolha um número entre 1 e 7.")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        return None
    
mensagem("Calculadora Simples")
while True:
    print("=" * 42)
    opcao = menu()
    if opcao is None or opcao == 7:
        mensagem("Saindo da calculadora...")
        break
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        continue

    if opcao == 1:
        resultado = soma(num1, num2)
    elif opcao == 2:
        resultado = subtracao(num1, num2)
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
    elif opcao == 4:
        resultado = divisao(num1, num2)
    elif opcao == 5:
        resultado = potencia(num1, num2)
    elif opcao == 6:
        resultado = raiz_quadrada(num1)
    else:
        print("Opção inválida. Tente novamente.")
        continue

    if resultado is not None:
        print(f"O resultado é: {resultado}")