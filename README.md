# Otimização Linear - Método Analítico

Um programa Python para resolver problemas de otimização linear usando o método analítico, ideal para problemas com duas variáveis.

## Funcionalidades

- Resolve sistemas de equações lineares com duas variáveis
- Calcula o lucro máximo baseado em uma função objetivo
- Valida entrada de equações e funções
- Suporta nomes de variáveis personalizados
- Exibe resultados intermediários do processo de resolução

## Requisitos

- Python 3.6+
- Bibliotecas necessárias:
  - sympy
  - roman

Instale as dependências usando:
```bash
pip install sympy roman
```

## Como Usar

1. Execute o programa:
```bash
python analitico.py
```

2. Siga as instruções:
   - Digite os nomes das variáveis (ex: x, y)
   - Informe o número de restrições
   - Digite as equações no formato "ax + by = c"
   - Digite a função de lucro no formato "ax + by"

### Exemplo

```
Digite o nome da primeira variável: x
Digite o nome da segunda variável: y
Digite o número de equações: 3
Digite a equação I: 2x + y = 100
Digite a equação II: x + y = 80
Digite a equação III: x + 2y = 120
Digite a função de lucro: 3x + 2y
```

## Estrutura do Código

- `validate_equation()`: Valida o formato das equações
- `validate_profit_function()`: Valida o formato da função de lucro
- `get_user_input()`: Gerencia entrada do usuário com validação
- `process_equation()`: Processa e formata equações para o solver
- `solve_equations()`: Resolve o sistema de equações
- `validate_solution()`: Verifica se a solução atende às restrições
- `display_results()`: Exibe os resultados finais

## Limitações

- Suporta apenas problemas com duas variáveis
- As equações devem estar no formato padrão (ax + by = c)
- A função de lucro deve estar no formato padrão (ax + by)

## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
