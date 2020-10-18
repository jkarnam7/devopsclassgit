#Calculate Persons Based On Year Of Birth#
name = str(input("Please Enter Your Good Name:"))
year = int(input("Please Enter The Year You Are Born:"))
print(year)
currentage = 2020 - year
months = currentage*12
print("Hello "+name + " You are years %d old " % (currentage))
print("Hello "+name + " You are months %d old " % (months))
