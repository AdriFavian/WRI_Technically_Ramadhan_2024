package main
import (
	"fmt"
)

func romanToInt(roman string) int {
	romanNumerals := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	result := 0

	for i, char := range roman {
	 	// cek apakah simbol saat ini lebih kecil dari simbol berikutnya
        // if yes = simbol saat ini - result
		if i+1 < len(roman) && romanNumerals[char] < romanNumerals[rune(roman[i+1])] {
			result -= romanNumerals[char]
		} else {
			result += romanNumerals[char]
		}
	}
	return result
}

func main() {
	fmt.Println(romanToInt("MM"))     //2000
	fmt.Println(romanToInt("MDCLXVI"))//1666
	fmt.Println(romanToInt("M"))      //1000
	fmt.Println(romanToInt("CD"))     //400
	fmt.Println(romanToInt("XC"))     //90
	fmt.Println(romanToInt("XL"))     //40
	fmt.Println(romanToInt("I"))      //1
}
