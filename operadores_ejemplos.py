#Operadores
#*****************************************//************************************************
#Operadores Aritméticos
# + 	Realiza Adición entre los operandos 	12 + 3 = 15
# - 	Realiza Substracción entre los operandos 	12 - 3 = 9
# * 	Realiza Multiplicación entre los operandos 	12 * 3 = 36
# / 	Realiza División entre los operandos 	12 / 3 = 4
# % 	Realiza un módulo entre los operandos 	16 % 3 = 1
# ** 	Realiza la potencia de los operandos 	12 ** 3 = 1728
# // 	Realiza la división con resultado de número entero 	18 // 5 = 3
#************************//****************************
a = 7
b = 2
print("Operadores aritméticos")
#Operador suma
print('El resultado de la suma es:',a+b)
#Operador resta
print('El resultado de la resta es:',a-b)
#Operador producto
print('El resultado del producto es:',a*b)
#Operador division
print('El resultado de la division es:',a/b)
#Operador módulo
print('El resultado del módulo es:',a%b)
#Operador division entera
print('El resultado de la division entera es:',a//b)
#Operador potencia
print('El resultado de la potencia es:',a**b)
#************************//***************************
#Operadores Relacionales o de comparaccion
#Operador 	          Descripción 	                                                                Uso
# > 	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha 	12 > 3 devuelve True
# < 	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda 	12 < 3 devuelve False
# == 	Devuelve True si ambos operandos son iguales 	12 == 3 devuelve False
# >= 	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha 	12 >= 3 devuelve True
# <= 	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda 	12 <= 3 devuelve False
# != 	Devuelve True si ambos operandos no son iguales 	12 != 3 devuelve True
#*************************//***************************
print("Operadores de comparación")
#> Mayor a>b a mayor q b
print(a>b)
#< Menor a<b a menor q b
print(a<b)
#== Igual a==b a igual b
print(a==b)
#>= Mayor igual a>=b a myor igual q b
print(a>=b)
#<= Menor igual a<=b a menor igual q b
print(a<=b)
#!= Desigual a!=b a distinta de b
print(a!=b)
#************************//****************************
#Operadores Lógicos
#Operador 	 Descripción 	                           Uso
# and 	Devuelve True si ambos operandos son True 	a and b
# or 	Devuelve True si alguno de los operandos es True 	a or b
# not 	Devuelve True si alguno de los operandos False 	not a
#************************//****************************
#Operadores de asignación
#Operador 	        Descripción
# = 	a = 5. El valor 5 es asignado a la variable a
# += 	a += 5 es equivalente a a = a + 5
# -= 	a -= 5 es equivalente a a = a - 5
# *= 	a *= 3 es equivalente a a = a * 3
# /= 	a /= 3 es equivalente a a = a / 3
# %= 	a %= 3 es equivalente a a = a % 3
# **= 	a **= 3 es equivalente a a = a ** 3
# //= 	a //= 3 es equivalente a a = a // 3
# &= 	a &= 3 es equivalente a a = a & 3
# |= 	a |= 3 es equivalente a a = a | 3
# ^= 	a ^= 3 es equivalente a a = a ^ 3
# >>= 	a >>= 3 es equivalente a a = a >> 3
# <<= 	a <<= 3 es equivalente a a = a << 3
#****************************//************************
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49
x=a; x&=b;  print("x&=", x)  # 2
x=a; x|=b;  print("x|=", x)  # 7
x=a; x^=b; print("x^=", x)   # 5
x=a; x>>=b; print("x>>=", x) # 1
x=a; x<<=b; print("x<<=", x) # 28
#****************************//************************
#Operadores Bit a Bit
#Operador 	                     Descripción 	                  Uso
# & 	Realiza bit a bit la operación AND en los operandos 	a & b = 2 (Binario: 10 & 11 = 10)
# | 	Realiza bit a bit la operación OR en los operandos 	a | b = 3 (Binario: 10 | 11 = 11)
# ^ 	Realiza bit a bit la operación XOR en los operandos 	a ^ b = 1 (Binario: 10 ^ 11 = 01)
# ~ 	Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando 	~a = -3 (Binario: ~(00000010) = (11111101))
# >> 	Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha 	a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
# << 	Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha 	a << b = 16 (Binario: 00000010 << 00000011 = 00001000)
#***************************//*************************
#Operadores de Pertenencia
# Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
# in y not in son operadores de pertenencia.
# in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
# not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
#***************************//*************************
z = [1,2,3,4,5]
#Esta 3 en la lista z?
print(3 in z) # Muestra True 
#No está 12 en la lista z?
print (12 not in z) # Muestra True
str = "Hello World"
#Contiene World el string str?
print("World" in str) # Muestra True
#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print("world" in str)  # Muestra False  
print("code" not in str) # Muestra True
#***************************//**************************
#Operadores de Identidad
#Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
# is y is not son operadores de identidad.
# is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.
# is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.
# Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
k = 3
l = 3  
o = 4
print(k is l)  # muestra True
print(k is not l)  # muestra False
print(k is not o)  # muestra True

u = 1
i = u
r = i
print(r is 1) # muestra True
print(r is u)# muestra True

str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print(str1 is str2) # muestra True
print("Code" is str2) # muestra False

s = [10,20,30]
m = [10,20,30]

print(s is m)  # muestra False (ya que las listas son objetos mutables en Python)  