def npr_to_usd(amount):
    return amount / 110

def usd_to_npr(amount):
    return amount * 110

amount = float(input("Enter the amount: "))
currency = input("Enter the currency: (npr, usd): ")

if currency == "npr":
    usd = npr_to_usd(amount)
    print(f"Nrs {amount} = ${usd}")

else:
    npr = usd_to_npr(amount)
    print(f"${amount} = Nrs {npr}")