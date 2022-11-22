
#-----------------------creation promotion tableau etudiant-----------------
tableauEtudiant = [
   
                   {   
                        "name":"pierre",
                        "prenom":"alfonse",
                        "promo":"data_engi",
                        "notes":[
                                    {
                                    "discipline":"math",
                                    "note":18
                                },
                                {
                                    "discipline":"francais",
                                    "note":18
                                },
                                {
                                    "discipline":"esv",
                                    "note":19
                                },
                        
                        ]
                    },
                        {
                            
                        "name":"mohamed",
                        "prenom":"hama",
                        "promo":"data_engi",
                        "notes":[
                                    {
                                    "discipline":"math",
                                    "note":9
                                },
                                {
                                    "discipline":"francais",
                                    "note":12
                                },
                                {
                                    "discipline":"esv",
                                    "note":14
                                },
                        
                        ]
                    },
                        {
                            
                        "name":"yvelybe",
                        "prenom":"pierrtee",
                        "promo":"data_engi",
                        "notes":[
                                    {
                                    "discipline":"math",
                                    "note":11
                                },
                                {
                                    "discipline":"francais",
                                    "note":8
                                },
                                {
                                    "discipline":"esv",
                                    "note":10
                                },
                        
                        ]
                    },
                        {
                            
                        "name":"celia",
                        "prenom":"dudu",
                        "promo":"Expert_it",
                        "notes":[
                                    {
                                    "discipline":"math",
                                    "note":2
                                },
                                {
                                    "discipline":"francais",
                                    "note":20
                                },
                                {
                                    "discipline":"esv",
                                    "note":15
                                },
                                
                        ]
                    },
                        {
                            
                        "name":"baba",
                        "prenom":"alfonse",
                        "promo":"Expert_it",
                        "notes":[
                                    {
                                    "discipline":"math",
                                    "note":6
                                },
                                {
                                    "discipline":"francais",
                                    "note":17
                                },
                                {
                                    "discipline":"esv",
                                    "note":5
                                },
                        
                        ]
                    },
              
            
                  ]



#---------------------------fonction moyenne etudiant------------
moyenne=0
def moyenneEtudian(nameStudent,promo):
    listeNoteEtudiant=[]
    for i in promo :
      if i["name"] == nameStudent :
        notesEleve= i["notes"]
        for j in notesEleve:
            note= j["note"]
            listeNoteEtudiant.append(note)
            moyenne= sum(listeNoteEtudiant)/len(listeNoteEtudiant)
    return("la moyenne de l'etuduant selectionner est ",moyenne)

print(moyenneEtudian("baba",tableauEtudiant))

#-------------------------moyenne de la promotion en fonction de la discipline----------------------

def moyennePromoDiscipline(disciplineSelected,promo):
    listeNotePromoDiscipline=[]
    for i in promo:
       notes=i['notes']
       for j in notes:
        if j["discipline"] ==disciplineSelected :
            note =j['note']
            listeNotePromoDiscipline.append(note)
            moyenne = sum(listeNotePromoDiscipline)/len(listeNotePromoDiscipline)
    #print ("la moyenne de la promo sur la disciple choisi est :",moyenne)
    return(moyenne)


moyennePromoDiscipline('esv',tableauEtudiant)

#-----------------------------etudiant moyenne maximal de la promo-----------------------------


