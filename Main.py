##Variables and Lists
Sections = []

##Classes
class SectionData:
    SectionLabel = 0
    SectionSize = 0
    Instructions = []

##Functions
#Gets the different sections from the xasm file
def GetSections(file: str):

    #Confirms the file exists
    try:
        with open(file, 'r') as File:
            print("FILE_EXISTS")
    except:
        print("ERR_FILE_DOES_NOT_EXIST")
        return
    
    #Creates a SectionData Object to store the section data
    with open(file, 'r') as File:
        Temp = SectionData
        TempList = []
        for Line in File:
            #Removes the new line character
            if "\n" in Line:
                Line = Line.replace("\n", "")
            TempList.append(Line)
        Temp.Instructions = TempList
        Sections.append(Temp)

##Main
GetSections("XerASM.xasm")
print(Sections[0].Instructions)