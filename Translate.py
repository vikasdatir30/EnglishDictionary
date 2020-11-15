import json as js
import difflib as dflib
json_path ="D:\SrcData\json\data.json"
class Translate:
    def __init__(self):
        #loading dictionary file
        self.dict_data = js.load(open(json_path))
    def translate(self, word):
        if word in self.dict_data:
            return self.dict_data[word]
        #checking close matches
        elif len(dflib.get_close_matches(word, self.dict_data.keys(), cutoff=0.7)) > 0:
            user_choice = input("Did you mean %s instead of %s ? Enter y if Yes, N if No (Y/N) : " % (
            dflib.get_close_matches(word, self.dict_data.keys(), cutoff=0.7)[0], word))
            if user_choice.lower() == 'y':
                return self.dict_data[dflib.get_close_matches(word, self.dict_data.keys(), cutoff=0.7)[0]]
            elif user_choice.lower() == 'n':
                return "Word doesn't exists, pleas double check ..!"
            else:
                return "Wrong input..! Exiting ...!"
        else:
            return "Word doesn't exists, pleas double check ..!"

def main():
    obj= Translate()
    word= input('Enter a word : ')
    output =obj.translate(word)
    #formatting output if list
    if  type(output) == list:
        for line in output:
            print(line)
    else:
        print(output)

if __name__=='__main__':
    main()
