class FileReader:
  

    def getReadSetsFile(self):
        return self.readSetsFile
    
    def getReadCommonWordsFile(self):
        return self.readCommonWordFile
   
    def punctuationMaker(self, sentence):
    #punctuation marks
        for ch in [',',"\'",'\"',':',';','[',']','(',')']:
            if ch in sentence:
                sentence = sentence.replace(ch, "")
        sentence = sentence.replace('\n', " ")
        sentence = sentence.replace('--', " ")
        return sentence

    
    def readCommonWordsFile(self, commonwords_file_name = None):
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
    
    
    def readSets(self,fileName):
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

    def openFile(self, text):
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
                            tempword = self.punctuationMaker(tempword.lower())
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



			