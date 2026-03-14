##Imported Modules
import x86CFunctionsModule.x86CFunctions as X

##Variables, Dictionaries and Lists
Sections = []
Operators = ["LDA", "STR", "ADD", "SUB", "MUL", "DIV", "MOV", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "AND", "ORR", "EOR", "NOT"]
Errors = ["INVALID_INSTRUCTION", "FILE_NOT_FOUND", "INVALID_REGISTER", "INVALID OPERANDS FOR INSTRUCTION"]

##Classes
#SectionData class used to store all relevant data on a section of xasm
class SectionData:
    def __init__(self, Label: str, Size: int, Data: list):
        self.SectionLabel: str = Label
        self.SectionSize: int = Size
        self.Instructions = Data

##Functions
#Gets the different sections from the xasm file
def GetSections(file: str):

    #Confirms the file exists
    try:
        File = open(file, 'r')
        File.close()
    except:
        print(Errors[1])
        return
    
    #Creates a SectionData Object to store the section data
    with open(file, 'r') as File:
        Temp = SectionData
        TempList = []
        Counter = 0
        SecSize = 0
        for Line in File:
            #Removes the new line character
            if "\n" in Line:
                Line = Line.replace("\n", "")
            
            if "    " in Line:
                Line = Line.replace("   ", "")
            if "    " in Line:
                Line = Line.replace("    ", "")

            try:
                if Line[0] == "." and Counter == 0:
                    Counter += 1
                    Temp = SectionData
                    TempList = []
                elif Line[0] == "." and Counter != 0:
                    Counter += 1
                    Temp.Instructions = TempList
                    Temp.SectionSize = SecSize
                    Sections.append(Temp)
                    SecSize = 0
                    Temp = SectionData
                    TempList = []
                else:
                    SecSize += 1
                    TempList.append(Line)
            except:
                print("Empty Line")
        Temp.Instructions = TempList
        Sections.append(Temp)

##Main
GetSections("XerASM.xasm")
print(Sections[1].Instructions)
print(Sections[1].SectionSize)