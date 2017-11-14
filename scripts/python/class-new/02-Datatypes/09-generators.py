def fib(n):
    pre, cur, nxt, i = -1, 1, 0, 1

    while (i <= n): 
        prev = cur
        cur =  nxt
        nxt = prev + cur
        yield cur
        i = i + 1

n = 20
#for (....)
# st[i] = fib(n)

fib(n)
#my_fib_list = fib(n)

for f in fib(n):
    print f

