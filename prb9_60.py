x=int(input("Dati lungimea sirului A:"))
z=int(input("Dati lungimea sirului B:"))
y={str(input("Dati numerele sirului A:")) for i in range(x)}#list comprehension
c={str(input("Dati numerele sirului B:")) for g in range(z)}#list comprehension
print('intersectia:', y.intersection(c))
print('reuniunea:', y.union(c))
print('diferenta A/B:',y.difference(c))
print('diferenta B/A:',c.difference(y))