# ACTIVITY 1

# Introduction
# HP has a revolutionary printing program: HP Instant Ink. With this program,
# the user can pay only for the number of copies printed and not for the volume of ink consumed.
# HP Instant Ink has 5 plans:

# Take into account that the number of pages printed per month is the maximum pages allowed
# for a specific plan (value itself included).

# Input
# The input value will be a positive integer value representing the number of pages that user prints per month.

# Output
# The output will be the name of the best plan for that user and the price per month that the user must pay.

# Example 1
# Input
# 15
# Output
# Plan in order to print 15 pages per month:
# Free.
# Price: 0 Euros.

# Example 2

# Input
# 450

# Output
# Plan in order to print 450 pages per month:
# Business.
# Price: 19.99 Euros.

# Example 3

# Input
# 1400

# Output
# Plan in order to print 1400 pages per month:
# Not available.
# Price: - Euros.

plans = [
    ["Free", 0, 15],
    ["Occasional", 2.99, 50],
    ["Moderate", 4.99, 100],
    ["Frequent", 9.99, 300],
    ["Business", 19.99, 700],
    ["Not available", "-", None]
]

plan = None
pages = int(input("Pages printed per month: "))

if pages > 0 and pages < 701:
    if pages < 16:
        plan = 0
    elif pages < 51:
        plan = 1
    elif pages < 101:
        plan = 2
    elif pages < 301:
        plan = 3
    else:
        plan = 4
else:
    plan = 5

print(f"\nPlan in order to print {pages} per month:")
print(plans[plan][0])
print(f"Price: {plans[plan][1]} Euros")
