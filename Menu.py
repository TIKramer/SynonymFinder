import math
from Profile import Profile
from ProfileSet import ProfileSet
from ProfileDictionary import ProfileDictionary
from FileReader import FileReader
import pickle
import os.path

class Menu:
     
    def __init__(self,fileReader, profileDictionary):
        self.profileDictionary = profileDictionary
        self.fileReader = fileReader
        self.sentences = []
        self.readProfileSets = []
        self.profileSets = {}
        self.loadState()
        self.displayMenu()
        
        
    def displayMenu(self):
        menuLoop = True

        while(menuLoop):
            print("\n\t ---Menu--- \t\n")
            print("Select 1 to add new sentences file:")
            print("Select 2 to add/update common text file")
            print("Select 3 to add new sets file:")
            print("Select 4 to process current files")
            print("Select 5 to read current file selection")
            print("Select 6 to save")


            selection = input("Please enter a number to select:\n")
            try:

                if(selection == "1"):
                    self.sentences = self.fileReader.openFile(input("Please enter a text file"))

                elif(selection == "2"):
                     commonWords = self.fileReader.readCommonWordsFile(input("Please enter a text file"))
                     self.profileDictionary.updateCommonWordList(commonWords)
                elif(selection == "3"):
                    self.readProfileSets = self.fileReader.readSets(input("Please enter a text file"))
                elif(selection == "4"):
                    self.createProfileDictionary()
                elif(selection == "5"):
                    print(self.profileDictionary)
                elif(selection == "6"):
                    print(self.saveState())
                elif(selection == "0"):
                    menuLoop = False
                
            except IOError as e:
                print(str(e))
        
                


        
    def createProfileDictionary(self):
        
        if(self.sentences and self.readProfileSets):
            uniqueProfiles = self.getUniqueProfiles(self.readProfileSets)
            self.profileDictionary.addProfilesUsingSentences(self.sentences, uniqueProfiles)
            #self.createProfileSets()
        else:
            numSentences = len(self.sentences)
            numProfiles = len(self.readProfileSets)
            if  (numSentences == 0 and numProfiles == 0):
                print("Error: textfile and set file are both empty")
            elif numSentences == 0:
                print("Error: text file is empty")
            elif numProfiles == 0:
                print("Error: set file is empty")
        
    def getUniqueProfiles(self, profileSets):
        uniqueProfiles = set()
        for key in profileSets:
            for profile in profileSets[key]:
                uniqueProfiles.add(profile)
        return uniqueProfiles
    
    def createProfileSets(self):
        for key in self.readProfileSets:
            setName = self.readProfileSets[key][0]
            if(setName not in self.profileDict):
                setProfile = Profile(setName)
                self.profileDict[setName] = setProfile
            profileList = []
            for value in self.profileSets[key][1:]:
                if(value in profileDict):
                    profileList.append(profileDict[value])
                else:
                    profile = Profile(value)
                    profileDict[value] = profile
                    profileList.append(profileDict[value])
            profileSets.append(ProfileSet(profileDict[setName], profileList))


    def saveState(self):
        f = open("profileDictionary.pkl", 'wb')
        pickle.dump(self.profileDictionary, f)          
        f.close()   
    
    def loadState(self):
        file = "profileDictionary.pkl"
        if os.path.isfile(file) and os.path.getsize(file) > 0:
            f = open('profileDictionary.pkl', 'rb')   
            self.profileDictionary = pickle.load(f)
            f.close()
            print("readFile")
        
    