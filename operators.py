import random
import math

# = affectation
variable = 123
# + addition
variable = 123 + 42
variable = variable + 42
variable += 42
# - soustraction

variable -= 42
# / division

variable = 123/42
# // division entiere

variable = 123//42
# % modulo

variable = 4%3
variable = random.randint(1, 100)
print(variable % 2)
# * multiplication
variable = 123*42
# ** puissance
variable = 2 ** 6
# ^ puissance mais pas en python
# sqrt() racine carré
variable = math.sqrt(4)
variable = 4**0.5


# ++ et --  n existe pas en python utiliser += et -=

# égalité

results = 1==1
print(results)

# les grandeurs
results = 123 < 42
print(results)

# plus grand ou egal

results = 123 <= 42
print(results)

# inégalité

results = 123 != 42
print(results)
