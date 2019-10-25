import os
import subprocess

#list that contains files extensions
extension = ["o", "c"]

#function that turns a C source code into a object file 
def fileToObject(sourceCode):
    flag = 0

    for element in sourceCode:
        if os.path.isfile(element):
            subprocess.run(["gcc", "-c", element])
            flag+=1
        
    if flag != 0:
        return True
    else:
        return False

#function that creates a static library with a name given as argument
def newLibrary(libName, objectFile):
    libList = ["ar", "rs", libName]

    for filename in objectFile:
        libList.append(filename)

    subprocess.run(libList)

#tad's names received from user
tad = []
print("Enter the C file's name that will compose the static library")
while True:
    element = input("file: ")
    if element == "":
        break
    print("")
    print("(if there is no more files that will compose the static libray just press RETURN)")
    print("")
    tad.append(element)

#libName = input("Enter the static library's name: ")
libName = "libStatic.a"
outputName = input("Enter the executable file's name that will be outputted: ")

#calling fileToObject function and passing a list of tad files as argument
if(fileToObject(tad)):

    #list of object files proveninet from fileToObject function
    objectFile = [
        filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extension[0])
    ]

    #calling newLibrary function and passing a list of file object to it
    newLibrary(libName, objectFile)

#in case an entered file does not exist
else:
    print("File doesn't exist!")
    exit()

#list containg all files that ends with ".c"
sourceCode = [filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extension[1])]

#searching for the client file, that is, the file that will utilize the static library
for filename in sourceCode:
    if filename == tad:
        continue
    else:
        client = [filename]

#running the client file with the static library to get an executable output
fileToObject(client)
objectClient = client[0][:-1] + "o"

subprocess.run(["gcc", "-o", outputName, objectClient, libName])

#deletes all the object files
for filename in objectFile: 
    subprocess.run(["rm", filename])

subprocess.run(["rm", objectClient])