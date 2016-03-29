#!/usr/bin/env python
"""Analyzes most used words in 2016 Presidential Debates.

The Democrats analyzed are Bernie Sanders and Hillary Clinton.
The Republicans analyzed are Donald Trump, John Kasich and Ted Cruz.

Requires (END) to be placed at end of transcript and each
speaker to be marked with their name, a colon, and a space. For example,
"SANDERS: Judy, one area very briefly..."

Requires nltk stopwords to be installed.

Command line arguments are required.
python parse.py <transcript> <party> <number of words> <store?>
transcript: File name of transcript. Must be stored in raw_files folder.
party: Political party of debate.
number of words: Number of words to return. For example, 5 would return
top 5 most used words.
store?: Whether or not to store in results.json. true if desired.

Author: Roy Xu
Email: royxu652@gmail.com
Github: https://github.com/captiosus
"""

import sys
import json
from nltk.corpus import stopwords

def main(argv):
    #  Check validity of command line arguments.
    if argv[1] != "Democrat":
        if argv[1] != "Republican":
            print "Invalid Party"
            return
    if not argv[2].isdigit():
        print "Invalid Amount"
        return
    #  Declare dictionaries for each candidate.
    total = {}
    sanders = {}
    clinton = {}
    trump = {}
    kasich = {}
    cruz = {}
    jsonData = {}
    #  Open transcipt file and store in array.
    with open("raw_files/" + argv[1] + "/" + argv[0], "r") as f:
        data = f.readlines()
    #  Declare stopwords and add several not included.
    stop = stopwords.words('english')
    stop.append("us")
    stop.append("it's")
    stop.append("you're")
    stop.append("they're")
    stop.append("mr")
    stop.append("i'm")
    stop.append("i've")
    stop.append("we've")
    stop.append("got")
    stop.append("get")
    stop.append("go")
    stop.append("that's")
    stop.append("we're")
    stop.append("we'll")
    stop.append("don't")
    stop.append("\"")
    #  Speech stores current speaker's statement.
    speech = ""
    speaker = ""
    for line in data:
        #  Check if we are at line indicating new speaker or end of file.
        #  We use the ": " as indication of end of a speaker's speech and
        #  the beginning of new speaker.
        if ": " in line[:15] or "(END)" in line:
            #  Checks if this is first speaker. Only case when this is false.
            if speech != "":
                #  Find speaker from location of ":" in speech.
                speaker = speech[0:speech.find(":")]
                #  Remove the speaker from speech.
                speech = speech[speech.find(":")+1:]
                #  Filter out punctuation.
                speech = speech.replace('...', " ").replace(',', " ").replace('?', " ").replace('-', "").replace('\n', " ").replace("  ", " ")
                #  Create array of words in speech.
                words = speech.split(" ")
                for word in words:
                    #  More punctuation removal.
                    word = word.strip('.')
                    #  Case of words does not matter. So all lowercase.
                    word = word.lower()
                    #  Remove cases of (APPLAUSE) in transcript.
                    if "(" not in word:
                        #  Remove stopwords.
                        if word not in stop:
                            #  Remove numbers.
                            if not word.isdigit():
                                #  Due to multiple spaces in succession, words
                                #  may be just a space. Removes instances.
                                if word != "":
                                    #  Check party.
                                    if argv[1] == "Democrat":
                                        if speaker == "SANDERS":
                                            #  Check if word has been recorded.
                                            #  Adds one more instance if it has.
                                            if word in sanders:
                                                sanders[word] += 1
                                            #  If not, records it.
                                            else:
                                                sanders[word] = 1
                                            if word in total:
                                                total[word] += 1
                                            else:
                                                total[word] = 1
                                        elif speaker == "CLINTON":
                                            if word in clinton:
                                                clinton[word] += 1
                                            else:
                                                clinton[word] = 1
                                            if word in total:
                                                total[word] += 1
                                            else:
                                                total[word] = 1
                                    elif argv[1] == "Republican":
                                        if speaker == "TRUMP":
                                            if word in trump:
                                                trump[word] += 1
                                            else:
                                                trump[word] = 1
                                            if word in total:
                                                total[word] += 1
                                            else:
                                                total[word] = 1
                                        elif speaker == "KASICH":
                                            if word in kasich:
                                                kasich[word] += 1
                                            else:
                                                kasich[word] = 1
                                            if word in total:
                                                total[word] += 1
                                            else:
                                                total[word] = 1
                                        elif speaker == "CRUZ":
                                            if word in cruz:
                                                cruz[word] += 1
                                            else:
                                                cruz[word] = 1
                                            if word in total:
                                                total[word] += 1
                                            else:
                                                total[word] = 1
                #  Resets speech and adds next line.
                speech = ""
                speech += line
            else:
                #  If first speaker, add line.
                speech += line
        else:
            # If not new speaker, add line.
            speech += line
    if argv[3] == "true":
        with open('results.json') as data_file:
            try:
                jsonData = json.load(data_file)
            except ValueError, e:
                jsonData = {"Total":{"Democrat":{"Sanders":{}, "Clinton":{}}, "Republican":{"Trump":{},"Kasich":{},"Cruz":{}}, "Total":{}}, "Democrat":{"Sanders":{},"Clinton":{}},"Republican":{"Trump":{},"Kasich":{},"Cruz":{}}}
    print "Total Most Used Words"
    #  Create temporary dictionary, because removal of key required.
    totalTemp = total
    #  Loops for specified amount
    for x in range(int(argv[2])):
        #  Find key with maximum value.
        mostWord = max(totalTemp, key=totalTemp.get)
        if argv[3] == "true":
            if mostWord not in sanders:
                sanders[mostWord] = 0
            if mostWord not in clinton:
                clinton[mostWord] = 0
            if mostWord not in trump:
                trump[mostWord] = 0
            if mostWord not in kasich:
                kasich[mostWord] = 0
            if mostWord not in cruz:
                cruz[mostWord] = 0
            if mostWord not in jsonData["Total"]["Total"]:
                jsonData["Total"]["Total"][mostWord] = 0
            if mostWord not in jsonData["Total"]["Democrat"]["Sanders"]:
                jsonData["Total"]["Democrat"]["Sanders"][mostWord] = 0
            if mostWord not in jsonData["Total"]["Democrat"]["Clinton"]:
                jsonData["Total"]["Democrat"]["Clinton"][mostWord] = 0
            if mostWord not in jsonData["Total"]["Republican"]["Trump"]:
                jsonData["Total"]["Republican"]["Trump"][mostWord] = 0
            if mostWord not in jsonData["Total"]["Republican"]["Kasich"]:
                jsonData["Total"]["Republican"]["Kasich"][mostWord] = 0
            if mostWord not in jsonData["Total"]["Republican"]["Cruz"]:
                jsonData["Total"]["Republican"]["Cruz"][mostWord] = 0
            if argv[1] == "Democrat":
                jsonData["Total"]["Democrat"]["Sanders"][mostWord] += sanders[mostWord]
                jsonData["Total"]["Democrat"]["Clinton"][mostWord] += clinton[mostWord]
            elif argv[1] == "Republican":
                jsonData["Total"]["Republican"]["Trump"][mostWord] += trump[mostWord]
                jsonData["Total"]["Republican"]["Kasich"][mostWord] += kasich[mostWord]
                jsonData["Total"]["Republican"]["Cruz"][mostWord] += cruz[mostWord]
            jsonData["Total"]["Total"][mostWord] += total[mostWord]

        print str(x+1) + ": " + mostWord + " - " + str(totalTemp[mostWord])
        #  Deletes this key after printing and loops again for next highest.
        del totalTemp[mostWord]
    if argv[1] == "Democrat":
        print "Sanders Most Used Words"
        sandersTemp = sanders
        for x in range(int(argv[2])):
            mostWord = max(sandersTemp, key=sandersTemp.get)
            if argv[3] == "true":
                if mostWord in jsonData["Democrat"]["Sanders"]:
                    jsonData["Democrat"]["Sanders"][mostWord] += sandersTemp[mostWord]
                else:
                    jsonData["Democrat"]["Sanders"][mostWord] = sandersTemp[mostWord]
            print str(x+1) + ": " + mostWord + " - " + str(sandersTemp[mostWord])
            del sandersTemp[mostWord]
        print "Clinton Most Used Words"
        clintonTemp = clinton
        for x in range(int(argv[2])):
            mostWord = max(clintonTemp, key=clintonTemp.get)
            if argv[3] == "true":
                if mostWord in jsonData["Democrat"]["Clinton"]:
                    jsonData["Democrat"]["Clinton"][mostWord] += clintonTemp[mostWord]
                else:
                    jsonData["Democrat"]["Clinton"][mostWord] = clintonTemp[mostWord]
            print str(x+1) + ": " + mostWord + " - " + str(clintonTemp[mostWord])
            del clintonTemp[mostWord]
    elif argv[1] == "Republican":
        print "Trump Most Used Words"
        trumpTemp = trump
        for x in range(int(argv[2])):
            mostWord = max(trumpTemp, key=trumpTemp.get)
            if argv[3] == "true":
                if mostWord in jsonData["Republican"]["Trump"]:
                    jsonData["Republican"]["Trump"][mostWord] += trumpTemp[mostWord]
                else:
                    jsonData["Republican"]["Trump"][mostWord] = trumpTemp[mostWord]
            print str(x+1) + ": " + mostWord + " - " + str(trumpTemp[mostWord])
            del trumpTemp[mostWord]
        print "Kasich Most Used Words"
        kasichTemp = kasich
        for x in range(int(argv[2])):
            mostWord = max(kasichTemp, key=kasichTemp.get)
            if mostWord in jsonData["Republican"]["Kasich"]:
                jsonData["Republican"]["Kasich"][mostWord] += kasichTemp[mostWord]
            else:
                jsonData["Republican"]["Kasich"][mostWord] = kasichTemp[mostWord]
            print str(x+1) + ": " + mostWord + " - " + str(kasichTemp[mostWord])
            del kasichTemp[mostWord]
        print "Cruz Most Used Words"
        cruzTemp = cruz
        for x in range(int(argv[2])):
            mostWord = max(cruzTemp, key=cruzTemp.get)
            if mostWord in jsonData["Republican"]["Cruz"]:
                jsonData["Republican"]["Cruz"][mostWord] += cruzTemp[mostWord]
            else:
                jsonData["Republican"]["Cruz"][mostWord] = cruzTemp[mostWord]
            print str(x+1) + ": " + mostWord + " - " + str(cruzTemp[mostWord])
            del cruzTemp[mostWord]

    if argv[3] == "true":
        with open('results.json', 'w') as outfile:
            json.dump(jsonData, outfile)

if __name__ == "__main__":
    if (sys.argv[1]=="-all"):
        for x in range(8):
            main(["Dem"+str(x+1), "Democrat", "20", "true"])
        for x in range(12):
            main(["Rep"+str(x+1), "Republican", "20", "true"])
    else:
        main(sys.argv[1:])
