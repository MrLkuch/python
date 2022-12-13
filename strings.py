

#heredoc string

my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmulti-ligne\nabc\nfoo\nbar"
print(my_text2)



my_number1 = 123
# interpolaton avec un f-string
my_text3 = f"Nombre = {my_number1}"
print(my_text3)

# interpolation avec une heredoc f-string
my_text4 = f"""
Le nombre
est
{my_number1}"""
print(my_text4)

# afficher des accolades dans une heredoc string
my_text5 = f"""
{{
foo
}}
{{bar}}"""
print(my_text5)

my_number2 = 3.14
my_text6 = "le nombre PI est " + str(my_number2) + "\nEt le nombre d'or est 1.618"
print(my_text6)

# tronquer un float dans une interpolation
# .4f veux dire 4 chiffres apres la virgule

my_number3 = 1/3
my_text7 = f"1/3 ~= {my_number3:.4f}"
print(my_text7)

# les interpolations acceptent les expressions

my_text8 = f"1 + 1 = {1+1}"
print(my_text8)



# l'ecriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un
    
    name str indique le nom de la personne à saluer
    return None
    """
    print(f"Salut {name}")

hello("lucas")

my_text9 ="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est ducimus consectetur nostrum, aliquam ea molestiae!"
#longueur d'une str
my_number4 = len(my_text9)
print(my_number4)

# trouve la position d'une str dans une autre str
my_number5 = my_text9.find('dolor')
print(my_number5)


#compte le nombre d'occurence d'une str dans uen autre str
my_number6 = my_text9.count('Lorem')
print(my_number6)

# remplace non permanant d'un str par un autre
print(my_text9.replace('Lorem', 'Foo'))

# éclate une str en liste en utilisant l'espace comme caractere de separation.
my_list1 = my_text9.split()
print(len(my_list1))

# acces en lecture au 0eme caractere de la str
print(my_text9[0])

# acces en lecture du 0eme au 10eme caractere de la str
print(my_text9[0:10])

# du 10eme a la fin
print(my_text9[10:])

# acces en lecture par la fin de la str
print(my_text9[::-1])

# acces en lecture 1 caractere sur 2 de la str
print(my_text9[::2])


def nbMot(texte: str)-> int:
    nb = 1
    for i in range (len(texte)):
        if texte[i] == ' ' and texte[i+1] != " ":
            nb+=1
            i+=1
    return print(nb)

textex ="Lorem ipsum dolor sit"
nbMot(textex)

