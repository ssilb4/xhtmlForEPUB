import os
number = 0
fileLocation = "./"
fileTypeInput = ".xhtml..bdb.html"
fileTypeOutput = ".xhtml"
file_list = os.listdir(fileLocation)
for filename in file_list:
    if filename.find(fileTypeInput) is -1:
        continue
    number += 1
    print(filename.find('.'))
    outputFile = filename.split('.')[0]
    inputFile = open(filename, 'rt', encoding='UTF-8')
    outputFile = open(outputFile + fileTypeOutput, 'w', encoding='U16')
    
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
