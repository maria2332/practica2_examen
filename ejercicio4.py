# En algunos países de la antigua Unión Soviética existía la creencia de los boletos de la
# suerte. Se creía que un billete de transporte de cualquier tipo traía suerte si la suma de los
# dígitos de la mitad izquierda de su número era igual a la suma de los dígitos de la mitad
# derecha. Aquí hay ejemplos de tales números:
# 003111 # 3 = 1 + 1 + 1
# 813372 # 8 + 1 + 3 = 3 + 7 + 2
# 17935 # 1 + 7 = 3 + 5 // si la longitud es impar, debes ignorar el número del medio al
# sumar las mitades.
# 56328116 # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
# Dichos boletos se comían después de usarlos o se recolectaban para fanfarronear.
# Su tarea es escribir una función luck_check(str), que devuelve true/Truesi el argumento es una
# representación decimal de cadena de un número de boleto de la suerte, o false/Falsepara
# todos los demás números. Debería arrojar errores para cadenas vacías o cadenas que no
# representan un número decimal.

#sumar los digitos de la mitad izquierda y la mitad derecha
#si la longitud es impar, debes ignorar el numero del medio al sumar las mitades


def luck_check(str):
    if len(str) == 0:
        raise Exception('No puede ser una cadena vacía')
    if len(str) % 2 == 0:
        mitad_izquierda = str[0:len(str)//2]
        mitad_derecha = str[len(str)//2:]
    else:
        mitad_izquierda = str[0:len(str)//2]
        mitad_derecha = str[len(str)//2+1:]
    suma_izquierda = 0
    suma_derecha = 0
    for i in mitad_izquierda:
        suma_izquierda += int(i)
    for i in mitad_derecha:
        suma_derecha += int(i)
    if suma_izquierda == suma_derecha:
        return True
    else:
        return False

print(luck_check("003111"))