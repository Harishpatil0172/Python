### @1 Write a function thet accepts 3 variables and return the sum of these variables,
### if values are equal then return two times their sum
def sum_num(a,b,c):
    if a==b==c:
        return 2*(a+b+c)
    else:
        return a+b+c
 sum_num(1,2,3)
     
 ### @2 Square root of number
 def sqrt(num):
    x=(format(num**0.5,'0.3f'))
    return (float(x))

sqrt(8)

###@3 Quotient and Remainder
