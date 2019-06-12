# loan-python

## Part 1: Calculate monthly payments for a loan

Write a function that calculates and returns the monthly payments for a loan. This function accepts three parameters in the exact order (principal, annual_interest_rate, duration):

- principal: The total amount of loan. Assume that the principal is a positive floating point number.
- annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
- duration: number of years to pay the loan back. Assume that duration is a positive integer.
To calculate the amount of monthly payment for the loan you should use the following equation

𝑀𝑜𝑛𝑡ℎ𝑙𝑦𝑃𝑎𝑦𝑚𝑒𝑛𝑡 = 𝑃𝑟𝑖𝑛𝑐𝑖𝑝𝑎𝑙 ∗ 𝐫(1+𝐫)** 𝐧 / (1+𝐫)**𝐧 −1 


Where:
- r is the monthly interest rate (should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly). Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation: 𝑀𝑜𝑛𝑡ℎ𝑙𝑦𝑃𝑎𝑦𝑚𝑒𝑛𝑡 = 𝐏𝐫𝐢𝐧𝐜𝐢𝐩𝐚𝐥 / 𝐧

- n is the total number of monthly payments for the entire duration of the loan (Notice that n is equal to loan duration in years multiplied by 12).
Your function should return the monthly payment as a floating point number.


## Part 2: Calculate the remaining balance of a loan

Write a function that calculates and returns the remaining loan balance. This function accepts four parameters in the exact order shown below:

(principal, annual_interest_rate, duration , number_of_payments)

- principal: The total amount of loan. Assume that the principal is positive floating point number.
- annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
- duration: number of years to pay the loan back. Assume that duration is a positive integer.
- number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer.
  
To calculate the reamining loan balance use the following equation

𝑅𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐿𝑜𝑎𝑛𝐵𝑎𝑙𝑎𝑛𝑐𝑒=𝑃𝑟𝑖𝑛𝑐𝑖𝑝𝑎𝑙 ∗ ((((1+𝐫)**𝐧)−((1+𝐫) **𝐩)) / ((1+𝐫)𝐧−1))

Where:

- r is the monthly interest rate. r should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly. Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation:  𝑅𝑒𝑚𝑎𝑖𝑛𝑖𝑛𝑔𝐿𝑜𝑎𝑛𝐵𝑎𝑙𝑎𝑛𝑐𝑒=𝑃𝑟𝑖𝑛𝑐𝑖𝑝𝑎𝑙(1−𝐩𝐧) 
- n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
- p is the number of payments which are already made.
Your function should return the remaining balance as a floating point number.


## Part 3: Display Loan Information

Write a program for loan calculations. Your program should ask the user for three pieces of information (with three seperate input() functions:)

- Total amount of loan.
- Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means that annual interest is 5% (five percent) per year.
- Total duration of loan in years.

Your Program should use the two functions that you implented in part 1 and 2 of this exercise and display the follwoing information about the loan.

In the first first line show the amount of loan and interest rate.
In the second line show duration of the loan and monthly payment.
In each of the following lines show the Loan balance and total amount paid for each year.

Example 1: assuming that user inputs the following numbers in response to your questions:

```
Enter loan amount: 1000.0
Enter annual interest rate (percent): 10.0
Enter loan duration in years: 5
The output of your program should be:
```

```
LOAN AMOUNT: 1000 INTEREST RATE (PERCENT): 10
DURATION (YEARS): 5 MONTHLY PAYMENT: 21
YEAR: 1 BALANCE: 837 TOTAL PAYMENT 254
YEAR: 2 BALANCE: 658 TOTAL PAYMENT 509
YEAR: 3 BALANCE: 460 TOTAL PAYMENT 764
YEAR: 4 BALANCE: 241 TOTAL PAYMENT 1019
YEAR: 5 BALANCE: 0 TOTAL PAYMENT 1274
```

Important notes:
 * Use floating point numbers in your calculations.
 * Convert all the numbers to int only for printing them.
  