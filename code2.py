def lone_sum(a, b, c):
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c

    
     ------------------------------------------------

# First we need keep in mind that if, elif, and else statements should be executed in order.
# For example on this code the first statement that we need to executate is the if because "if" test the expression
# for that reason we need on this code we need to executate if with a==b and a==c and b==c,
#because is the statement which will test the expression if is true or false with the rest of the statement elif, and else.

def lone_sum(a, b, c):
    if a == b and a == c and b == c: # This will test the expression for false or true
        return 0 # This return make that statement of the function to exit and back a value to its caller, in this case 0,
                 #because we have no other value before it.
    elif a >= b: # if a is greater or equal to b, will print the value of c, which is on return
        return c
    elif b == c: # if b equal to c will print the value of a, which represent the return
        return a
    elif a == c:  # if a equal to c will print the value of c, which represent the return
        return c
    else:
        return a + b + c # else will print the sum of the above return.


print(lone_sum(1, 2, 4)) # here we can use different numbers, in this case 1 is a, b is 2 and 4 is c
                         #Therefore this create the addition of a+b+c= 7
