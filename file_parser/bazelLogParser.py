__author__ = 'Awadhesh Gupta'

"""
bazelLogParser.py
---------------------------------------------
Responsible for:
    - reading input file path and output path 
    - reading input file, parsing for required information
    - Adding required information to output file.
"""
import os

#To Parge log as per defined business logic.
def logParser(inputFile,outputPath):
    searchString = "_virtual_includes"
    interList = []
    finalList = []
    # checking if file exists and valid
    if os.path.isfile(inputFile) and os.path.getsize(inputFile) <= 0:
        print("Error : File doesn't exists or invalid !!!")
        return 1
    try:
        #Opening file 
        with open(inputFile, "r") as fileRead:
            for line in fileRead:
                val = line.split(";")
                for tempVal in  val:
                    if searchString in tempVal:
                        interList.append(tempVal)
                        finalVal = tempVal.split("_virtual_includes")
                        finalOutput = outputPath + finalVal[1]
                        finalList.append(finalOutput)
    except IOError:
        print("Error: Input File does not appear to exist.")
        return 1
    # print the contents of list
    scriptLocation = os.path.dirname(os.path.realpath(__file__))
    IntermediateFile =  scriptLocation +"/../data/Intermediate.txt"
    #Writing List to file
    with open(IntermediateFile, 'w') as filehandle:  
        for listitem in interList:
            filehandle.write('%s\n' % listitem)
    FinalFile =  scriptLocation +"/../data/Final.txt"
    #Writing List to file
    with open(FinalFile, 'w') as filehandle:  
        for listitem in finalList:
            filehandle.write('%s\n' % listitem)
    return finalList
    #print(interList)
    #print(finalList)

#scriptLocation = os.path.dirname(os.path.realpath(__file__))
#print(scriptLocation)
#inputFile = "../../input.txt"
#outputPath = "aaa/bbb/ccc/ddd/fff/ggg/edr"
#logParser(inputFile,outputPath)

