company = "Samsung Convertor 1999"
print(company)
def conversion():
    value = input('Enter the value that is need to convert: ')
    unit1 = input('which unit of measure of the needed to convert?:  ')
    unit2 = input('Which unit of measure do you want it converted to?: ')
    if unit1 == "m" or "M" and unit2 == "ft" or "FT":
        ans = float(value) * 3.28
        print(ans)
    elif unit1 == "ft" or "FT" and unit2 == "m" or "M":
        ans = float(value) / 3.28
        print(ans)
    elif unit1 == "m" or "M" and unit2 == "in" or "IN":
        ans = float(value) * 39.37
        print(ans)
    elif unit1 == "in" or "IN" and unit2 == "m" or "M":
        ans = float(value) / 39.37
        print(ans)
    elif unit1 == "kg" or "KG" and unit2 == "lbs" or "LBS":
        ans = float(value) * 2.20
        print(ans)
    elif unit1 == "lbs" or "LBS" and unit2 == "kg" or "KG":
        ans = float(value) / 2.20
        print(ans)
    elif unit1 == "fah" or "FAH" and unit2 == "cel" or "CEL":
        ans = float(value) - 32 * (5/9)
        print(ans)
    elif unit1 == "cel" or "CEL" and unit2 == "fah" or "FAH":
        ans = float(value) * 9 / 5 + 32
        print(ans)
    elif unit1 == "cel" or "CEL" and unit2 == "rank" or "RANK":
        ans = float(value) + 273.15 * 9 / 5
        print(ans)
    elif unit1 == "rank" or "RANK" and unit2 == "cel" or "CEL":
        ans = float(value) - 491.67 * 5 / 9
        print(ans)
    elif unit1 == "kPa" and unit2 == "psi":
        ans = float(value) / 6.8947
        print(ans)
    elif unit1 == "psi" and unit2 == "kPa":
        ans = float(value) * 6.8947
        print(ans)
    print("\n")

    convertAgain()
conversion()

def convertAgain():
    ques = input("Do you want to convert another set of measure?: Yes/No: ")
    if ques == "Yes":
        conversion()
        convertAgain()
    elif ques == "No":
        print("no alec")
convertAgain()