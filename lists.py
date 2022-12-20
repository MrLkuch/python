fruits=["ananas", "banana", "cerise"]
print(fruits)

# acces en lecture au 0eme element de la liste
print(fruits[0])


# acces en ecriture au 0eme element de la liste
fruits[0] = "abricot"
print(fruits)
print(fruits[0])

index = 0
print(fruits[index])
index += 1
print(fruits[index])

#supprime un element
del fruits[1]
print(fruits)

#supprime le dernier element
#.pop(0) est equivalent a shift() dans les autres langages
last_element = fruits.pop()
print(last_element)
print(fruits)

#inserer un element

fruits.insert(1,'kiwi')
print(fruits)