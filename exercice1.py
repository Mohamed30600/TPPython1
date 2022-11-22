import random

#-----------------------------------------affichage-----------------------------
print("-----------------------------AFFICHAGE---------------------------------\n")

j ="hello word"
print (12)
print ('salut christophe\n')
print ("voici l'afichage d'une variable avec j en parametre :",j)
#pour aller o pas a la lign on ajour \n a la fin de l instruction 
print("------------------------------Boucle While------------------\n")
#delcaration del a variable
compteur=0
#boucle compteur incrementer de 0 a 99
while  compteur<100:
  print ("le numero du compteur avec la boucle while est :",compteur)
  compteur=compteur+1
  print("\n")

#---------------------------BOUCLE FOR ET While---------------------------  
  
print("------------------------------Boucle For------------------\n")

for compteur2 in range(0,100,1):
    print ("le numero de comteur avec boucle for est :",compteur2)

#----------------------------TRacer un figure--------------------------------

print("-------------------Tracer un Carre-----------------------")
#afaire
print("-------------------Tracer un triangle-----------------------")


#---------------------------------Liste-----------------------------------

print("------------------------------LISTE-----------------------------")

listVide =[]
listElements =["pierre","outils","employes","fourniture","prix"]
print ("le nombre element dans la listeElement est :",(len(listElements)))
listElements.pop()
listElements.append("prix actualiser")
print ("voici la nouvelle liste avec le remplacement de l'element prix",listElements,"\n")

print("---------------------------affichage liste avec while----------------------------)")
i=0
while i< len(listElements) :
  print (listElements[i])
  i+=1

print("---------------------------affichage liste avec for----------------------------)")
for i in range(len (listElements)):
    print ("les elements du tableua sont:",listElements[i])

print("---------------------------affichage liste avec index----------------------------)")

print(listElements[0])
print(listElements[1])
print(listElements[2])
print(listElements[3])
print(listElements[4])


print("---------------------------Aleatoire----------------------------)")
listRandom=["paul","pierr","julie","alson","mohamed","jordan"]
#choixx aleatoire dans la liste listrandom
print (random.choice(listRandom))
#choix aleatoire chiffre siyue entre 4 inclus et 10 inclu
print ("chiffre aleatoire entre 2 borne 4 et 10 inclus:",random.randint(4,10))
#choix chiffre aleatoire situer en 4 non inclu et 10 non inclu
print ("chiffre aleatoire entre 2 borne 4 et 10 non inclus:",random.randrange(4,10))
#melande la liste listRandom
print("liste non modifier par random.shuffle",listRandom)
random.shuffle(listRandom)
print("liste modifier melange des elements:",listRandom)




