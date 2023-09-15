import re

def tokenize(lines):
    words = [] # lista av ord
    for line in lines:
        line = str(line) # försäkrar att line är en string
        index = 0 # index räknar var i line man är
        start = index # start räknar var startvärdet för ett ord är
        while index < len(line):
            # om det är ett mellanslag eller symbol så splicar den upp det ordet som den höll på att räkna och det blir word
            if line[index].isspace() or not (line[index].isalpha() or line[index].isdigit()): 
                end = index
                word = line[start:end].lower()
                # delar upp bokstäverna från andra karaktärer och sedan lägger till de uppdelade orden i words
                splitwords = re.split('(\d+)', word)
                for splitword in splitwords:
                    words.append(splitword)
                start = index + 1
            # om det inte är en bokstav, nummer eller mellanslag så läggs den karaktären in i words
            if not (line[index].isalpha() or line[index].isdigit() or line[index].isspace()):
                words.append(line[index])
                start = index + 1
            index += 1 # ökar index med 1 varje loop
            # om det är den sista karaktären i line så läggs det sista ordet till i words
            if index == len(line): 
                end = index
                words.append(line[start:end].lower())
    # om det finns tomma strings i words så tas de bort
    while '' in words:
        words.remove('')  
    return words 

def countWords(words, stopWords):
    # en dictionary som har en string (själva ordet) och en int (antal gånger ordet uppstår)
    dict = {}
    frequencies = [] # en separat lista som lägger till ett ord flera gånger så man kan sedan räkna med count()
    for word in words:
        wordCount = 1
        # om ordet inte är med i stopWords så läggs den till i både frequencies och dict
        if word not in tokenize(stopWords): 
            frequencies.append(word)
            wordCount = frequencies.count(word)
            dict.update({word:wordCount})
    return dict

def printTopMost(frequencies, n):
    # sorterar frequencies efter antalet upprepningar, högst till lägst
    sortedList = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    # limitedList kopierar de n första värdena i sortedList
    limitedList = []
    count = 0
    while count < n and count < len(frequencies):
        limitedList.append(sortedList[count])
        count += 1
    # skriver ut listan
    for word in limitedList:
        # använder ljust och rjust för att justera mellanrummet mellan ordet word[0] och numret word[1]
        result = str(word[0]).ljust(15)+str(word[1]).rjust(10)
        print(result)