__author__ = 'Awadhesh Gupta'

"""
test_main.py
---------------------------------------------
Responsible for:
    - Unit testcase for each function..
"""

import argparse
import sys
import unittest
import file_parser.bazelLogParser
import common.argumentParse
import main
import os
  
class LogParserTest(unittest.TestCase): 
  
    # test if input file doesn't exists 
    def test_logParser_if_filedoesnotexists(self):
        out=file_parser.bazelLogParser.logParser("input","Test/value")
        self.assertEqual(out,1)
    # test if input file is blank. 
    def test_logParser_if_fileisblank(self):
        out=file_parser.bazelLogParser.logParser("test/input1.txt","123/value")
        self.assertEqual(out,1)
    # test if input file exists 
    def test_logParser_if_fileexists(self):
        out=file_parser.bazelLogParser.logParser("test/input.txt","ABC/Value")
        if len(out) > 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    # test if search string  doesnot exists in input file.
    def test_logParser_if_SearchStringDoesnotexists(self):
        out=file_parser.bazelLogParser.logParser("test/input.txt","ABC/Value")
        if len(out) > 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    # test if valid output file Final.txt created. 
    def test_logParser_if_validOutputfilecreated(self):
        out=file_parser.bazelLogParser.logParser("test/input.txt","ABC/Value")
        if os.path.isfile("data/Final.txt") and os.path.getsize("data/Final.txt") > 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    # test if valid output file Intermediate.txt created. 
    def test_logParser_if_validInterMediateOutputfilecreated(self):
        out=file_parser.bazelLogParser.logParser("test/input.txt","ABC/Value")
        if os.path.isfile("data/Intermediate.txt") and os.path.getsize("data/Intermediate.txt") > 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    # test if data folder is accessible to create file. 
    def test_logParser_if_dataFolderAccess(self):
        if os.access("data", os.W_OK):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

#Main  
if __name__ == '__main__': 
    unittest.main() 

