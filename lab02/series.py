# Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

def fibonacci(n):
    if n< 0:
     return "you entered a negative value"
    elif n==0:
     return 0
    elif n==1:
     return 1
    else:
      return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))

# add a new function lucas that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.


def lucas(n):
    if n< 0:
     return "you entered a negative value"
    elif n==0:
     return 2
    elif n==1:
     return 1
    else:
      return lucas(n-1) + lucas(n-2)

print(lucas(8))

# Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

#def sum_series(printElement, firstElement=0, firstElement2=1):
   