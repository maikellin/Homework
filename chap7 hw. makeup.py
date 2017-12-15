def days_in_month(name):
    """takes a month name and returns the number of days in that month"""
    if name == "January" or name == "March" or name == "May" or name == "July" or name == "August" or name == "October" or name == "December":
        return 31
    elif name == "February":
        return 28
    elif name == "April"  or name == "June"  or name == "November":
        return 30

def hours_in(secs):
    return secs//3600

def minutes_in(secs):
    return secs%3600//60

def seconds_in(secs):
    return secs%3600%60

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def is_odd(n):
    if is_even(n):
        return False
    else:
        return True
#3   if n%2 == 0:
#      return False
#    else:
#        return True

def is_factor(f,n):
    if n%f == 0:
        return True
    else:
        return False

def is_multiple(a,b):
    return is_factor(b,a)
    
def f2c(t):
    return round((t-32)/1.8,0)

def c2f(tc):
    return round((tc*1.8+32), 0)
    #if a%b == 0:
     #   return True
    #else:
     #   return False
     
def sqrt(n):
    approx = n/2
    while True:
        better = (approx + n/approx)/2
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


print("sqrt",sqrt(25.0))

def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



print(sqrt(25))