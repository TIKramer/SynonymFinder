import math
from Profile import Profile
from ProfileSet import ProfileSet
from ProfileDictionary import ProfileDictionary
from FileReader import FileReader
from Data import Data
import pickle
import os.path

class Menu:
     
    def __init__(self,fileReader, profileDictionary):
        self.profileDictionary = profileDictionary
        self.fileReader = fileReader
        self.sentences = []
        self.readProfileSets = []
        self.profileSets = {}
        self.uniqueProfiles = set()
        self.data = Data()
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
            print(self.uniqueProfiles)


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
                    self.createProfileSets()
                elif(selection == "5"):
                    print(self.profileDictionary)
                    for profile in self.profileSets:
                        print(str(self.profileSets[profile]))
                        print("ID of set: " + str(id(self.profileSets[profile])))
                elif(selection == "6"):
                    self.saveState()
                elif(selection == "0"):
                    menuLoop = False
                
            except IOError as e:
                print(str(e))
                
    def createProfileDictionary(self):
        self.getUniqueProfiles(self.readProfileSets)
        if(self.sentences and self.uniqueProfiles):
            ("\n--ADDING--" + str(self.uniqueProfiles))
            self.profileDictionary.addProfilesUsingSentences(self.sentences, self.uniqueProfiles)
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
        for key in profileSets:
            for profile in profileSets[key]:
                self.uniqueProfiles.add(profile)
                
    def createProfileSets(self):
        for key in self.readProfileSets:
            setName = self.readProfileSets[key][0]
            if(setName not in self.profileSets):
                if(setName not in self.profileDictionary.getProfiles()):
                    setProfile = Profile(setName)
                    self.profileDictionary.getProfiles()[setName] = setProfile
                profileList = []
                for value in self.readProfileSets[key][1:]:
                    if(value in self.profileDictionary.getProfiles()):
                        profileList.append(self.profileDictionary.getProfiles()[value])
                    else:
                        profile = Profile(value)
                        self.profileDictionary.getProfiles()[value] = profile
                        profileList.append(self.profileDictionary.getProfiles()[value])
                self.profileSets[setName] = (ProfileSet(self.profileDictionary.getProfiles()[setName], profileList))

    def saveState(self):
        f = open("data.pkl", 'wb')
        self.data.setProfileDictionary(self.profileDictionary)
        self.data.setProfileSets(self.profileSets)
        self.data.setUniqueProfiles(self.uniqueProfiles)
        pickle.dump(self.data, f)          
        f.close()


 
        
    def loadState(self):
        file = "data.pkl"
        if os.path.isfile(file) and os.path.getsize(file) > 0:
            f = open(file, 'rb')   
            self.data = pickle.load(f)
            self.profileDictionary = self.data.getProfileDictionary()
            self.profileSets = self.data.getProfileSets()
            self.uniqueProfiles = self.data.getUniqueProfiles()
            f.close()
            print("readFile")
           

    