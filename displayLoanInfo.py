import monthlyPayment
import remainingBalance


totalLoanAmount = input("Please insert your total loan amount: ")
interestRate = input("Please insert your annual interest rate (percent): ")
loanDurationInYears = input(
    "Please insert your total loan duration in years: ")

monthlyPaymentFinal = monthlyPayment.calculateMonthlyPayments(
    totalLoanAmount, interestRate, loanDurationInYears)

print("LOAN AMOUNT: " + str(totalLoanAmount) +
      " INTEREST RATE(PERCENT): " + str(interestRate))
print("DURATION (YEARS): " + str(loanDurationInYears) +
      " MONTHLY PAYMENT " + str(int(monthlyPaymentFinal)))

for year in range(1, loanDurationInYears+1):
    print("YEAR: " + str(year) +
          " BALANCE: " + str(int(remainingBalance.calculateRemainingBalance(totalLoanAmount, interestRate, loanDurationInYears, year*12))) +
          " TOTAL PAYMENT: " + (str(int(monthlyPaymentFinal*(year*12)))))
