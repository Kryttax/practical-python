# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
normal_payment = 2684.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if(extra_payment_start_month < months 
    and months < extra_payment_end_month):
        payment = normal_payment + extra_payment
    else:
        payment = normal_payment

    principal = principal * (1+rate/12) 
    
    if principal < payment:
        payment = principal    

    principal = principal - payment
    total_paid = total_paid + payment
    months = months + 1

    print(f"Month: {months} -- Paid: {total_paid} -- Left: {principal}")

print('Total paid:', total_paid)
print('Months:', months)