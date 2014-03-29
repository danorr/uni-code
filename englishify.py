def englishify_sentence(sentence):
    ''' Takes a pig latin sentence and translates it with variations '''
    
    ending = ""
    outstring = ""
    words = sentence.split(" ")
    for word in words:
        ending = word[-3:]
        if ending == "way":
            englishify_word(word, ending)
            outstring += outstring + word
            print(outstring)
            #word1 = word.replace(ending, "")
            #word2 = word[-3:-2] + word[:-3]
            #print("word1:{:<10}\t word2:{:>10}".format(word1, word2))
        else:
            ending = "ay"
            word3 = word[-3] + word.strip(word[-3:])
            print("word3:{}".format(word3))
                
def englishify_word(word, ending):
    word1 = word.replace(ending, "")
    word2 = word[-3:-2] + word[:-3]
    return "(word1 or word2)"

    

print(englishify_sentence("oday ouyay antway anway eggway"))