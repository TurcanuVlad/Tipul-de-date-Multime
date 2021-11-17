from itertools import combinations
  
letters ={'A', 'B', 'C', 'D'}
  
m = combinations(letters, 4) 
d = [' '.join(i) for i in m]
y = combinations(letters, 3) 
a = [' '.join(i) for i in y]
x = combinations(letters, 2)
b= [' '.join(i) for i in x]  
v = combinations(letters, 1)
c= [' '.join(i) for i in v]

print('Submultimi cu 1 litera', c)

print('Submultimi cu 2 litere:', b)

print('Submultimi cu 3 litere:', a)

print('Submultimi cu 4 litere:', d)