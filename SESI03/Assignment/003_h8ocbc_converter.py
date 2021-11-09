def kelvin_to_celcius(value: float, reverse: bool = False):
    """
    kelvin_to_celcius(value, reverse) is function to convert kelvin to celcius temperature, this function can be reversed by add value "True on reverse argument"
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
    return_value = (round(value, 2))
    return return_value


def toFahrenheit(value: float, unit: str):
    """
    toFahrenheit(value, unit) is function to convert kelvin or celcius unit temperature into fahrenheit unit
    :param value: float | integer
    :param unit: str
    :assert InvalidUnit: if unit value not 'celcius' or 'kelvin'
    :return return_value: float of converted value temperature
    """
    assert unit in ['celcius', 'kelvin'], "InvalidUnit: unit value only accept 'celcius' or 'kelvin'"
    # Celcius to Fahrenheit formula: (0°C × 9/5) + 32 = 32°F (Google Unit Converter)
    celcius = value if unit == 'celcius' else kelvin_to_celcius(value)
    return_value = ((celcius * 9/5) + 32)
    return return_value

def fahrenheit_to_cf(value: float, output: str):
    """
    fahrenheit_to_cf(value, unit) is function to convert kelvin or celcius unit temperature into fahrenheit unit
    :param value: float | integer
    :param output: str
    :assert InvalidUnit: if unit value not 'celcius' or 'kelvin'
    :return return_value: float of converted value temperature
    """
    assert output in ['celcius', 'kelvin'], "InvalidOutput: unit value only accept output 'celcius' or 'kelvin'"
    # Fahrenheit to Celcius formula: (0°F − 32) × 5/9 = -17.78°C (Google Unit Converter)
    celcius = (value - 32) * (5/9)
    return_value = celcius if output == 'celcius' else kelvin_to_celcius(celcius, reverse = True)
    return return_value

print(fahrenheit_to_cf(50, 'celcius'))