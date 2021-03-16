note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

liste1 = (i for i in notes if i[0] ='eleve1')
liste2 = (i for i in notes if i[0] ='eleve2')
moyenne1 = sum(x[2] for x in liste1)/len(liste1)
moyenne_maths_1 = sum(x[2] for x in liste1 if x[1] = 'math')/len(liste1 if x[1] = 'math')


def moyenne_tuples():
  

