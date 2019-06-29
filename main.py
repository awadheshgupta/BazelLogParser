__author__ = 'Awadhesh Gupta'

"""
main.py
---------------------------------------------
Responsible for:
    - importing argument Parser
    - Assignming input value to variable
    - importing bazelLogParser.py` 
    - calling function logParser and passing input parameters.
"""

import file_parser.bazelLogParser
import common.argumentParse
import os

def main():
    #scriptLocation = os.path.dirname(os.path.realpath(__file__))
    #print(scriptLocation)
    arguments=common.argumentParse.argumentParse()
    inputFile=arguments.input
    outputPath=arguments.output
    #print(inputFile)
    #print(outputPath)
    file_parser.bazelLogParser.logParser(inputFile,outputPath)

#Main block execution
if __name__ == "__main__":
    main()



