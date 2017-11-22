
def factorial(n):
    print("n :", n)
    
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

n = 5
t = factorial(n)
print(t)
