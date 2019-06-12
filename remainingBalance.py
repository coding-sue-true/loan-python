def calculateRemainingBalance(principal, annual_interest_rate, duration, number_of_payments):
    r = ((annual_interest_rate/100)/12)
    n = duration * 12
    p = number_of_payments
    if annual_interest_rate == 0:
        return principal-number_of_payments*(principal/n)
    top = (((1+r)**n) - ((1+r)**p))
    bottom = (((1+r)**n) - 1)
    remainingBalance = principal * (top/bottom)

    print(remainingBalance)
    return remainingBalance


calculateRemainingBalance(1000.0, 4.5, 5, 12)
