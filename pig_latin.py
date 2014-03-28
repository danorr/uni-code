def pig_latinify_sentence(sentence):
    ''' Receives a sentence and returns an altered sentence '''
    
    # split the words and make a new list
    words = sentence.split(" ")
    # set up variables to test against or add to
    vowels = "aeiou"
    ending = ""
    outstring = ""
    #loop through list of words
    for word in words:
        # if word begins with vowel or is numeric set ending = "way"
        if word[0] in vowels or word[0].isnumeric():
            ending = "way"
            if outstring:
                outstring = outstring + " " + (word + ending)
            else:
                outstring = word + ending
        else:
            # word begins with a consonant, set ending = "ay"
            ending = "ay"
            if outstring:
                outstring = outstring + " " + (word[1:] + word[0] + ending)
            else:
                outstring = word[1:] + word[0].lower() + ending                    
    return outstring.strip().lower()
    
    
#def pig_latinify_word(word, ending):
    #''' Receives word and vowel or consonant and
        #Returns the latinified word'''
    #if ending == "way":
        #build_string(word + ending)
    #else:
        #build_string(word[1:] + word[0].lower() + ending)
    
    
#def build_string(word):
    #outstring = ""
    #if not outstring == "":
        #outstring = outstring + " " + word
    #else:
        #outstring = word
    #return outstring

   
print(pig_latinify_sentence("Toby likes his art"))
print(pig_latinify_sentence("Testing 123"))
print(pig_latinify_sentence("Cook me some eggs"))

