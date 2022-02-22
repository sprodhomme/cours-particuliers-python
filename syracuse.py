import datetime

def syracuse(n):
    liste=[n]
    while n>1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        liste.append(n)
    return liste

#print(syracuse(3))

def testeConjecture(n_max):
    resultat = True
    for n in range(2,n_max):
        if syracuse(n)[-1]!=1:
            resultat = False
    return resultat

n_max=int(input("n_max"))
print(syracuse(n_max))

duree = datetime.datetime.now()
#execution d'une longue fonction
print(testeConjecture(n_max))
duree = datetime.datetime.now() - duree

print(duree)
