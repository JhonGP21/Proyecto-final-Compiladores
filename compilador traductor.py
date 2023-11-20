def translate_to_python(program):
    python_code = ""
    indentation_level = 0

    lines = program.split('\n')

    for line in lines:
        tokens = line.split()
        if not tokens:
            continue

        if tokens[0] == "INICIO":
            python_code += "while True:\n"
            indentation_level += 1
        elif tokens[0] == "FIN":
            indentation_level -= 1
        elif tokens[0] == "SI":
            condition = ' '.join(tokens[1:-1])
            python_code += "    " * indentation_level + f"if {condition}:\n"
            indentation_level += 1
        elif tokens[0] == "ENTONCES":
            python_code += "    " * indentation_level + "    " + ' '.join(tokens[1:]) + ":\n"
        elif tokens[0] == "SINO":
            indentation_level -= 1
            python_code += "    " * indentation_level + "else:\n"
            indentation_level += 1
        elif tokens[0] == "MIENTRAS":
            condition = ' '.join(tokens[1:-1])
            python_code += "    " * indentation_level + f"while {condition}:\n"
            indentation_level += 1
        elif tokens[0] == "HACER":
            indentation_level -= 1
        elif tokens[0] == "LEER":
            variable = tokens[1]
            python_code += "    " * indentation_level + f"{variable} = input()\n"
            python_code += "    " * indentation_level + f"{variable} = int({variable})\n"
        elif tokens[0] == "ESCRIBIR":
            expression = ' '.join(tokens[1:])
            python_code += "    " * indentation_level + f"print({expression})\n"

    return python_code

# Ejemplo de uso:
pseudocode_program = """
INICIO
ESCRIBIR "Introduzca un numero mayor a 10"
LEER x
MIENTRAS x <= 10 HACER
    ESCRIBIR "El número es inválido ya que es menor a 10"
    LEER x
FIN
MIENTRAS x > 10 HACER
    ESCRIBIR "El numero es mayor a 10"
    LEER x
FIN
"""

python_code = translate_to_python(pseudocode_program)
print(python_code)
