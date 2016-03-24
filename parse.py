from nltk.corpus import stopwords
def parse():
    with open("raw_files/DemWinsconsin", "r") as f:
        data = f.readlines()
    stop = stopwords.words('english')
    speech = ""
    speaker = ""
    for line in data:
        if ": " in line:
            if speech != "":
                speaker = line[0:line.find(":")]
                if speaker == "SANDERS":
                    print speech
                    speech = speech.replace('...', " ").replace(',', " ").replace('?', " ").replace('--', "").replace('\n', " ").replace("  ", " ")
                    words = speech.split(" ")
                    for word in words:
                        word = word.strip('.')
                        if word.lower() not in stop:
                            if "(" not in word:
                                if not word.isdigit():
                                    pass
                                    # print word
                speech = ""
            else:
                speech += line
        else:
            speech += line

parse()
