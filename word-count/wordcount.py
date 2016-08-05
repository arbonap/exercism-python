# -*- coding: utf-8 -*-
import re
def word_count(string):
    outputdict = {}
    string = string.lower().strip()
    wordlist = re.split(r'[-🖖.,_\s]+', string)
    for word in wordlist:
        word = word.replace("!!&@$%^&","")
        if word != "" and word != ":":
            if word in outputdict:
                outputdict[word] += 1
            else:
                outputdict[word] = 1
    return outputdict
