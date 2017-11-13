def tax_owed(income):
    if income <= 11000:
        tax_paid = 11000*0
    elif income <= 43000:
        tax_paid = income * 0.30
    elif income <= 150000:
        tax_paid = income * 0.40
    elif income > 150000:
        tax_paid = income * 0.55

    return tax_paid


income = int(input("What is your yearly income"))
print(tax_owed(income))
