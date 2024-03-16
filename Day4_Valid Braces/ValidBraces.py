def ValidBraces(braces):
    stack = []
    matching_braces = { #pasangan kurung
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for brace in braces: #iterasi setiap elemen brace
        if brace in {'(', '[', '{'}: 
            stack.append(brace) #menambahkan ke stack jika kurung pembuka
        else:
            #memeriksa apakah stack kosong, jika stack kosong = semua tanda kurung memiliki pasangan
            #stack pop untuk memeriksa kecocokan tanda kurung pembuka yang terakhir
            if not stack or stack.pop() != matching_braces[brace]:
                return False # if not match

    # semua brace telah diproses,cek apakah masih ada opening brace yang tidak memiliki pasangan
    # Jika masih ada elemen di stack, berarti terdapat opening yang tidak memiliki pasangan
    return not stack  # True jika stack kosong, False jika tidak

print(ValidBraces("(){}[]"))    # True
print(ValidBraces("([{}])"))    # True
print(ValidBraces(")[{}]("))    # False
print(ValidBraces("(}"))        # False
print(ValidBraces("[(])"))      # False
print(ValidBraces("[({})](]"))  # False
