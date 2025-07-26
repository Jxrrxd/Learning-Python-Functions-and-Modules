#Define a function using the 'def' keyword, followed by the functions name & parenthesis & a colon
#inside the parenthesis, specify any parameters the function should take

def greet(name):                        #when the function 'greet' is called, print out "Hello" and the persons name
    print(f"Hello, {name}")             #function prints a greeting to the user

greet("Jarred")                         #call the function and pass it a parameter(name)

def add(a,b):                           #name of the function and the two parameters
    return a+b                          #what we want to return- return a value

result = add(2,5)                       #create a variable, call the function, provide values for the two parameters
print(result)                           #print out the variable

def factorial(n):                       #factorial function uses recursion- the function calls itself- calculates the factorial of a number
    if n==0:                            #if n=0, return the value 1, otherwise, return the following
        return 1
    else:
        return n*factorial(n-1)
print(factorial(0))

def greet(name, greeting="Hello" ):     #functions can have operational values- have default values if you don't provide a value
    print(f"{greeting}, {name}")        #calling the greet function
greet("Jarred", "Prevening")            #call the function and parameter- after the comma you could change the greeting