#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to test the a unit conversion function"""

import conversions
import unittest

class KnownValuesC_K(unittest.TestCase):
    knownValuesCtoK = ((500.00, 773.15),
                   (410.00, 683.15),
                   (240.00, 513.15),
                   (0.00, 273.15),
                   (-90.0, 183.15),
                   (-273.15, 0.00))
    
    def testCtoKValues(self):
        """convertCelsiusToKelvin should return the correct K value"""
        for c, k in self.knownValuesCtoK:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(k, result)
            
class KnownValuesC_F(unittest.TestCase):
    knownValuesCtoF = ((500.00, 932.00),
                   (410.00, 770.00),
                   (240.00, 464.00),
                   (0.00, 32.00),
                   (-90.0, -130.00),
                   (-273.15, -459.67))
    
    def testCtoFValues(self):
        """convertCelsiusToFahrenheit should return the correct F value"""
        for c, f in self.knownValuesCtoF:
            result = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(f, result)                   

class KnownValuesF_C(unittest.TestCase):
    knownValuesFtoC = ((932.00, 500.00),
                   (770.00, 410.00),
                   (464.00, 240.00),
                   (32.00, 0.00),
                   (-130.00, -90.0),
                   (-459.67, -273.15))
    
    def testFtoCValues(self):
        """convertFahrenheitToCelsius should return the correct C value"""
        for f, c in self.knownValuesFtoC:
            result = conversions.convertFahrenheitToCelsius(f)
            self.assertEqual(c, result) 

class KnownValuesF_K(unittest.TestCase):
    knownValuesFtoK = ((932.00, 773.15),
                   (770.00, 683.15),
                   (464.00, 513.15),
                   (32.00, 273.15),
                   (-130.00, 183.15),
                   (-459.67, 0.00))
    
    def testFtoKValues(self):
        """convertFahrenheitToKelvin should return the correct C value"""
        for f, k in self.knownValuesFtoK:
            result = conversions.convertFahrenheitToKelvin(f)
            self.assertEqual(k, result) 

class KnownValuesK_C(unittest.TestCase):
    knownValuesKtoC = ((773.15, 500.00),
                   (683.15, 410.00),
                   (513.15, 240.00),
                   (273.15, 0.00),
                   (183.15, -90.0),
                   (0.00, -273.15))
    
    def testKtoCValues(self):
        """convertKelvinToCelsius should return the correct C value"""
        for k, c in self.knownValuesKtoC:
            result = conversions.convertKelvinToCelsius(k)
            self.assertEqual(c, result)

class KnownValuesK_F(unittest.TestCase):
    knownValuesKtoF = ((773.15, 932.00),
                   (683.15, 770.00),
                   (513.15, 464.00),
                   (273.15, 32.00),
                   (183.15, -130.00),
                   (0.00, -459.67))
    
    def testKtoFValues(self):
        """convertKelvinToFahrenheit should return the correct F value"""
        for k, f in self.knownValuesKtoF:
            result = conversions.convertKelvinToFahrenheit(k)
            self.assertEqual(f, result)

class KnownValuesM_Y(unittest.TestCase):
    knownValuesMtoY = ((100, 176000.00),
                   (55, 96800.00),
                    (33.3, 58608.00), 
                   (1, 1760.00),
                   (11.21, 19729.6))
    
    def testMtoYValues(self):
        """convertMilesToYards should return the correct F value"""
        for m, y in self.knownValuesMtoY:
            result = conversions.convertMilesToYards(m)
            self.assertEqual(y, result)

class KnownValuesM_Me(unittest.TestCase):
    knownValuesMtoMe = ((100, 160934.4),
                   (55, 88513.92),
                    (33.3, 53591.16), 
                   (1, 1609.34),
                   (11.21, 18040.75))
    
    def testMtoMeValues(self):
        """convertMilesToMeters should return the correct F value"""
        for m, me in self.knownValuesMtoMe:
            result = conversions.convertMilesToMeters(m)
            self.assertEqual(me, result)

class KnownValuesY_M(unittest.TestCase):
    knownValuesYtoM = ((176000.00, 100),
                   (96800.00, 55),
                    (58608.00, 33.3), 
                   (1760.00, 1),
                   (19729.6, 11.21))

    def testYtoMValues(self):
        """convertYardsToMiles should return the correct M value"""
        for y, m in self.knownValuesYtoM:
            result = conversions.convertYardsToMiles(y)
            self.assertEqual(m, result)

class KnownValuesY_Me(unittest.TestCase):
    knownValuesYtoMe = ((1000.00, 914.41),
                   (555.00, 507.5),
                    (332.2, 303.77), 
                   (13.00, 11.89),
                   (1, 0.91))

    def testYtoMeValues(self):
        """convertYardsToMeters should return the correct Me value"""
        for y, me in self.knownValuesYtoMe:
            result = conversions.convertYardsToMeters(y)
            self.assertEqual(me, result)

class KnownValuesME_M(unittest.TestCase):
    knownValuesMeToM = ((160934.4, 100),
                   (88513.92, 55),
                    (53591.16, 33.3), 
                   (1609.34, 1),
                   (18040.75, 11.21))

    def testMEtoMValues(self):
        """convertMetersToMiles should return the correct M value"""
        for me, m in self.knownValuesMeToM:
            result = conversions.convertMetersToMiles(me)
            self.assertEqual(m, result)

class KnownValuesME_Y(unittest.TestCase):
    knownValuesMeToY = ((914.41, 1000.00),
                   (507.5, 555.00),
                    (303.77, 332.2), 
                   (11.89, 13.00),
                   (0.91, 1))

    def testMEtoYValues(self):
        """convertMetersToYards should return the correct M value"""
        for me, y in self.knownValuesMeToY:
            result = conversions.convertMetersToYards(me)
            self.assertEqual(y, result)
            
if __name__ == "__main__":
    unittest.main()
