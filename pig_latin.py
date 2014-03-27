def pig_latinify_sentence(sentence):
    words = sentence.split(" ")
    vowels = "aeiou"
    for word in words:
        if word[0] in vowels:
            pig_latinify_word(word, vowel)
        else:
            pig_latinify_word(word, consonant)
        outstring = outstring + " " + word
    
    
def pig_latinify_word(word, string):
    ''' Receives word and vowel or consonant and
        Returns the latinified word'''
    consonant_ending = 'ay'
    vowel_ending = 'way'
    if string == vowel or word[0].isnumeric():
        return word + vowel_ending 
    else:
        out_word = word[1:] + word[0].lower() + consonant_ending
        return out_word

   
print(pig_latinify_sentence("Toby likes his art"))
print(pig_latinify_sentence("Testing 123"))
print(pig_latinify_sentence("Cook me some eggs"))
