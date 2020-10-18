#Calculate Persons Based On Year Of Birth#
name = str(input("Please Enter Your Good Name:"))
year = int(input("Please Enter The Year You Are Born:"))
print(year)
currentage = 2020 - year
months = currentage*12
days = currentage*365
print("Hello "+name + " You are %d years old " % (currentage))
print("Hello "+name + " You are %d months old " % (months))
print("Hello "+name + " You are %d days old " % (days))
