function romanToInt (roman) {
    const angkaRoman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    let result = 0;

    for (let i = 0; i <roman.length; i++) {
        // cek apakah simbol saat ini lebih kecil dari simbol berikutnya
        // if yes = simbol saat ini - result
        if (i+1 < roman.length && angkaRoman[roman[i]] < angkaRoman[roman[i+1]]) {
            result -= angkaRoman[roman[i]];
        } else {
            result += angkaRoman[roman[i]];
        }
    }
    return result;
}
console.log(romanToInt('XXI'));    //21
console.log(romanToInt('I'));      //1
console.log(romanToInt('IV'));     //4
console.log(romanToInt('MMVIII')); //2008
console.log(romanToInt('MDCLXVI'));//1666
