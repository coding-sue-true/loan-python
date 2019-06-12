def calculateRemainingBalance(principal, annualInterestRate, duration, numberOfPayments):
    r = annualInterestRate/100/12
    n = duration * 12
    p = numberOfPayments
    if annualInterestRate == 0 or r == 0:
        return principal-numberOfPayments*(principal/n)
    top = (((1+r)**n) - ((1+r)**p))
    bottom = (((1+r)**n) - 1)
    remainingBalance = principal * (top/bottom)
    # print(remainingBalance)
    return remainingBalance


# calculateRemainingBalance(1000.0, 4.5, 5, 12)
# 817.551280458
