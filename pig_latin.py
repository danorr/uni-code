def pig_latinify_sentence(sentence):
    words = sentence.split(" ")
    length = len(words)
    vowels = "aeiou"
    ending = ""
    outstring = ""
    for i in range(len(words)): # what's the point of this?
        for word in words:
            if word[0] in vowels or word[0].isnumeric():
                ending = "way"
                if outstring:
                    outstring = outstring + " " + (word + ending)
                else:
                    outstring = word + ending
            #pig_latinify_word(word, ending)
            else:
                ending = "ay"
                if outstring:
                    outstring = outstring + " " + (word[1:] + word[0].lower() + ending)
                else:
                    outstring = word[1:] + word[0].lower() + ending                    
    return outstring
    
    
def pig_latinify_word(word, ending):
    ''' Receives word and vowel or consonant and
        Returns the latinified word'''
    if ending == "way":
        build_string(word + ending)
    else:
        build_string(word[1:] + word[0].lower() + ending)
    
    
def build_string(word):
    outstring = ""
    if not outstring == "":
        outstring = outstring + " " + word
    else:
        outstring = word
    return outstring

   
print(pig_latinify_sentence("Toby likes his art"))
print(pig_latinify_sentence("Testing 123"))
print(pig_latinify_sentence("Cook me some eggs"))
