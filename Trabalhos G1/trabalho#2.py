def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def evaluate_rpn(expression):
    stack = []

    for token in expression.split():
        if isfloat(token):
            stack.append(float(token))
        elif token in {'+', '-', '*', '/', '^'}:
            if len(stack) < 2:
                raise ValueError("Expressão inválida: operador sem operandos suficientes")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Expressão inválida: divisão por zero")
                stack.append(operand1 / operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
        else:
            raise ValueError("Expressão inválida: token desconhecido")

    if len(stack) != 1:
        raise ValueError("Expressão inválida: formato inválido")
    return stack[0]


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operators = []

    for token in expression.split():
        if isfloat(token):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Descarta o '('
        elif token in precedence:
            while operators and precedence.get(operators[-1], 0) >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)
        else:
            raise ValueError("Expressão inválida: token desconhecido")

    while operators:
        output.append(operators.pop())

    return ' '.join(output)


expressions = ["( 2 + 3 ) * 4",
               "10 - 5 + 2",
               "8 * 6 / 2",
               "12 / ( 3 * 2 )",
               "2 ^ 3",
               "5 ^ ( 2 + 1 )",
               "( 2 + 3 ) * 4 - 5",
               "10 / ( 5 - 2 ) ^ 2",
               "( 2 + ( 3 * 4 ) ) - 5",
               "10 / ( ( 5 - 2 ) ^ 2 ) ",
               ]

for expression in expressions:
    polish_notation = infix_to_postfix(expression)
    print()
    print(expression)
    print("Notação polonesa reversa:", polish_notation)
    try:
        result = evaluate_rpn(polish_notation)
        print("Resultado da expressão:", result)
    except ValueError as e:
        print("Erro ao avaliar a expressão:", e)
