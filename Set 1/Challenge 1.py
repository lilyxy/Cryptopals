# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 00:26:51 2017

@author: Lily 
"""

import codecs

def hex_to_64(hex_string):
    decimal = codecs.decode(hex_string, 'hex');
    base64 = codecs.encode(decimal, 'base64');
    return base64


tests = ["49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"]
for t in tests:
    print(hex_to_64(t));