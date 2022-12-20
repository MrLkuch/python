# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
longueur=0
index=0
for i in range(len(my_list)):
    if len(my_list[i])>longueur:
        longueur=len(my_list[i])
        index = i


print(index, my_list[index], longueur)