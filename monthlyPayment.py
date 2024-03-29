def calculateMonthlyPayments(principal, annualInterestRate, duration):
    r = annualInterestRate/100/12
    n = duration * 12
    if annualInterestRate == 0 or r == 0:
        return principal/n
    secondPart = (r * ((1+r)**n)) / ((1+r)**n - 1)
    monthlyPayment = principal * secondPart
    return monthlyPayment


# calculateMonthlyPayments(1000.0, 4.5, 5)
# 18.6430192415
