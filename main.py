print("Printing Fibonacci Number")

def fibonacciGenerator(limit):
    initial = 0
    secondInitial = 1
    print(initial)
    print(secondInitial)
    temp = 0
    loop = 0

    while(loop < limit - 2):
        temp = initial + secondInitial
        print(temp)
        initial = secondInitial
        secondInitial = temp
        loop += 1


print("Enter Range Of Fibonacci Series")
limit = int(input())
fibonacciGenerator(limit)

# Fibonacci In Recursion

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print("Enter The nth Term You Want To Find The Fibonacci of: ")
term = int(input())
print(fibonacci_rec(term))