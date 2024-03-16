function expandedForm(num) {
    var multiple = 10;
    var hasil = [];

    while (num > 1){
        var remainder = num % multiple;// mencari sisa dengan operasi modulus desimal
        if (remainder > 0){
            hasil.unshift(remainder);//memasukkan remainder ke hasil
        }
        num -= remainder;//mencari nilai untuk next operation
        multiple = multiple * 10;// multiple modulus meningkat 
    }
    return hasil.join(" + ");
}
console.log(expandedForm(12))   
console.log(expandedForm(42))   
console.log(expandedForm(70304))