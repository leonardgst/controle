note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

#Question 4.a)
liste1 = (i for i in notes if i[0] == 'eleve1')
moyenne1 = sum(x[2] for x in liste1)/len(liste1)
print(moyenne1)

#Question 4.b)
liste2 = (i for i in liste1 if  i[1] == 'math')
moyenne_maths_1 = sum(x[2] for x in liste2)/len(liste2)
print(moyenne_maths_1)

#Question 4.c)
def moyenne_tuples(valeur, eleve, matiere):
  eleve == None
  matiere == None
  list1 = (i for i in valeur if i[0] == eleve and i[1] == matiere)
  a = sum(x[2] for x in list1)/len(list1)
  return a

moyenne_tuples(notes, 'eleve1', 'math')
print(moyenne_tuples)


