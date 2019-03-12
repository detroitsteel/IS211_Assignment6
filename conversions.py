#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts from one unit of measurement to a convertable unit of measure."""

def convertCelsiusToKelvin(cel):
    """convertCelsiusToKelvin Function - intakes an int or float which is
    assumed to be a degree of Celsius and converts to Kelvin.
    Args:
        cel (float): A url in csv format
    Output: A float. 
    Example:
        convertCelsiusToKelvin(500)
        >>>773.15
    """
    cel = float(cel)
    kel = cel + 273.15
    return round(kel, 2)

def convertCelsiusToFahrenheit(cel):
    """convertCelsiusToFahrenheit Function - intakes an int or float which is
    assumed to be a degree of Celsius and converts to Fahrenheit.
    Args:
        cel (float): A url in csv format
    Output: A float. 
    Example:
        convertCelsiusToKelvin(500)
        >>>932.00
    """
    cel = float(cel)
    fah = cel * 1.8 + 32
    return round(fah, 2)

def convertFahrenheitToCelsius(fah):
     fah = float(fah)
     cel = (fah - 32) * 0.5555555555555556
     return round(cel, 2)

def convertFahrenheitToKelvin(fah):
     fah = float(fah)
     kel = (fah + 459.67) * 0.5555555555555556
     return round(kel,2)   

def convertKelvinToCelsius(kel):
    kel = float(kel)
    cel = round(kel - 273.15, 2)
    return cel

def convertKelvinToFahrenheit(kel):
    kel = float(kel)
    fah = round(kel * 1.8 - 459.67, 2)
    return fah

def convertMilesToYards(mil):
    mil = float(mil)
    yar = mil * 1760
    return round(yar, 2)

def convertMilesToMeters(mil):
    mil = float(mil)
    mer = mil * 1609.344
    return round(mer, 2)

def convertYardsToMiles(yar):
    yar = float(yar)
    mil = yar / 1760
    return round(mil, 2)
    
def convertYardsToMeters(yar):
    yar = float(yar)
    met = yar / 1.0936
    return round(met, 2)

def convertMetersToMiles(met):
    met = float(met)
    mil = met / 1609.344
    return round(mil, 2)

def convertMetersToYards(met):
    met = float(met)
    yar = met * 1.0936
    return round(yar, 2)
