from sympy import symbols, Eq, solve, sympify
import re
from time import sleep
import roman


def validar_equacao(equacao):
    # Verifique se a equação está no formato correto
    padrao = re.compile(r"^([+-]?\s*\d*\s*[a-z]\s*)+=\s*-?\d+$")
    return bool(padrao.match(equacao))


def validar_lucro(equacao):
    # Verifique se o lucro está no formato correto
    padrao = re.compile(r"^\s*([+-]?\s*\d*\s*[a-z]\s*)+(\s*[+-]?\s*\d*\s*[a-z]\s*)*\s*$")
    return bool(padrao.match(equacao))


nome_1 = input("Digite o nome da primeira variável: ")
nome_2 = input("Digite o nome da sehunda variável: ")
print("=-" * 27)

# Peça ao usuário para inserir o número de equações
while True:
    try:
        num_equacoes = int(input("Insira o número de equações: "))
        print("=-" * 27)
        break

    except:
        print("Valor inválido, digite um número inteiro positivo!!")


equacoes = []
for i in range(num_equacoes):
    while True:
        equacao_input = input(f"Insira a equação {roman.toRoman(i + 1)} no formato 'ax + by = c': ")
        if validar_equacao(equacao_input):
            equacoes.append(equacao_input)
            break
        else:
            print("Formato de equação inválido. Tente novamente.")

print("=-" * 27)
while True:
    lucro = input("Digite o lucro no formato ax + by: ")
    if validar_lucro(lucro):
        break
    else:
        print("Formato de lucro inválido. Tente novamente.")

# Extraia todas as variáveis únicas das equações
variaveis = symbols(' '.join(set(re.findall(r'[a-z]', ''.join(equacoes)))))

equacoes_sympy = []
lucro_sympy = []
for equacao in equacoes:
    # Separe os lados esquerdo e direito das equações
    equacao_esq, resultado_dir = equacao.split('=')

    # Adicione um '*' entre o coeficiente e a variável para cada termo na equação
    equacao_esq = re.sub(r'(\d+)([a-z])', r'\1*\2', equacao_esq)
    lucro = re.sub(r'(\d+)([a-z])', r'\1*\2', lucro)

    # Remova os espaços em branco
    equacao_esq = equacao_esq.replace(" ", "")
    resultado_dir = resultado_dir.replace(" ", "")
    lucro = lucro.replace(" ", "")

    # Converta as entradas do usuário em equações usando sympify
    try:
        equacao_sympy = Eq(sympify(equacao_esq), sympify(resultado_dir))
        equacoes_sympy.append(equacao_sympy)

    except Exception as e:
        print("Erro ao processar a equação: ", str(e))
        continue

for i in range(num_equacoes):
    for j in range(i + 1, num_equacoes):
        sleep(1)

        print('-=' * 27)
        print(f"Analisaremos a {roman.toRoman(i + 1)} e {roman.toRoman(j + 1)}: ")
        print('-=' * 27)

        solucao_1 = solve((equacoes_sympy[i], equacoes_sympy[j]), variaveis)
        solucao_x = solucao_1[variaveis[0]]
        solucao_y = solucao_1[variaveis[1]]
        lucro = sympify(lucro)

        solucao_a = equacoes_sympy[i].lhs.subs({variaveis[0]: solucao_x, variaveis[1]: solucao_y})
        solucao_b = equacoes_sympy[j].lhs.subs({variaveis[0]: solucao_x, variaveis[1]: solucao_y})

        for n in enumerate(equacoes_sympy):
            verificacao = equacoes_sympy[n[0]].lhs.subs({variaveis[0]: solucao_x, variaveis[1]: solucao_y})
            validar = bool()

            if verificacao <= equacoes_sympy[n[0]].rhs:
                validar = True

            elif equacoes_sympy[n[0]].rhs == 0 and verificacao >= 0:
                validar = True

            else:
                validar = False
                break

        if validar:
            # Todos Os Real, estou transformando em Inteiro, pois não existe fazer 3.6 de algo

            '''
            print(f"Quantidade de {nome_1}: {int(eval(str(solucao_x))):.2f}")
            print(f"Quantidade de {nome_2}: {int(eval(str(solucao_y))):.2f}")

            lucro_final = lucro.subs({variaveis[0]: int(eval(str(solucao_x))), variaveis[1]: int(eval(str(solucao_y)))})
            print(f"Seu lucro final: R${eval(str(lucro_final)):.2f}")
            '''

            # Caso pode valor Real, codigo abaixo

            # '''
            print(f"Quantidade de {nome_1}: {eval(str(solucao_x)):.2f}")
            print(f"Quantidade de {nome_2}: {eval(str(solucao_y)):.2f}")

            lucro_final = lucro.subs({variaveis[0]: eval(str(solucao_x)), variaveis[1]: eval(str(solucao_y))})
            print(f"Seu lucro final: R${eval(str(lucro_final)):.2f}")
            # '''

        else:
            print("Está Operação Não Possui Uma Solução Viável!!")
