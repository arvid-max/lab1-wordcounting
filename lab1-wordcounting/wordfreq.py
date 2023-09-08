import urllib.request
import re

example = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
             '130 hampsters from the cancer labs down the hall, and',
             'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
             'said the source on a recent Geraldo interview.']
tests = [
    [],                               # 1
    [""],                             # 2
    ["   "],                          # 3
    ["This is a simple sentence"],    # 4
    ["I told you!"],                  # 5
    ["The 10 little chicks"],         # 6
    ["15th anniversary"],             # 7
    ["He is in the room, she said."]  # 8
]


def tokenize(lines):
    words = [] # lista av ord
    for line in lines:
        index = 0 # index räknar var i line man är
        start = index # start räknar var startvärdet för ett ord är
        while index < len(line):
            # om det är ett space eller symbol så splicar den upp det ordet som den höll på att räkna och det blir word
            if line[index].isspace() or not (line[index].isalpha() or line[index].isdigit()): 
                end = index
                word = line[start:end].lower()
                # delar upp bokstäverna från andra karaktärer och sedan lägger till de uppdelade orden i words
                splitwords = re.split('(\d+)', word) 
                for splitword in splitwords:
                    words.append(splitword) 
                start = index + 1
                
            # om det inte är en bokstav, nummer eller space så läggs den karaktären in i words
            if not (line[index].isalpha() or line[index].isdigit() or line[index].isspace()):
                words.append(line[index])
                start = index + 1

            index += 1 # ökar index med 1 varje loop

            # om det är den sista karaktären i line så läggs det sista ordet till i words
            if index == len(line): 
                end = index
                words.append(line[start:end].lower())

    # halv fix
    for word in words:
        if len(word) < 1:
            words.remove(word)

    return words

for test in tests:
    print(tokenize(test))
