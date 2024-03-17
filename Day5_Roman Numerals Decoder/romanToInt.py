def romanToInt(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    
    for i in range(len(roman)):# len() = Return the number of items in a container
        # cek apakah simbol saat ini lebih kecil dari simbol berikutnya
        # if yes = simbol saat ini - result
        if i + 1 < len(roman) and roman_numerals[roman[i]] < roman_numerals[roman[i + 1]]:
            result -= roman_numerals[roman[i]]
        else:
            result += roman_numerals[roman[i]]
            
    return result

# Contoh penggunaan
print(romanToInt("XXI"))    # 21
print(romanToInt("I"))      # 1
print(romanToInt("IV"))     # 4
print(romanToInt("MMVIII")) # 2008
print(romanToInt("MDCLXVI"))# 1666   
