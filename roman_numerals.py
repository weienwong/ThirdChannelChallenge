

def roman_numerals(num):
    symbol_values = [
        ('M', 1000), 
        ('CM', 900), 
        ('D', 500), 
        ('CD', 400), 
        ('C', 100), 
        ('XC', 90), 
        ('L', 50), 
        ('XL', 40), 
        ('X', 10), 
        ('IX', 9), 
        ('V', 5), 
        ('IV', 4), 
        ('I', 1)
    ]

    symbol_count = []
    result_roman_numeral = ""

    for t in symbol_values:
        symbol = t[0]
        value = t[1]

        q = int(num / value)
        symbol_count.append((symbol, q))
        num = num % value


    for t in symbol_count:        
        result_roman_numeral += t[0] * t[1]

    return result_roman_numeral
