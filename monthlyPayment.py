def calculateMonthlyPayments(principal, annual_interest_rate, duration):
    r = ((annual_interest_rate/100)/12)
    n = duration * 12
    if annual_interest_rate == 0:
        return principal/n
    secondPart = (r * ((1+r)**n)) / ((1+r)**n - 1)
    monthlyPayment = principal * secondPart
    print(monthlyPayment)
    return monthlyPayment


calculateMonthlyPayments(1000.0, 4.5, 5)
