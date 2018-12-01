
import math
import time
from Profile import Profile
from ProfileSet import ProfileSet
from ProfileDictionary import ProfileDictionary

def readCommonWordsFile(commonwords_file_name = None):
    common = []
    if(commonwords_file_name):
        try:
            commonFile = open(commonwords_file_name,'r')
            common = list(commonFile.read().splitlines())
            for word in common:
                    word = word.lower()
        except IOError as e:
            print("Error reading file: " + commonwords_file_name + " " + str(e) + "\n")
            print("Running without common word file: ")
    return common

def createSets(fileName):
    dictOfSets = {}
    tempWords = []
    try:
        file = open(fileName, 'r')
        words = file.readlines()
        for word in words:
            if(" " not in word.lstrip().rstrip()):
                if word == "\n":
                    if(tempWords):
                        dictOfSets[tempWords[0]] = tempWords
                        tempWords = []
                elif (word == words[len(words)-1]):
                    tempWords.append(word.strip("\n").lower())
                    dictOfSets[tempWords[0]] = tempWords
                    tempWords = []            
                else:
                    tempWords.append(word.strip("\n").lower())
            else:
                raise IOError("Error: set file has incorrect format. Check formatting of: " + fileName + " " + "\n")
    except PermissionError as e:
        raise IOError("Error reading file. Check file read permissions of: " + fileName + " " + str(e) + "\n")
    except IOError as e:
        print("Error reading set file: " + fileName + str(e))
        raise e
    except Exception as e:
        print("Error reading set file: " + fileName + str(e))
        raise IOError
    return(dictOfSets)

#Opens the text file which words are to be read from, with error handling
def openFile(text):
    sentences = []
    try:
        file = open(text, 'r')
        sentences = []
        endOfSentence = ['.','!','?']
        word = ''
        with file as data:
            tempword = ''
            for line in data:
                for word in line:
                    if(word in endOfSentence):
                        tempword = punctuationMaker(tempword.lower())
                        sentences.append(tempword)
                        tempword = ''
                    else:
                        tempword += word
            if(tempword.strip('\n') != ''):
                raise IOError("Error: Reached end of file with no end of line character")
    except PermissionError as e:
            raise IOError("Error reading file. Check file read permissions of: " + text + " " + str(e) + "\n")
    except IOError as e:
        raise IOError("Error reading file: " + text + str(e))
    except Exception as e:
        raise IOError("Error reading file: " + text + str(e))
    return sentences


#Reads a file with [',',"\'",'\"',':',';','[',']','(',')'] as space characters
#and [.,?,!] as fullstop
def punctuationMaker(sentence):
    #punctuation marks
    for ch in [',',"\'",'\"',':',';','[',']','(',')']:
        if ch in sentence:
            sentence = sentence.replace(ch, "")
    sentence = sentence.replace('\n', " ")
    sentence = sentence.replace('--', " ")
    return sentence

#Creates profiles and adds associated words to each profile

           
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
    try:
        sentences = openFile(corpus_file_name)
        profileSets = createSets(test_sets_file)
        
        
        #If sentences and profiles exist, read common words file
        if(sentences and profileSets):
            commonWords = readCommonWordsFile(commonwords_file_name);
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
                
        #Print sysnonym for target word is set file
        
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
