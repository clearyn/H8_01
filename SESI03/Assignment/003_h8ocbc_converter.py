"""
003_h8ocboc_converter
Nama: Ryan Cleary
Kode: FSDO001ONL003
"""

def kelvin_to_celcius(value: float, reverse: bool = False):
    """
    kelvin_to_celcius(value, reverse) is function to convert Kelvin to Celcius temperature, this function can be reversed by add value "True on reverse argument"
    :param value: float | integer
    :param reverse: bool | default: False 
    :return return_value: float of converted value temperature
    """
    if(reverse == True):
        # Celcius to kelvin formula : 0°C + 273.15 = 273.15K (Google Unit Converter)
        value += 273.15
    else:
        # Kelvin to celcius formula : 0K − 273.15 = -273.1°C (Google Unit Converter)
        value -=  273.15
    return_value = round(value, 2)
    return return_value

def toFahrenheit(value: float, unit: str):
    """
    toFahrenheit(value, unit) is function to convert Celcius or Kelvin unit temperature into Fahrenheit unit
    :param value: float | integer
    :param unit: str
    :assert InvalidUnit: if unit value not 'celcius' or 'kelvin'
    :return return_value: float of converted value Celcius or Kelvin into Fahrenheit 
    """
    assert unit in ['celcius', 'kelvin'], "InvalidUnit: unit value only accept 'celcius' or 'kelvin'"
    # Celcius to Fahrenheit formula: (0°C × 9/5) + 32 = 32°F (Google Unit Converter)
    celcius = value if unit == 'celcius' else kelvin_to_celcius(value)
    return_value = round(((celcius * 9/5) + 32), 2)
    return return_value

def fahrenheit_to_cf(value: float, output: str):
    """
    fahrenheit_to_cf(value, unit) is function to convert Fahrenheit unit temperature into Celcius or Kelvin unit
    :param value: float | integer
    :param output: str
    :assert InvalidOutput: if output value not 'celcius' or 'kelvin'
    :return return_value: float of converted value Fahrenheit into Celcius or Kelvin
    """
    assert output in ['celcius', 'kelvin'], "InvalidOutput: unit value only accept output 'celcius' or 'kelvin'"
    # Fahrenheit to Celcius formula: (0°F − 32) × 5/9 = -17.78°C (Google Unit Converter)
    celcius = (value - 32) * (5/9)
    temp_value = celcius if output == 'celcius' else kelvin_to_celcius(celcius, reverse = True)
    return_value = round(temp_value, 2)
    return return_value

##
print(__doc__)
isFinished = False
defaultValueTest = 50
intro = """
Choose menu:
1. I want to convert kelvin to celcius
2. I want to convert celcius to kelvin
3. I want to convert celcius to fahrenheit
4. I want to convert kelvin to fahrenheit
5. I want to convert fahrenheit to celcius
6. I want to convert fahrenheit to kelvin
7. Auto test all with my value
8. Exit
"""

while isFinished == False:
    try:
        print(intro)
        choice = int(input("Enter number of choice: "))
        if(choice == 1): 
            i_value = float(input("Enter Kelvin value: "))
            print("Your value in Celcius : {result}".format(result = kelvin_to_celcius(i_value)))
        if(choice == 2): 
            i_value = float(input("Enter Celcius value: "))
            print("Your value in Kelvin : {result}".format(result = kelvin_to_celcius(i_value, reverse = True)))
        if(choice == 3): 
            i_value = float(input("Enter Celcius value: "))
            print("Your value in Fahrenheit : {result}".format(result = toFahrenheit(i_value, 'celcius')))
        if(choice == 4): 
            i_value = float(input("Enter Kelvin value: "))
            print("Your value in Fahrenheit : {result}".format(result = toFahrenheit(i_value, 'kelvin')))
        if(choice == 5): 
            i_value = float(input("Enter Fahrenheit value: "))
            print("Your value in Celcius : {result}".format(result = fahrenheit_to_cf(i_value, 'celcius')))
        if(choice == 6): 
            i_value = float(input("Enter Fahrenheit value: "))
            print("Your value in Kelvin : {result}".format(result = fahrenheit_to_cf(i_value, 'kelvin')))
        if(choice == 7):
            defaultValueTest = float(input("Enter value for all test: "))
            print("\nShowing all test result :\n")
            print(defaultValueTest,"K -> C = ",  kelvin_to_celcius(defaultValueTest))
            print(defaultValueTest,"C -> K = ",  kelvin_to_celcius(defaultValueTest, True))
            print(defaultValueTest,"C -> F = ",  toFahrenheit(defaultValueTest, 'celcius'))
            print(defaultValueTest,"K -> F = ",  toFahrenheit(defaultValueTest, 'kelvin'))
            print(defaultValueTest,"F -> C = ",  fahrenheit_to_cf(defaultValueTest, 'celcius'))
            print(defaultValueTest,"F -> K = ",  fahrenheit_to_cf(defaultValueTest, 'kelvin'))
        if choice == 8: isFinished = True

        input("\nPress enter to continue")

    except:
        print("Something went wrong, try again with valid number value")
        continue
else:
    print("Terima Kasih, testing selesai")