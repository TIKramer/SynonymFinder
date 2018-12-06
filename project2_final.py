import time

from FileReader import FileReader
from ProfileDictionary import ProfileDictionary
from Menu import Menu

#main function
def main():
    fileReader = FileReader()
    profileDictionary = ProfileDictionary("")
    menu = Menu(fileReader, profileDictionary)

    
    #Prints computational time of program
   # print("--- %s seconds ---" % (time.time() - start_time))

main()
#Tested with
#main("sample.txt","set.txt","common.txt")
#with files from project description
