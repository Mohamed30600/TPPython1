
import random
import time


tableau= [1,5,6,85,44,5,33,6,9,87,45,44,25,5]

#--------------------fonction copie-----------------------------

def copieTableau(tab):
    nouveauTableau= tab.copy()
    print("voici la copy du tableau est :",nouveauTableau)
    return nouveauTableau

copieTableau(tableau)


#-----------------------fonction inverse-----------------------
def inverseTableau(tab):
        inverseTableau= list(reversed(tab))
        print("voci le tableau inverser:",inverseTableau)
        return inverseTableau

inverseTableau(tableau)

#-----------------------------Produire tableau--------------------
tab=[]
def tableau_premier_entiers(n):
     global tab
     i=1
     while i<=n:
        tab.append(i)
        i+=1
     #print("tableau contruit de 1 a n:",tab)
     return tab

tableau_premier_entiers(10)
print("tableau contruit avec entier de 1 a n:",tab)

#-----------------------------------------------------------------------
def tableau_premier_entier_melanger(tab):
    tableauMelanger=random.sample(tab,len(tab))
    print ("le tableau melanger est :",tableauMelanger)
    return tableauMelanger

tableau_premier_entier_melanger(tab)

#-------------------------------------------------------------------------------
def tableau_premiers_entier_inverses(tab):
    tableauDecroissant= sorted(tab)
    print("tableau ranger du plus petit au plus grand :",tableauDecroissant)
    return tableauDecroissant
#---------------------------------------------------------------------------------
def ligne_dans_fichier(f,n,t):
    fichier =open(f,"a")
    fichier.write(n)
    fichier.write(" ")
    fichier.write(t)
    fichier.write("\n")
    fichier.close()


ligne_dans_fichier("fichiertest.txt","3","6")

diffTemp=0

#------------------------------------------------------------------------------------
def temp_tri_bulles(t):
    
    global diffTemp
    start = time.perf_counter()
    print("tableau tirer et copier",sorted(copieTableau(t)))
    end = time.perf_counter()
    diffTemp = end-start
    return diffTemp
    
    print (f'le temp execution pour creez un tableau aléatoire de n element est: ' ,end-start)


    
(temp_tri_bulles(tableau))
#-------------------------------------------------------------------------------------
def stats_melange (nmin,nmax,pas,fois):
    n=1
    while  n <= fois:
     tabs = random.sample(range(nmin, nmax), pas)
     n=n+1
     tmp=temp_tri_bulles(tabs)
     ligne_dans_fichier("tmpTableau.txt","temp :", str(diffTemp))
     
     
 
stats_melange(2,5,3,3)
#------------------------------------------------------------------------------------
def stats_ordonne (nmin,nmax,pas,fois):
    n = 1
    while n <= fois:
        tabs = sorted(random.sample(range(nmin, nmax), pas))
        print ("tableau trier time",tabs)
        n=n+1
        tmp = temp_tri_bulles(tabs)
        ligne_dans_fichier("tmpTableauordonne","temps",str(diffTemp))

stats_ordonne(2,5,3,5)
#----------------------------------------------------------------------------------------
def stats_inverse (nmin,nmax,pas,fois):
    n=1
    while n <= fois:
        tabs = sorted(random.sample(range(nmin, nmax), pas))
        tabsReverse= list(reversed(tabs))
        n=n+1
        print ("tableau trier en sene inverse ",tabsReverse)
        tmpReverse= temp_tri_bulles(tabsReverse)
        ligne_dans_fichier("tmpTableauordonneeReversed","temps",str(diffTemp))

stats_inverse(2,5,3,5)
