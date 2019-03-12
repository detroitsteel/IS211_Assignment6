#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to test the a unit conversion function"""

import conversions_refactored
import unittest
import random

class KnownValuesC_K(unittest.TestCase):
    knownValuesCtoK = ((500.00, 773.15),
                   (410.00, 683.15),
                   (240.00, 513.15),
                   (0.00, 273.15),
                   (-90.0, 183.15),
                   (-273.15, 0.00))
    
    def testCtoKValues(self):
        """convertInputUnits should return the correct Kel value"""
        for c, k in self.knownValuesCtoK:
            result = conversions_refactored.convertInputUnits('cel', 'kel', c)
            self.assertEqual(k, result)
            
class KnownValuesC_F(unittest.TestCase):
    knownValuesCtoF = ((500.00, 932.00),
                   (410.00, 770.00),
                   (240.00, 464.00),
                   (0.00, 32.00),
                   (-90.0, -130.00),
                   (-273.15, -459.67))
    
    def testCtoFValues(self):
        """convertInputUnits should return the correct Fah value"""
        for c, f in self.knownValuesCtoF:
            result = conversions_refactored.convertInputUnits('cel', 'fah', c)
            self.assertEqual(f, result)                   

class KnownValuesF_C(unittest.TestCase):
    knownValuesFtoC = ((932.00, 500.00),
                   (770.00, 410.00),
                   (464.00, 240.00),
                   (32.00, 0.00),
                   (-130.00, -90.0),
                   (-459.67, -273.15))
    
    def testFtoCValues(self):
        """convertInputUnits should return the correct Cel value"""
        for f, c in self.knownValuesFtoC:
            result = conversions_refactored.convertInputUnits('fah', 'cel', f)
            self.assertEqual(c, result) 

class KnownValuesF_K(unittest.TestCase):
    knownValuesFtoK = ((932.00, 773.15),
                   (770.00, 683.15),
                   (464.00, 513.15),
                   (32.00, 273.15),
                   (-130.00, 183.15),
                   (-459.67, 0.00))
    
    def testFtoKValues(self):
        """convertInputUnits should return the correct Kel value"""
        for f, k in self.knownValuesFtoK:
            result = conversions_refactored.convertInputUnits('fah', 'kel', f)
            self.assertEqual(k, result) 

class KnownValuesK_C(unittest.TestCase):
    knownValuesKtoC = ((773.15, 500.00),
                   (683.15, 410.00),
                   (513.15, 240.00),
                   (273.15, 0.00),
                   (183.15, -90.0),
                   (0.00, -273.15))
    
    def testKtoCValues(self):
        """convertInputUnits should return the correct Cel value"""
        for k, c in self.knownValuesKtoC:
            result = conversions_refactored.convertInputUnits('kel', 'cel', k)
            self.assertEqual(c, result)

class KnownValuesK_F(unittest.TestCase):
    knownValuesKtoF = ((773.15, 932.00),
                   (683.15, 770.00),
                   (513.15, 464.00),
                   (273.15, 32.00),
                   (183.15, -130.00),
                   (0.00, -459.67))
    
    def testKtoFValues(self):
        """convertInputUnits should return the correct Fah value"""
        for k, f in self.knownValuesKtoF:
            result = conversions_refactored.convertInputUnits('kel', 'fah', k)
            self.assertEqual(f, result)

class KnownValuesM_Y(unittest.TestCase):
    knownValuesMtoY = ((100, 176000.00),
                   (55, 96800.00),
                    (33.3, 58608.00), 
                   (1, 1760.00),
                   (11.21, 19729.6))
    
    def testMtoYValues(self):
        """convertMilesToYards should return the correct Yar value"""
        for m, y in self.knownValuesMtoY:
            result = conversions_refactored.convertInputUnits('mil', 'yar', m)
            self.assertEqual(y, result)

class KnownValuesM_Me(unittest.TestCase):
    knownValuesMtoMe = ((100, 160934.4),
                   (55, 88513.92),
                    (33.3, 53591.16), 
                   (1, 1609.34),
                   (11.21, 18040.75))
    
    def testMtoMeValues(self):
        """convertInputUnits should return the correct Met value"""
        for m, me in self.knownValuesMtoMe:
            result = conversions_refactored.convertInputUnits('mil', 'met', m)
            self.assertEqual(me, result)

class KnownValuesY_M(unittest.TestCase):
    knownValuesYtoM = ((176000.00, 100),
                   (96800.00, 55),
                    (58608.00, 33.3), 
                   (1760.00, 1),
                   (19729.6, 11.21))

    def testYtoMValues(self):
        """convertInputUnits should return the correct Mil value"""
        for y, m in self.knownValuesYtoM:
            result = conversions_refactored.convertInputUnits('yar', 'mil', y)
            self.assertEqual(m, result)

class KnownValuesY_Me(unittest.TestCase):
    knownValuesYtoMe = ((1000.00, 914.41),
                   (555.00, 507.5),
                    (332.2, 303.77), 
                   (13.00, 11.89),
                   (1, 0.91))

    def testYtoMeValues(self):
        """convertInputUnits should return the correct Met value"""
        for y, me in self.knownValuesYtoMe:
            result = conversions_refactored.convertInputUnits('yar', 'met', y)
            self.assertEqual(me, result)

class KnownValuesME_M(unittest.TestCase):
    knownValuesMeToM = ((160934.4, 100),
                   (88513.92, 55),
                    (53591.16, 33.3), 
                   (1609.34, 1),
                   (18040.75, 11.21))

    def testMEtoMValues(self):
        """convertInputUnits should return the correct Mil value"""
        for me, m in self.knownValuesMeToM:
            result = conversions_refactored.convertInputUnits('met', 'mil', me)
            self.assertEqual(m, result)

class KnownValuesME_Y(unittest.TestCase):
    knownValuesMeToY = ((914.41, 1000.00),
                   (507.5, 555.00),
                    (303.77, 332.2), 
                   (11.89, 13.00),
                   (0.91, 1))

    def testMEtoYValues(self):
        """convertInputUnits should return the correct Yar value"""
        for me, y in self.knownValuesMeToY:
            result = conversions_refactored.convertInputUnits('met', 'yar', me)
            self.assertEqual(y, result)

class KnownValuesSelf(unittest.TestCase):
    KnownValuesSelf = ('cel',
                   'kel',
                    'fah', 
                   'mil',
                   'yar',
                    'met')
    def testSelfValues(self):
        """convertInputUnits should return the correct Yar value"""
        randm = random.randint(1, 100)
        for sf in self.KnownValuesSelf:
            result = conversions_refactored.convertInputUnits(sf,sf,  randm)
            self.assertEqual(randm, result)
            randm = random.randint(1, 100)

class KnownValuesWrong(unittest.TestCase):
    KnownValuesWrong = (('cel', 'yar'),
                   ('kel', 'mil'),
                    ('fah', 'met'), 
                   ('mil', 'cel'),
                   ('yar', 'fah'),
                    ('met', 'kel'))
    
    def testSelfValues(self):
        """convertInputUnits should return the correct Yar value"""
        randm = random.randint(1, 100)
        for w1, w2 in self.KnownValuesWrong:
            result = conversions_refactored.convertInputUnits(w1,w2, randm)
            self.assertRaises(conversions_refactored.ConversionNotPossible
                              ,conversions_refactored.convertInputUnits,
                              w1,w2,randm)
            #self.assertEqual(randm, result)
            randm = random.randint(1, 100)            
if __name__ == "__main__":
    unittest.main()
