#THE TASK: Create a function that takes in two strings as a parameter.If each string equals an anagram, return True as an output, -
########## If each word does not equal an anagram return False.
#Anagram Definiton: Two words that are made up of the same letters but are aranged in a different order to create a new word.
#Edgecase check: An anagram must contain the same number of characters as well.

#What are the ways I can check if its an anagram?
#Main goal: Figure out if each word has the same alphabetical characters and if they equal the same length
########### I could use a 'len' function to check for equal length, and I can use the 'sorted' function in python to determine
########### if each string shares the same alphabetical characters. 


''''
PSEUDOCODE

DEF AnagramChecker(s1,s2)
    #Check if both strings are equal length
    IF len s1 == len s2
        #Check if both strings share the same letters
        IF sorted s1 == sorted s2
            #If they are, return TRUE
            RETURN TRUE
        ELSE
            RETURN FALSE    
    ELSE
        RETURN False 

END
'''

def anagram_checker(string1,string2):
    if len(string1) == len(string2):
        if sorted(string1) == sorted(string2):
            print ('True')
        else:
            print ('False')
    else:
        print ('False')

anagram_checker('tako','coat')