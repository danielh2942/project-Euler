fib = 1
swap = 0
fib_prev = 1
total = 0

while fib < 4000000:
    swap = fib
    fib = fib + fib_prev
    fib_prev = swap
    if fib % 2 ==0:
        total += fib

print total
