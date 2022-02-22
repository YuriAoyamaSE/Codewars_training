"""
Write a function that takes in a string of one or more words, and returns the
same string, but with all five or more letter words reversed (Just like the
name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test" spinWords( "This is
another test" )=> returns "This is rehtona test"
"""
def spin_words(sentence):
    frase = []
    for item in sentence.split():
        if len(item) >= 5:
            frase.append(item[::-1])
        else:
            frase.append(item)

    return " ".join(frase)


