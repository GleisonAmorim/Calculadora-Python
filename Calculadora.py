# Função para somar dois números
def soma(num1, num2):
    return num1 + num2

# Função para subtrair dois números
def subtracao(num1, num2):
    return num1 - num2

# Função para multiplicar dois números
def multiplicacao(num1, num2):
    return num1 * num2

# Função para dividir dois números
def divisao(num1, num2):
    return num1 / num2

# Loop principal da calculadora
while True:
    # Exibir opções do menu
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    # Obter entrada do usuário
    escolha = input("Digite sua escolha (0-4): ")

    # Verificar a escolha do usuário
    if escolha == "0":
        print("Saindo...")
        break
    elif escolha in ["1", "2", "3", "4"]:
        # Obter os números para a operação
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Executar a operação correspondente
        if escolha == "1":
            resultado = soma(num1, num2)
            operacao = "+"
        elif escolha == "2":
            resultado = subtracao(num1, num2)
            operacao = "-"
        elif escolha == "3":
            resultado = multiplicacao(num1, num2)
            operacao = "*"
        elif escolha == "4":
            resultado = divisao(num1, num2)
            operacao = "/"

        # Exibir o resultado
        print(f"{num1} {operacao} {num2} = {resultado}\n")
    else:
        print("Opção inválida. Tente novamente.\n")
