#( I ) is the interest earned,
#( P ) is the principal amount (initial investment),
#( R ) is the annual interest rate (as a decimal),
#( T ) is the time the money is invested for in years.

principal = 1000
rate = 0.05
time = 3

def interest_earned(P, R, T) :
    I = P * R * T
    print("The simple interest is: ", I)

interest_earned(principal, rate, time)