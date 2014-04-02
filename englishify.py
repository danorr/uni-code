def englishify_sentence(sentence):
    ''' Takes a pig latin sentence and returns english translation '''
    
    wordlist = sentence.split(" ")
    answer = []
    converted_word = ""
    for word in wordlist:        
        converted_word = englishify_word(word)
        answer.append(converted_word)
    return " ".join(answer)
                  
def englishify_word(word):
    ''' Takes a pig latin word and translates it with variations '''
    ending = word[-3:]
    outstring = ""
    if ending == "way":      
        word1 = word.replace(ending, "")
        word2 = "{0}{1}".format(word[-3:-2], word[:-3])
        outstring = "({0} or {1})".format(word1, word2)
    else:
        ending = "ay"
        word3 = "{0}{1}".format(word[-3], word[:-3])
        outstring = word3   
    return outstring
              

    
english = englishify_sentence("obytay ikeslay ishay artway")
print(english)
print(englishify_sentence("oday ouyay antway anway eggway"))
english = englishify_sentence("onay hankyoutay iway amway allergicway otay eggsway")
print(english)
english = englishify_sentence("eggceptionallyway oringbay esttay asecay")
print(english)