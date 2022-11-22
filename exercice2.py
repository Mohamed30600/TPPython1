import math
import random
import time

count=0

print("-----------------------------Tableau et Nombre-------------------------")

notes = [12,15,17,8,10,5,16,19]

def moyenneNote(tab):
    return (sum(tab)/len(tab))

print("la moyenne des note de la liste est :", moyenneNote(notes),"\n")
print("le nombre d'occurence la liste est :" ,len(notes))


#note superieu a 10
def NoteSupDix(tab):
    for i in tab:
      if i>=10:
        global count
        count= count+1
    return count

NoteSupDix(notes)
print (" le nbr de note supereiru a 10 et:",count)

#valeur maximale du tableau 


def maxValueNote(tab):
    max_value=None
    for i in tab:
        if(max_value is None or i>max_value):
            max_value=i
    print(" la note maximale dan le tableau notes est:",max_value)


maxValueNote(notes)

#---------------------------------tester si un element est present-+--------------------------------
a=12
def isElementpresent(tab) :
    if  a in tab:
        print (" la note",a," est presente dans la liste des notes ")
    else:
        print("la note",a, "n'est pas presente dans la liste de notes")

isElementpresent(notes)

print (notes)
print("-----------------------------tableau pour un taille donnee n------------")


def creation_TableauNelements(n):
    tableau =[random.randint(0,20) for i in range(n)]
    return (tableau)

#---------------------------tableau a 8 elements et temp dinsctruction du bloc 
start=time.time()
creation_TableauNelements(8)
end =time.time()
tempExecution = end-start
print (f'le temp execution pour creez un tableau aléatoire de n element est: {tempExecution:.2}ms') 

print("-------------------------temp necessaire pour calculer moyenne et rechercher un element sur de grand tableaux")

#-----------------------------------------calculer moyenne tableau de n element-----------------------------------------


tableau1=creation_TableauNelements(500)
start =time.time()
moyannetableau1=moyenneNote(tableau1)
end =time.time()
diffTemp = end-start
print (f'le temp execution pour creez un tableau aléatoire de n element est: {diffTemp:.2}ms')
print( "la moyenne tableau 1 est :",moyannetableau1)


#----------------------------Rechercher un element table de n element---------------------------------------

tableau2 =creation_TableauNelements(6)
print (tableau2)
start = time.time()
#element a trouver 12
isElementpresent(tableau2)
end=time.time()





