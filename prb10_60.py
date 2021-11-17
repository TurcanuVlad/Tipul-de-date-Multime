from itertools import combinations
a={1, 2, 3, 4}
s= combinations(a, 3)
g= combinations(a, 2)
h= combinations(a, 1)
fr=combinations(a, 4)
y=[i for i in s]
l=[i for i in g]
k=[i for i in h]
p=[i for i in fr]
print('Submultimi cu 1 cifra', k)
print('Submultimi cu 2 cifre:', l)
print('Submultimi cu 3 cifre:', y)
print('Submultimi cu 4 cifre:', p)