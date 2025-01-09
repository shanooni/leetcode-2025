def romanToInteger(romans:str) -> int:
    roman = {"I" : 1, "V" : 5 , "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    number : int = 0

    for i in range(len(romans) - 1):
        if roman[romans[i]] < roman[romans[i + 1]]:
            print(i)
        else:
            print(roman[romans[i]])
    return number

romanToInteger("IIX")