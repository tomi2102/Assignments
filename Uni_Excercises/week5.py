#Excercise 0
months_of_year = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
roman_arabic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
periodic_tabe = {"H":"Hydrogen", "He":"Helium", "Li":"Lithium", "Be":"Beryllium", "B":"Boron", "C":"Carbon", "N":"Nitrogen"}
roman = {}
roman[1] = "I"
roman[5] = "V"
roman[10] = "X"
roman[50] = "L"
roman[100] = "K"
roman[500] = "D"
roman[1000] = "M"
roman[100000] = "T"
print(roman)
roman.update({100:"C"})
print(roman)
roman.pop(100000)
print(roman)



