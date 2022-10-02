def filterFileData(data):
    '''this functions will filter the data like removing unwanted characters'''
    data=[data[d] for d in range(1,len(data)) if data[d]!=""]
    # print(data)
    return  " ".join(data).replace(",","")

def UniqueWords(data):
    '''Prints the unique words '''
    unqWords = list(set(data))
    unqWords.sort()
    return unqWords

def NumberOfWords(data):
    '''returns the no of words'''
    return f"Number of words in a file are : {len(data)}"

#reading the input file
input_filename = "CS638_A.txt"

with open(input_filename,mode="r") as f1:
    inpData = f1.read().splitlines()
    filteredData = filterFileData(inpData)
    words = [ch for ch in filteredData.split()]
    Unqres = UniqueWords(words)
    print(*Unqres)
    print(f"Number of unique words are : {len(Unqres)} ")
    print(NumberOfWords(words))
