### Question 3
a, b="a",42
c, d, e=True,"d", 23
print(a < d and c)
print(c or b < e)

print(a)
print(b)


### Question 4
for i in range(5):
    print("x"*(5-i))


### Question 8
def f(a,x):
   a[0], x=1, 1
a=[3,4]
x=2
f(a,x)
print(a[0],x)


### Question 9
a = [3,4] + [[1,2]]*2
print(a[-1][-1])



### Question 13
def g(a,b):
    print("toto")

print(type(g(0,2)))


### Question 15
def f(x,y):
    res = 1
    for i in range(x):
        res *= y
    return res

print(f(3,5))
print(3**5)
print(5**3)


### Question 19
def ff(x,y=1,z=2):
    return (x,y,z)
print(ff(1,2,3))


### Question 20
def fff(x,y=2,z):
    return x + y + z

res = fff(3, z=4)
print(res)

def F(n):
    cpt = 0
    while n != 1:
        cpt += 1
        n = n // 2
    return cpt
print(F(18))
