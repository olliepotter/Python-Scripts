birthday = ["03", "05", "1998"]
sum = 0
product = 1

for i in range(len(birthday)):
    print(birthday[i])
    sum = sum + int(birthday[i])
    product = product * int(birthday[i])


print(sum)
print(product)
