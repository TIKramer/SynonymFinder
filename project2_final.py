
import math
import time
from Profile import Profile
from ProfileSet import ProfileSet
from ProfileDictionary import ProfileDictionary
from FileReader import FileReader

           
def createProfileSets(profileSets,profileDict):
    newSets = []
    for key in profileSets:
            setName = profileSets[key][0]
            if(setName not in profileDict):
                setProfile = Profile(setName)
                profileDict[setName] = setProfile
            profileList = []
            for value in profileSets[key][1:]:
                if(value in profileDict):
                    profileList.append(profileDict[value])
                else:
                    profile = Profile(value)
                    profileDict[value] = profile
                    profileList.append(profileDict[value])
            newSets.append(ProfileSet(profileDict[setName], profileList))
    return newSets
			
			
		   
#Opens text and set files, with error handling
def fileRead(corpus_file_name, test_sets_file, commonwords_file_name = None):
    dictionaryKeys = {}
    fileReader = FileReader()
    try:
        sentences = fileReader.openFile(corpus_file_name)
        profileSets = fileReader.readSets(test_sets_file)
        
        
        #If sentences and profiles exist, read common words file
        if(sentences and profileSets):
            commonWords = fileReader.readCommonWordsFile(commonwords_file_name);
            profileDict = ProfileDictionary(commonWords)
            uniqueProfiles = set()
            for key in profileSets:
                for profile in profileSets[key]:
                    uniqueProfiles.add(profile)
            profileDict.addProfilesUsingSentences(sentences, uniqueProfiles)
          #  print("\n\n\n Profile Dict"+ str(list(profileDict.getProfiles())) + "\n--------\n\n")
            #for key in profileDict.getProfiles():
              #  print("\n\n Item: " + key + "\n" + str(profileDict.getProfiles()[key]) + "\n ****\n")
            print(createProfileSets(profileSets, profileDict.getProfiles()))
        else:
            numSentences = len(sentences)
            numProfiles = len(profileSets)
            if  (numSentences == 0 and numProfiles == 0):
                print("Error: textfile and set file are both empty")
            elif numSentences == 0:
                print("Error: text file is empty")
            elif numProfiles == 0:
                print("Error: set file is empty")
    except IOError as e:
        print(str(e))
  
#main function
def main(corpus_file_name, test_sets_file, commonwords_file_name = None):
    start_time = time.time()
    fileRead(corpus_file_name, test_sets_file, commonwords_file_name)
    
    #Prints computational time of program
    print("--- %s seconds ---" % (time.time() - start_time))

main()
#Tested with
#main("sample.txt","set.txt","common.txt")
#with files from project description
