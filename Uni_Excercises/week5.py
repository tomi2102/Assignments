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

#Excercise1
def display_dico(dico):
    for key in dico:
        print(key, '-->', dico[key])


#Excercise2
def concat_dico(dico1, dico2):
    result = {}
    for key, val in dico1.items():
        result[key] = val

    for key, val in dico2.items():
        result[key] = val 

    return result


def concat_dico_advanced(dico1, dico2):
    result = {}
    for key, val in dico1.items():
        result[key] = val

    for key, val in dico2.items():
        if key in result:
            result[key] = [dico1[key],dico2[key]]

        else:
            result[key] = val

    return result





#Excercise3
def map_list(keys, values):
    if len(keys) != len(values):
        return None
    mapped = {}
    for index in range(len(keys)):
        if keys[index] not in mapped:
            mapped[keys[index]] = values[index]
        else:
            print("Error: duplicate value", keys[index], "in the list of keys.")
            return None

    return mapped        







#Excercise4
def reverse_dictionary(dico):
    reversed_dico = {}
    for key, val in dico.items():
        if val in reversed_dico:
            print("Duplicate values in initial dictionary are not allowed.")
            return None
        else:
            reversed_dico[val] = key

    return reversed_dico


