x=int(input("Dati lungimea sirului A:"))
z=int(input("Dati lungimea sirului B:"))
y={int(input("Dati numerele sirului A:")) for i in range(x)}#list comprehension
c={int(input("Dati numerele sirului B:")) for i in range(z)}#list comprehension
print('intersectia:', y.intersection(c))
print('reuniunea:', y.union(c))
print('diferenta A/B:',y.difference(c))
print('diferenta B/A:',c.difference(y))