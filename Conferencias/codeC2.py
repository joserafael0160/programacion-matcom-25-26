day = int(input("Día: "))
month = int(input("Mes: "))
year = int(input("Año: "))

# Vamos a utilizar esta variable para guardar el resultado y
# aprovechar el valor por defecto de False
valid = False

# Separamos el caso que más ruido causa, hay múltiples formas de separarlo
if month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # Note que aquí igualamos contra la condición directamente
        valid = day > 0 and day <= 29
        # Podemos hacer esto porque el valor que nos va a interesar
        # guardar es justamente True si la condición es True, si la
        # condición es falsa nos quedaremos con el valor por defecto
        #
        # Esto es equivalente a escribir
        # if day > 0 and day <= 29:
        #    valid = True
        # else:
        #    valid = False     # Y esta línea es innecesaria
        #
    else:
        # Aquí aplicamos la misma idea
        valid = day > 0 and day <= 28
else:
    if month <= 7:
        # Aquí está el truco de la fórmula con el módulo
        #
        # Si el mes es par month%2 da 0 -> 30+0=30 debería tener
        # 30 días
        #
        # Si el mes es impar month%2 da 1 -> 30+1=31 debería
        # tener 31 días
        if day <= 30 + month % 2 and day > 0:
            valid = True
    elif month <= 12:
        # Aquí de usamos también el truco pero los valores se
        # invierten, por eso empezamos en 31 y restamos
        #
        # Si el mes es par month%2 da 0 -> 31-0=31 debería tener
        # 31 días
        #
        # Si el mes es impar month%2 da 1 -> 31-1=30 debería tener
        # 30 días
        if day <= 31 - (month % 2) and day > 0:
            valid = True

# Aquí sintaxis extra. Además del if-else como instrucción con
# bloques de código asociados, existe una expresión if.
#
# boolean_expression if condition else boolean_expression
#
# Esta expresión da como resultado el valor de la izquierda si la
# condición da True, sino, da como resultado el valor de la
# derecha
print(f"La fecha {"" if valid else "no "}es válida")
