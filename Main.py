##Imported Modules
import x86CFunctionsModule.x86CFunctions as X
from pathlib import Path
import click

@click.command()
@click.argument("path")
def cli(path):
    target_dir = Path(path)
    if not target_dir.exists():
        click.echo("The target directory doesn't exist")
        raise SystemExit(1)

    if ".xasm" in target_dir.name or ".xsm" in target_dir.name:
        click.echo(f"{target_dir.name} is a Valid uncompressed XASM File Type.", nl=False)

    click.echo()

if __name__ == "__main__":
    cli()

##Variables, Dictionaries and Lists
Sections = []
Operators = ["LDR", "STR", "ADD", "SUB", "MUL", "DIV", "MOV", "CMP", "JMP", "JEQ", "JNE", "JGT", "JLT", "AND", "ORR", "EOR", "NOT", "STP"]
OperatorsA1 = ["JMP", "JEQ", "JNE", "JGT", "JLT", "NOT", "STP"]
Errors = ["INVALID_INSTRUCTION: ", "FILE_NOT_FOUND", "INVALID_REGISTER: ", "INVALID OPERANDS FOR INSTRUCTION"]

##Classes
#SectionData class used to store all relevant data on a section of xasm
class SectionData:
    def __init__(self, Label: str, Size: int, Data: list):
        self.SectionLabel: str = Label
        self.SectionSize: int = Size
        self.Instructions = Data

class XSMLine:
    def __init__(self, instruction, opr1, opr2):
        self.Operator = instruction
        self.Operand1 = opr1
        self.Operand2 = opr2

##Functions
#Removes the New Line character, the tab character and four spaces next to each other (just in case '    ' is used instead of tab)
def CleanLine(Line):
    Templine = ""
    if "\n" in Line:
        Templine = Line.replace("\n", "")
    if "    " in Line:
        Templine = Line.replace("   ", "")
    if "    " in Line:
        Templine = Line.replace("    ", "")
    return Templine

def SplitLine(Line):
    if "," in Line:
        Line = Line.replace(",", "")
    Templine = Line.split(" ")
    return Templine

def ErrorOut(Error):
    print(Errors[Error])
    exit()

def OperandErCheckAm(SplitArray):
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
            try:
                if Line[0] == "." and Counter == 0:
                    Counter += 1
                    TempList = []
                    TempLabel = Line
                elif Line[0] == "." and Counter != 0:
                    Counter += 1
                    Sections.append(SectionData(TempLabel, len(TempList) - 1, TempList))
                    TempList = []
                    TempLabel = Line
                elif Line != "\n":
                    TempList.append(Line)
            except:
                pass
        Sections.append(SectionData(TempLabel, len(TempList) - 1, TempList))

##Main
GetSections("XerASM.xasm")
OperandErCheckAm(["JMP", "<Label>", "Test"])
print(Sections[0].Instructions)
print(Sections[0].SectionSize)