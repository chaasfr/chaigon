import operator

def safe_eval(expression):
    ops = {
        '+': (1, operator.add),
        '-': (1, operator.sub),
        '*': (2, operator.mul),
        '/': (2, operator.truediv),
    }

    def tokenize(expression):
        tokens = expression.replace('(', '(').replace(')', ')').split()
        filtered_tokens = []
        for token in tokens:
            if token:
                filtered_tokens.append(token)
        return filtered_tokens

    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Empty Expression")

    values = []
    operators = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
            values.append(float(token))
        elif token in ops:
            precedence, _ = ops[token]
            while operators and operators[-1] in ops and ops[operators[-1]][0] >= precedence:
                op = operators.pop()
                if not values:
                    raise ValueError("Invalid Expression: Not enough values")
                val2 = values.pop()
                if not values:
                    raise ValueError("Invalid Expression: Not enough values")
                val1 = values.pop()
                values.append(ops[op][1](val1, val2))
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                if not values:
                    raise ValueError("Invalid Expression: Not enough values")
                val2 = values.pop()
                if not values:
                    raise ValueError("Invalid Expression: Not enough values")
                val1 = values.pop()
                values.append(ops[op][1](val1, val2))
            if operators:
                operators.pop()  # Remove '('
            else:
                raise ValueError("Unmatched parenthesis")
        else:
            raise ValueError("Invalid token: {}".format(token))

    while operators:
        if operators[-1] == '(':
            raise ValueError("Unmatched parenthesis")
        op = operators.pop()
        if not values:
            raise ValueError("Invalid Expression: Not enough values")
        val2 = values.pop()
        if not values:
            raise ValueError("Invalid Expression: Not enough values")
        val1 = values.pop()
        values.append(ops[op][1](val1, val2))

    if len(values) != 1:
        raise ValueError("Invalid expression")

    return values[0]
