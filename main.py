#challenge1
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
moy=sum(notes)/len(notes)
notes_sup = []
for note in notes:
    if note > moy:
        notes_sup.append(note)
print("Notes supérieures à la moyenne :", notes_sup)

#Challenge2
ch1 = "Le langage Python est très populaire"
ch2 = "Python est un langage puissant"

mots1=ch1.lower().split()
mots2=ch2.lower().split()

commun=list(set(mots1) & set(mots2))
print("Mots communs :", commun)

#challenge3
stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]
print("la liste initiale: ", stock)
nombres=[]
cara=[]
for i in stock:
    if isinstance(i, int):
        nombres.append(i)
    elif isinstance(i,str):
        cara.append(i)

print('les chaines de caracteres sont: ', cara)
print('les nombres sont: ', nombres)


nombres.sort(reverse=True)
cara.sort()

print(f'la liste des chaînes en ordre croissant (alphabétique): {cara}')
print(f'la liste des nombres en ordre décroissant: {nombres}')


#challenge4
l = list(input("entrer une chaine de caracteres"))
cc = input("entrer un caractere a chercher")
def recherchecara(cc, l):
    if cc in l:
        print("le caractere existe")
    else:
        print("le caractere n'existe pas")

recherchecara(cc,l)

#challenge5
ll = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
a=int(input("entrer un nombre a chercher son occurence dans la liste10"))
nbrr = 0

for i in ll:
    if i == a:
        nbrr += 1

print(f"L'element {a} apparait {nbrr} fois dans la liste.")


