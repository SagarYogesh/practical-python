# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 0

while principal > 0:
    month = month + 1
    if principal < payment:
        total_paid = total_paid + principal * (1 + rate/12)
        principal = 0
        print(f'Month no {month}: Total paid = {round(total_paid, 2)} and Principal remaining = {round(principal, 2)}')
    elif month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        print(f'Month no {month}: Total paid = {round(total_paid, 2)} and Principal remaining = {round(principal, 2)}')
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
        print(f'Month no {month}: Total paid = {round(total_paid, 2)} and Principal remaining = {round(principal, 2)}')
