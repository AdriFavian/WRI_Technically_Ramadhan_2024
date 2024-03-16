function ValidBraces(braces) {
    let stack = [];
    const matchingBraces = {//pasangan kurung
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let i = 0; i < braces.length; i++) {
        let brace = braces[i];

        // menambahkan ke stack jika brace is kurung pembuka 
        if (brace === '(' || brace === '[' || brace === '{') {
            stack.push(brace);
        } else {
            // Jika brace adalah penutup kurung tutup, periksa apakah sesuai dengan brace terakhir di stack
            let lastOpeningBrace = stack.pop();
            if (lastOpeningBrace !== matchingBraces[brace]) {
                return false; // Jika tidak sesuai, kembalikan false
            }
        }
    }

    // Jika masih ada elemen di stack, berarti terdapat kurung buka yang tidak memiliki pasangan
    return stack.length === 0;
}

console.log(ValidBraces("(){}[]"));    //true
console.log(ValidBraces("([{}])"));    //true
console.log(ValidBraces(")[{}]("));    //false
console.log(ValidBraces("(}"));        //false
console.log(ValidBraces("[(])"));      //false
console.log(ValidBraces("[({})](]"));  //false
