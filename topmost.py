import wordfreq
import sys

def main():
    wordfreq.printTopMost(wordfreq.countWords(lines,stopwords),num)

# öppna textfiler för lines och stopwords
inp_file = open(sys.argv[1], encoding="utf-8")
lines = wordfreq.tokenize(inp_file)
inp_file.close()
inp_file = open(sys.argv[2], encoding="utf-8")
stopwords = inp_file.readlines()
inp_file.close()
# num är en int
num = int(sys.argv[3])

main() # kallar funktionen