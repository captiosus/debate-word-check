# debate-word-check
by
## Team Glasses-Jacket-Shirt
The data we are using records the number of times certain words are said by presidental candidates in the primary debates that have taken place so far.

We will be parsing transcripts of debates and finding the most commonly said words, which are then displayed as circles of size corresponding to how many times they are said. The viewer should be able to sort by party and candidate. Also, hovering over the circles will display further information, such as how many times the word was said.

Taking transcripts of recent political debates from here:

Republican:
* http://time.com/3988276/republican-debate-primetime-transcript-full-text/
* http://time.com/4037239/second-republican-debate-transcript-cnn/
* https://www.washingtonpost.com/news/the-fix/wp/2015/10/28/the-third-republican-debate-annotating-the-transcript/
* http://time.com/4107636/transcript-read-the-full-text-of-the-fourth-republican-debate-in-milwaukee/
* http://time.com/4150816/republican-debate-las-vegas-transcript/
* http://time.com/4182096/republican-debate-charleston-transcript-full-text/
* https://www.washingtonpost.com/news/the-fix/wp/2016/01/28/7th-republican-debate-transcript-annotated-who-said-what-and-what-it-meant/
* http://time.com/4210921/republican-debate-transcript-new-hampshire-eighth/
* http://time.com/4224275/republican-debate-transcript-south-carolina-ninth/
* http://time.com/4238363/republican-debate-tenth-houston-cnn-telemundo-transcript-full-text/
* http://time.com/4247496/republican-debate-transcript-eleventh-detroit-fox-news/
* http://time.com/4255181/republican-debate-transcript-twelfth-cnn-miami/

Democrats:
* http://time.com/4072553/democratic-debate-transcript-primetime-cnn/
* http://time.com/4113434/transcript-read-the-full-text-of-the-second-democratic-debate/
* http://time.com/4156144/democratic-debate-third-new-hampshire-abc-transcript/
* http://time.com/4183952/democratic-debate-full-text-hillary-clinton-bernie-sanders/
* http://time.com/4208869/democratic-debate-transcript-full-text-new-hampshire-fifth/
* http://time.com/4218812/democratic-debate-transcript-full-text-milwaukee-sixth/
* http://time.com/4249183/democratic-debate-flint-full-text-transcript-seventh/
* http://time.com/4253623/democratic-debate-eighth-miami-transcript-full-text/
* https://www.washingtonpost.com/news/the-fix/wp/2016/03/09/transcript-the-post-univision-democratic-debate-annotated/

These transcripts are parsed with the parse.py file. In order to be parsed, the transcript required an "(END)" to be placed at end of transcript and each speaker to be marked with their name, a colon, and a space. 
For example, "SANDERS: Judy, one area very briefly..."
The parsing file required nltk stopwords to be installed.
The file must be ran with the command line arguments shown below.
python parse.py <transcript> <party> <number of words> <store?>
transcript: File name of transcript. Must be stored in raw_files folder.
party: Political party of debate.
number of words: Number of words to return. For example, 5 would return
top 5 most used words.
store?: Whether or not to store in results.json. true if desired, false if not.

