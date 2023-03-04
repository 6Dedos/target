def fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

num = int(input("Digite um número: "))
fib_seq = []
a, b = 0, 1
while b < num:
    fib_seq.append(b)
    a, b = b, a + b

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci: {fib_seq}")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci: {fib_seq}")
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def pertence_fibonacci(num):
    i = 0
    while True:
        termo = fibonacci(i)
        if termo == num:
            return True, i
        elif termo > num:
            return False, i-1
        else:
            i += 1

num = int(input("Digite um número: "))
pertence, n = pertence_fibonacci(num)
if pertence:
    print(f"O número {num} pertence à sequência de Fibonac5ci e é o termo de índice {n}.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci. O termo de índice {n} é {fibonacci(n)}.")
