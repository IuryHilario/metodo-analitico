from sympy import symbols, Eq, solve, sympify
import re
from time import sleep
import roman
from typing import List, Tuple, Dict, Any

def validate_equation(equation: str) -> bool:
    """Valida se a equação está no formato correto."""
    pattern = re.compile(r"^([+-]?\s*\d*\s*[a-z]\s*)+=\s*-?\d+$")
    return bool(pattern.match(equation))

def validate_profit_function(equation: str) -> bool:
    """Valida se a função de lucro está no formato correto."""
    pattern = re.compile(r"^\s*([+-]?\s*\d*\s*[a-z]\s*)+(\s*[+-]?\s*\d*\s*[a-z]\s*)*\s*$")
    return bool(pattern.match(equation))

def get_user_input(prompt: str, validator=None, error_msg: str = "Entrada inválida") -> str:
    """
    Obtém entrada do usuário com validação.
    
    Args:
        prompt: Mensagem exibida ao usuário
        validator: Função de validação opcional
        error_msg: Mensagem de erro para entrada inválida
    
    Returns:
        str: Entrada do usuário validada
    """
    while True:
        user_input = input(prompt)
        if validator is None or validator(user_input):
            return user_input
        print(error_msg)

def process_equation(equation: str) -> Tuple[str, str]:
    """
    Processa e formata a equação para uso com sympy.
    
    Args:
        equation: Equação em formato string
    
    Returns:
        Tuple[str, str]: Lado esquerdo e direito da equação processados
    """
    left_side, right_side = equation.split('=')
    left_side = re.sub(r'(\d+)([a-z])', r'\1*\2', left_side)
    return left_side.replace(" ", ""), right_side.replace(" ", "")

def solve_equations(equations_sympy: List[Eq], variables: tuple, profit_expr: str) -> None:
    """
    Resolve o sistema de equações e calcula o lucro.
    
    Args:
        equations_sympy: Lista de equações no formato sympy
        variables: Tupla com as variáveis do sistema
        profit_expr: Expressão de lucro
    """
    num_equations = len(equations_sympy)
    
    for i in range(num_equations):
        for j in range(i + 1, num_equations):
            sleep(1)
            print('-=' * 27)
            print(f"Analisando equações {roman.toRoman(i + 1)} e {roman.toRoman(j + 1)}: ")
            print('-=' * 27)

            try:
                solution = solve((equations_sympy[i], equations_sympy[j]), variables)
                if not solution:
                    print("Nenhuma solução encontrada para esta combinação.")
                    continue

                x_sol = solution[variables[0]]
                y_sol = solution[variables[1]]

                if validate_solution(equations_sympy, variables, x_sol, y_sol):
                    display_results(x_sol, y_sol, variables[0].name, variables[1].name, profit_expr)
                else:
                    print("Esta operação não possui uma solução viável!")

            except Exception as e:
                print(f"Erro ao resolver equações: {e}")

def validate_solution(equations: List[Eq], variables: tuple, x_sol: float, y_sol: float) -> bool:
    """
    Valida se a solução satisfaz todas as restrições.
    
    Args:
        equations: Lista de equações
        variables: Tupla de variáveis
        x_sol: Solução para primeira variável
        y_sol: Solução para segunda variável
    
    Returns:
        bool: True se a solução é válida, False caso contrário
    """
    for eq in equations:
        substitution = eq.lhs.subs({variables[0]: x_sol, variables[1]: y_sol})
        if substitution > eq.rhs:
            return False
    return True

def display_results(x_sol: float, y_sol: float, var1_name: str, var2_name: str, profit_expr: str) -> None:
    """
    Exibe os resultados da otimização.
    
    Args:
        x_sol: Valor da primeira variável
        y_sol: Valor da segunda variável
        var1_name: Nome da primeira variável
        var2_name: Nome da segunda variável
        profit_expr: Expressão de lucro
    """
    print(f"Quantidade de {var1_name}: {eval(str(x_sol)):.2f}")
    print(f"Quantidade de {var2_name}: {eval(str(y_sol)):.2f}")
    
    profit_sympy = sympify(profit_expr)
    final_profit = profit_sympy.subs({symbols(var1_name): eval(str(x_sol)), 
                                    symbols(var2_name): eval(str(y_sol))})
    print(f"Lucro final: R${eval(str(final_profit)):.2f}")

def main():
    """Função principal para executar o resolvedor de programação linear."""
    var1_name = get_user_input("Digite o nome da primeira variável: ")
    var2_name = get_user_input("Digite o nome da segunda variável: ")
    print("=-" * 27)

    while True:
        try:
            num_equations = int(get_user_input("Digite o número de equações: "))
            if num_equations > 0:
                break
            print("Por favor, insira um número positivo.")
        except ValueError:
            print("Valor inválido, por favor insira um número inteiro positivo!")

    print("=-" * 27)
    equations = []
    for i in range(num_equations):
        equation = get_user_input(
            f"Digite a equação {roman.toRoman(i + 1)} no formato 'ax + by = c': ",
            validate_equation,
            "Formato de equação inválido. Tente novamente."
        )
        equations.append(equation)

    print("=-" * 27)
    profit_function = get_user_input(
        "Digite a função de lucro no formato ax + by: ",
        validate_profit_function,
        "Formato de função de lucro inválido. Tente novamente."
    )

    # Process equations
    variables = symbols(f'{var1_name} {var2_name}')
    equations_sympy = []
    
    for eq in equations:
        try:
            left, right = process_equation(eq)
            equations_sympy.append(Eq(sympify(left), sympify(right)))
        except Exception as e:
            print(f"Erro ao processar equação: {e}")
            return

    solve_equations(equations_sympy, variables, profit_function)

if __name__ == "__main__":
    main()
