import csv, json, sys

#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput,encoding='UTF-8') #open json file
    outputFile = open(fileOutput, 'w',encoding='UTF-8') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    
    output = csv.writer(outputFile,lineterminator='\n') #create a csv.write
#    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row