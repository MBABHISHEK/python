def fibonacci(n):
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 0:
        return "N must be a positive integer."

    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a value for N: "))

result = fibonacci(n)

if isinstance(result, str):

    print("Invalid Input-",result)
else:
    print("The", n, "th Fibonacci number is:", result)
    
    
    
    
    
    
