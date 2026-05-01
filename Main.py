##Imported Modules
import x86CFunctionsModule.x86CFunctions as X

##Variables, Dictionaries and Lists
Sections = []
Operators = ["LDR", "STR", "ADD", "SUB", "MUL", "DIV", "MOV", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "AND", "ORR", "EOR", "NOT", "STP"]
OperatorsA1 = ["JMP", "JEQ", "JNE", "JGT", "JLT", "NOT", "STP"]
Operands = ["ACC", "R0", "R1", "R2", "R3"]
DataType = ["Integer", "Fixed Point", "Floating Point", "Address", "SectionLabel"]
Errors = ["INVALID_INSTRUCTION: ", "FILE_NOT_FOUND", "INVALID_REGISTER: ", "INVALID_OPERANDS", "INVALID_VALUE: "]
ErrorsWithReason = ["INVALID_INSTRUCTION: ", "INVALID_REGISTER: "]
Warns = ["!Value! | ", "!Memory! | "]
RegisterTypes = ["R", "%", "?"]

RegisterMemory = [
    [0, DataType[0]], 
    [0, DataType[0]], 
    [0, DataType[0]], 
    [0, DataType[0]],   #Accumulator and Void Registers
    0, 0, 0, 0,         #Integer Registers
    0, 0, 0, 0,         #Fixed-Point Registers
    0, 0, 0, 0          #Floating-Point Registers
]

## GIR
#R0 - 3
## GFiR, 01100110 . 01100110
#?0 - 3
## GFPR, 0.1101001001 01110
#%0 - 3

## Operator
# 10101 010



##Classes
#SectionData class used to store all relevant data on a section of xasm
class SectionData:
    def __init__(self, Label: str, Size: int, Data: list):
        self.SectionLabel: str = Label
        self.SectionSize: int = Size
        self.Instructions = Data

class XSMLine:
    def __init__(self, instruction, opr1, opr2 = "0"):
        self.Operator = instruction
        self.Operand1 = opr1
        self.Operand2 = opr2

##Functions
def InstructionCheck(SplitArray):
    Res = SplitArray[0] in OperatorsA1
    match Res:
        case True:
            if len(SplitArray) > 2:
                ErrorOut(3)
            return 1
        case False:
            if len(SplitArray) < 3:
                ErrorOut(3)
            return 2

def OperandCheck(Operand1):
    #Check if the Operand Type is a valid type
    match Operand1[0] in RegisterTypes:
        
        case True:
            print("Register")
            try:
                if int(Operand1[1]) > 3:
                    ErrorOut(2, Operand1)
            except:
                ErrorOut(2, Operand1)
        
        case False:
            if Operand1[0] == "#":
                print("Constant")
                Temp = ""
                for i in range(len(Operand1)):
                    if i > 0:
                        Temp += Operand1[i]
                print("A " + Temp)

                #Check if the Constant Value is a valid signed integer
                try:
                    Value = int(Temp)
                    if Value > 32767 or Value < -32767:
                        ErrorOut(0, Temp, True)
                except:
                    ErrorOut(4, Temp)

            else:
                print("Assume Memory Location")

def OperatorCheck(Line):
    Operator = Line[0]
    
    #Check how many Operands are included
    match len(Line) > 2:
        #Case for when two Operands are included
        case True:
            Operand1 = Line[1]
            Operand2 = Line[2]
            #Check if the Operator is Valid
            match Operator in Operators:
                case True:
                    pass
                case False:
                    ErrorOut(0, Operator)
            
            OperandCheck(Operand1)
            OperandCheck(Operand2)
            
        #Case for when only one Operand is included
        case False:
            Operand1 = Line[1]
            #Check if the Operator is Valid
            match Operator in Operators:
                case True:
                    pass
                case False:
                    ErrorOut(0, Operator)
            
            OperandCheck(Operand1)

    return Line

#Print an Error or a Warning when encountering a problem
def ErrorOut(Error, Reason = "", Warn = False):
    #Check if the values should be interpreted as a Warning or an Error (Warnings do not close the program)
    match Warn:

        case False:
            match Errors[Error] in ErrorsWithReason:

                case True:
                    print("EXECUTION ERROR | " + Errors[Error] + Reason)

                case False:
                    print("EXECUTION ERROR | " + Errors[Error])
            exit()
        
        case True:
            print("WARNING | " + Warns[Error] + Reason)

#Removes the New Line character, the tab character and four spaces next to each other (just in case '    ' is used instead of tab)
def CleanLine(Line):
    
    Templine = Line
    if "\n" in Line:
        Templine = Line.replace("\n", "")
    if "\t" in Line:
        Templine = Templine.replace("\t", "")
    if "    " in Line:
        Templine = Templine.replace("    ", "")
    if "," in Line:
        Templine = Templine.replace(",", "")
    
    return Templine

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
        TempList = []
        Counter = 0
        for Line in File:
            #Removes the new line character and tab character
            Line = CleanLine(Line)

            #Runs through the length of the file and creates instances of SectionData objects
            try:
                if Line[0] == "." and Counter == 0:
                    Counter += 1
                    TempList = []
                    TempLabel = Line.replace(".", "")
                elif Line[0] == "." and Counter != 0:
                    Counter += 1
                    Sections.append(SectionData(TempLabel, len(TempList), TempList))
                    TempList = []
                    TempLabel = Line.replace(".", "")
                elif Line != "\n":
                    TempList.append(Line)
            except:
                pass

        Sections.append(SectionData(TempLabel, len(TempList), TempList))

#Creates an XASMLine object and performs Neccisary Checks
def GetXSMLine(Line):
    #Split the Line into a list
    Instruction = Line.split(" ")

    #Perform the Syntax Check
    InstructionCheck(Instruction)

    #Performs the Operation and Operand check
    OperatorCheck(Instruction)


    if len(Instruction) > 2:
        return XSMLine(Instruction[0], Instruction[1], Instruction[2])
    else:
        return XSMLine(Instruction[0], Instruction[1])

##Main
GetSections("XerASM.xasm")
OperandCheck("#32768")
OperatorCheck(["MOV", "R0", "R1"])
InstructionCheck(["JMP", "<Label>"])
print(str(Sections[3].SectionLabel) + " | " + str(Sections[3].Instructions) + " | " + str(Sections[3].SectionSize))
