from locale import MON_1


months = {"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "ocotber":31, "november":30, "december":31}

month_num = int(input("Enter the month number i.e. (1 to 12): "))
if( month_num < 1 or month_num > 12 ):
    print("invalid month")
    exit()
    
keys = list(months.keys())
month = keys[month_num - 1]
days = months[month]

print(f"{month} has {days} days")