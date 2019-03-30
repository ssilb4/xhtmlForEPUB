number = 0
padd1 = "0"                                   #It is padding for me
padd2 = "00"                                  #It is padding for me
padd3 = "000"                                 #It is padding for me
fileLocation = "./Section"                    #need to setting
filename = ""                                 #need to setting
fileTypeInput = ".xhtml..bdb.html"            #need to setting
fileTypeOutput = ".xhtml"
while 1:
    number += 1
    if number < 10:
        filename = fileLocation + padd3 + str(number)
    elif number < 100: 
        filename = fileLocation + padd2 + str(number)
    elif number < 1000: 
        filename = fileLocation + padd1 + str(number)
    
    inputFile = open(filename + fileTypeInput, 'rt', encoding='UTF-8')
    outputFile = open(filename + fileTypeOutput, 'w', encoding='U16')
    if not inputFile: break

    textStart = "<body"
    writeFlag = -1

    outputFile.write("<?xml version=\"1.0\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.1//EN\"\n\"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n<title></title>\n</head>\n")

    while 1:
        line = inputFile.readline()
        if not line: break
        if textStart in line:
            writeFlag = 1
        if writeFlag == 1:
            outputFile.write(line)
    inputFile.close()
    outputFile.close()
    print(number)



