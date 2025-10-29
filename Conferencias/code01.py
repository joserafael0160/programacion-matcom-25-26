# --- Calculadora Completa ---
# Este programa demuestra los conceptos de entrada de datos, conversión de tipos y operaciones.

# --- 1. ENTRADA DE DATOS ---
# Mostramos un mensaje de bienvenida al usuario.
print("--- Calculadora de Operaciones Básicas ---")
print("Por favor, introduce dos números para ver todas las operaciones entre ellos.")

# Pedimos el primer y segundo número.
# La función input() siempre devuelve el dato como un string (texto).
input_a_str = input("Introduce el primer número (a): ")
input_b_str = input("Introduce el segundo número (b): ")


# --- 2. PROCESO (Conversión de Tipos) ---
# Convertimos los strings a números flotantes (float) para poder hacer cálculos.
# Usamos float() en lugar de int() para que la calculadora funcione con decimales.
a = float(input_a_str)
b = float(input_b_str)


# --- 3. SALIDA (Mostrar Resultados) ---
# Usamos f-strings para formatear e imprimir los resultados de forma clara.

# Sección de Operaciones Aritméticas
print("\n--- Operaciones Aritméticas ---")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}  (División entera)")
print(f"{a} % {b} = {a % b}  (Módulo o residuo)")
print(f"{a} ** {b} = {a ** b} (Potencia)")

# Sección de Operaciones de Comparación
# El resultado de una comparación siempre es un valor booleano (True o False).
print("\n--- Operaciones de Comparación ---")
print(f"{a} == {b} (¿Es igual?) = {a == b}")
print(f"{a} != {b} (¿Es diferente?) = {a != b}")
print(f"{a} > {b}  (¿Es mayor que?) = {a > b}")
print(f"{a} < {b}  (¿Es menor que?) = {a < b}")
print(f"{a} >= {b} (¿Es mayor o igual que?) = {a >= b}")
print(f"{a} <= {b} (¿Es menor o igual que?) = {a <= b}")

print("\n¡Cálculos finalizados!")
