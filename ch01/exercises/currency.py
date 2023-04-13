# Ask the user for the exchange rate and amount to exchange
rate = float(input("Enter the exchange rate for EUR to USD: "))
amount = float(input("Enter the amount of EUR to exchange: "))

# Convert the amount to USD and apply the service fee
total = amount * rate
result = total - 3.0

print("You will receive ${:.2f} USD, after a $3.00 service fee.".format(result))
