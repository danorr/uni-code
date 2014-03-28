def englishify_sentence(sentence):
    ''' Takes a pig latin sentence and translates it with variations '''
    
    ending = ""
    vowels = "aeiou"
    words = sentence.split(" ")
    for word in words:
        ending = word[-3:]
        if ending == "way":
            word1 = word.strip(ending)
            word2 = word[-3:-2] + word[:-3]
            print("word1:{:<10}\t word2:{:>10}".format(word1, word2))
        else:
            ending = "ay"
            word3 = word[-3] + word.strip(word[-3:])
            print("word3:{}".format(word3))
                
#def englishify_word(word):
    

print(englishify_sentence("oday ouyay antway anway eggway"))