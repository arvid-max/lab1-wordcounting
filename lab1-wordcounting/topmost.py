import wordfreq
import sys
import urllib.request

# terminal: python topmost.py argv[1] argv[2] argv[3]

def main():
    # tokenize delar upp orden, countWords räknar orden, printTopMost skriver ut orden
    wordfreq.printTopMost(wordfreq.countWords(wordfreq.tokenize(lines),stopwords),num)

# öppnar en hemsida om argv[1] börjar med http:// eller https:// 
if sys.argv[1][:7] == "http://" or sys.argv[1][:8] == "https://":
    inp_url = urllib.request.urlopen(sys.argv[1])
    lines = inp_url.read().decode("utf8").splitlines()
# annars öppnar det en textfil
else:
    inp_file = open(sys.argv[1], encoding="utf-8")
    lines = inp_file.readlines()
    inp_file.close()

# öppnar en textfil för stopwords
inp_file = open(sys.argv[2], encoding="utf-8")
stopwords = inp_file.readlines()
inp_file.close()

# num är en int
num = int(sys.argv[3])

main() # kallar funktionen