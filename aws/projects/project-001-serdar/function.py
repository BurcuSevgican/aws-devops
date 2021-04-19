def convert_to_roman(num):
    roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanvalue = ''
    for i,d in enumerate(number):
        while (num >= d): 
            num -= d
            romanvalue += roman[i]
    return romanvalue