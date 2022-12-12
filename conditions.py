import random


if True:
    print("la condition est vraie")
    print("ce code est exécuté")

if False:
    print("la condition est fausse")
    print(" ce code n'est pas exécuté")


conditions_vente = False

if conditions_vente:
    print("a accepter les conditions")

else:
    print("n'a pas accepter les conditions")

if not conditions_vente:
    print("n'a pas accepter les conditions")
else:
    print("a accepter les conditions")


emails = random.randint(0, 3)

if emails == 1:
    print("Vous avez un nouveau mail.")

elif emails > 1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")


windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

print(f'{windows_closed = }')
print(f'{electricity_off = }')


if windows_closed and electricity_off:
    print("fenetres fermées")
    print("elec coupée")

elif not windows_closed and electricity_off:
    print("les fenetres ne sont pas fermées")
    print("elec coupée")

elif windows_closed and not electricity_off:
    print("fenetres fermées")
    print("l'elec n'est pas coupée")

else:
    print("les fenetres ne sont pas fermées")
    print("l'elec n'est pas coupée")



bank_card = True
cash = True

if bank_card or cash:
    print("on a un moyen de paiement")

    if bank_card or not cash:
        print("carte")

    if not bank_card or cash:
        print("cash")

else:
    print("aucune moyen de paiement")



ticket = True

vip = False

registration = False

if (ticket or vip) and registration:
    print("Access authorized")

else:
    print("Access denied")




product_count = 15;

if product_count > 20:
    print("plus de 20 articles")
elif 5 < product_count <= 20:
    print("plus de 5 articles")
elif 0 < product_count <= 5:
    print("plus de 0 articles")
else:
    print("plus d article")



if product_count > 20:
    print("plus de 20 articles")
elif 5 < product_count and product_count <= 20:
    print("plus de 5 articles")
elif 0 < product_count and product_count <= 5:
    print("plus de 0 articles")
else:
    print("plus d article")