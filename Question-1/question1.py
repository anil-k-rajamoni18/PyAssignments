input_filename = "CS638_A.txt"
output_filename = "Student_details.txt"
ID = "CS638AS"
#reading the input file
with open(input_filename,mode="r") as f1:
    inpData = f1.read().splitlines()
    filteredData=[]

    #filtering only needed lines
    for d in range(len(inpData)):
        if(inpData[d]!=""):
            filteredData.append(inpData[d])

    # storing in dictionary with key:value 
    outputDict = {ID+str(i):filteredData[i].replace(",","") for i in range(1,len(filteredData))}
    
    #print(outputDict)
    
    #writing to the output file .

    with open(output_filename , mode="w") as wf:
        wf.write("ID \t\t\t\t NAME\n\n")
        for key, val in outputDict.items():
            wf.write("%s \t\t\t %s\n"%(key,val))