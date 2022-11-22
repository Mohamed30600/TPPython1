
# ------------------------fonction qui renvoie la------------------------------------


tableauAlgoAvance = [18, 15, 2, 30, 14, 16, 95, 12, 5]


def index_minimum(tab, val1, val2):
    n = len(tab)
    val1Index = tab.index(val1)
    val2Index = tab.index(val2)
    min_value = tab[0]
    indice_min = 0
    for i in range(val1Index, val2Index):
        if tab[i] <= min_value:
            min_value = tab[i]
            indice_min = i
    print('indice du plu petit nombre entr l intervalle',
          val1, "et", val2, " est :", indice_min)
    return indice_min


index_minimum(tableauAlgoAvance, 18, 30)


# --------------------------Programme tri a bulle-------------------------------
print("programme tri a bulle")


def triABulle(tableau):
    n = len(tableau)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]


print("tableau non tier :", str(tableauAlgoAvance))
triABulle(tableauAlgoAvance)
print("tableau trier :", str(tableauAlgoAvance))


# def dichotomique (tableauTrier,val):
#     val1=0
#     longeurTableau = len(tableauTrier)-1
#     moitier =(val1+longeurTableau)//2
#     while val1 <= longeurTableau:

#         if(tableauTrier[moitier]==val):
#             return moitier
#         elif tableauTrier[moitier]>val:
#             val1 = moitier-1
#         else:
#             val1= moitier+1
#             moitier=(val1+longeurTableau)//2
#     return val1

# dichotomique(tableauTrier,30)
print("dichotomie tableau trier :")

tableauTrier = [2, 5, 12, 14, 15, 16, 18, 30, 95]


def recherche_dichotomique(element, liste_triee):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b:
        if liste_triee[m] == element:
            return m
        elif liste_triee[m] > element:
            b = m-1
        else:
            a = m+1
        m = (a+b)//2
    return a


print("position de la valeur par recherche dichotomie est :",
      recherche_dichotomique(2, tableauTrier))


# -----------------------insertion d un element  a un index-------------------------
#
tableauTrier.insert(2, 'element ajouter')
print("nouveau tableau avec element ajouter", tableauTrier)

# -------------------------autre methode de tri----------------------

print("tri par extraction")


def tri_par_selection(tab):
    for i in range(0, len(tab)-1):  # de 0 à n-2
            indmin = i
            for j in range(i+1, len(tab)):  # de i+1 à n-1, recherche du min
                if tab[j] < tab[indmin]:
                    indmin = j
            # echange de valeurs entre indmin et i
            tab[indmin], tab[i] = tab[i], tab[indmin]


print("tri par insertion")

def tri_par_insertion (tab) :
    for j in range(1,len(tab)) :
            elt_a_placer = tab[j]
            i = j - 1
            while i >= 0 and tab[i] > elt_a_placer :
                tab[i+1] = tab[i]
                i = i - 1
            tab[i+1] = elt_a_placer