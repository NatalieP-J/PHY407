def f(x):
    return x**4 - 2*x + 1

N = 1000
a = 0.0
b = 2.0
h = (b-a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)

i = h*s
print(i)
print (i-4.4)/4.4