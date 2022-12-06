# l'opérateur d'affectation = permet d'injecter une valeur dans une variable.

my_number1 = 123
my_number2 = -42

print(my_number1)
print(type(my_number1))

print(my_number2)

# float

my_number3 = 3.14
my_number4 = -2.71
# 0.0 ou 0. ou .0
my_number5 = 0.0

print(my_number3)
print(type(my_number3))

print(my_number4)
print(my_number5)

# string

my_text1 = "Ceci est un string"
my_text2 = 'la meme chose'

print(my_text1)
print(my_text2)

#\ carac d'echapement
#\ saut de ligne

my_text3 ="abc\ndef"
print(my_text3)
print("\\")
my_text4 = """abc
def
ghi"""
print(my_text4)


#bool

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# none

my_none = None
print(my_none)
print(type(my_none))


#permutation de variable
a=123
b=42

a, b = b, a

print(a)

c=0
c=a
a=b
b=c

print(a)

# transtypage

variable = "123"
variable = int(variable)
print(type(variable))

variable = float(variable)

variable = 3.14
variable = int(variable)

variable = 3.14
variable = str(variable)

#
variable = 2.71
# recuperer la partie entiere dans a
a = int(variable)
print(a)
# recuperer la partie apres la virgule dans b
b = variable-a
print(b)