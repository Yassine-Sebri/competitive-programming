"""Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method."""
class RomanNumerals:
    def to_roman(number):
        roman = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40: 'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM'}
        var = [int(i) for i in '{:04d}'.format(number)]
        new_number = 'M'*var[0]
        for i in range(3):
            if var[1+i] < 4:
                new_number = new_number+var[1+i]*roman[100 // 10 ** i]
            elif var[1+i] == 4:
                new_number = new_number+roman[400 // 10 ** i]
            elif var[1+i] < 9:
                new_number = new_number+roman[500 // 10 ** i]+(var[1+i]-5)*roman[100 / 10 ** i]
            else:
                new_number = new_number+roman[900 // 10 ** i]
        return new_number

        return 
    def from_roman(number):
        roman = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40: 'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        roman = {v: k for k, v in roman.items()}
        new_number = 0
        index = 0
        while index < len(number):
            if number[index] in 'CXI' and index < len(number) - 1:
                if number[index] == 'C' and number[index+1] in 'MD':
                    new_number += roman[number[index:index+2]]
                    index += 1
                if number[index] == 'X' and number[index+1] in 'CL':
                    new_number += roman[number[index:index+2]]
                    index += 1
                if number[index] == 'I' and number[index+1] in 'XV':
                    new_number += roman[number[index:index+2]]
                    index += 1
                else:
                    new_number += roman[number[index]]
            else:
                new_number += roman[number[index]]
            index += 1
        return new_number
