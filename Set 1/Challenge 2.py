# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 00:51:30 2017

@author: Lily 
"""


def xor(stra, strb):
    a = int(stra, 16);
    b = int(strb, 16);
    return hex(a^b);


def xorwrap(stra, strb):
    orig = str(xor(stra, strb));
    return orig[2:];

print(xorwrap("1c0111001f010100061a024b53535009181c",
          "686974207468652062756c6c277320657965"));