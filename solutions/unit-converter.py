#!/usr/bin/python
# -*- coding: latin-1 -*-

# **Unit Converter (temp, currency, volume, mass and more)** 
# - Converts various units between one another. The user enters the type of unit
#   being entered, the type of unit they want to convert to and then the value.
#   The program will then make the conversion.

units = {"mass": ["kilogram", "gram", "stone", "pound", "ounze"],
         "distance": ["metre", "centemetre", "kilometre", "mile", "yard", "feet", "inch"],
         "temperature": ["Celsius", "Farenheit", "Kelvin"],
         "currency": ["GBP", "EUR", "USD", "YEN"],
         "volume": ["litre", "millilitre", "gallon", "pint", "fluid ounce"]}

def get_from_unit():
    i = 1
    choices = []
    for key in units.keys():
        print key + ": ",
        for j, unit in enumerate(units[key]):
            print str(i + j) + ") " + unit,
            choices.append((key, unit))
        i += len(units[key])
        print "\n"
    while True:
        ch = raw_input("Please select a unit by entering the appropiate number (1 - {n}): ".format(n = i-1))
        if ch.isdigit():
            ch = int(ch)
            if 0 < ch < i:
                return choices[ch]
    
def get_to_unit(from_unit):
    pass

def get_value():
    pass

def display_conversion(from_unit, to_unit, value):
    pass

def ask_to_continue():
    pass

def main():
    cont = True
    while cont:
        from_unit = get_from_unit()
        to_unit = get_to_unit(from_unit)
        value = get_value()
        display_conversion(from_unit, to_unit, value)
        cont = ask_to_continue()

if __name__ == "__main__":
    main()

