__author__ = 'Awadhesh Gupta'

"""
argumentParse.py
---------------------------------------------
Responsible for:
    - Parsing input argument.` 
"""

import argparse


def argumentParse():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-i','--input', help='Input file path', required=True)
    parser.add_argument('-o','--output', help='Output path', required=True)
    args = parser.parse_args()
    return args

#argumentParse()