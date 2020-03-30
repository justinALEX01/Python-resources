# Create a class to open file
class OpenFile():
    file = ""
    def __init__(self,_fileName):
        self.fileName=_fileName

    def openfile(self):
        self.file = open(self.fileName)

    def closefile(self):
        if self.file.close():
           self.file = None

#Create a class to Write File
class WriteFile(OpenFile):
    data = [["Romania","Spania","Grecia"],["Bucuresti","Madrid","Atena"]]

    def openfile(self):
        self.file = open(self.fileName,"w")

    def write(self):
        for item1 in self.data:
            for item2 in item1:
                self.file.write(item2 + " ")
            self.file.write("\n")
    pass

#Create a class to Read File
class ReadFile(OpenFile):
    List=[]
    def read(self):
        for line in self.file:
            self.List.append(line)
        pass

alfa = WriteFile("Data.txt")
alfa.openfile()
alfa.write()
alfa.closefile()

alfaRead = ReadFile("Data.txt")
alfaRead.openfile()
alfaRead.read()
print(alfaRead.List)
alfa.closefile()
