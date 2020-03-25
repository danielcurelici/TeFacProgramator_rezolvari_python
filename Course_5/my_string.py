def capitalize_sentences(text):
    """
    This function splits a text using the "." as delimiter, strips any leading
    whitespaces and then capitalizes the first letter for each substring (the
    substrings represent sentences). Afterwards, the leading whitespaces and
    the dot (".") are added back.
    Parameters:
        -text   :   string  => The text to be processed
    Returns:
        -the text after the processing
    """
    sentences = text.split(".")
    result = ""
    for s in sentences:
        if s:
            result += s.strip().capitalize() + ". "
    return result
    
def letter_count_dict(text):
    """
    This function takes a string and creates a dictionary whose keys are 
    letters and the values are the number of appearances of each letter
    in the string. This is the short version.
    Parameters:
        -text   :   string  => The text to be processed
    Returns:
        -the created dictionary
    """
    dict = {key : text.count(key) for key in text if key.isalpha()}
    return dict
    
def letter_count_dict_long(text):
    """
    This function takes a string and creates a dictionary whose keys are 
    letters and the values are the number of appearances of each letter
    in the string. This is the long version, where we iterate over each
    character in the string and if it is a letter, we check if the character
    exists as a key in the dictionary and increment its value if true. 
    Otherwise, we create a new key representing the character and initialize
    its value with 1.
    Parameters:
        -text   :   string  => The text to be processed
    Returns:
        -the created dictionary
    """
    dict = {}
    for key in text:
        if key.isalpha():
            if key in dict.keys():
                dict[key] += 1
            else:
                dict[key] = 1
    return dict 
   
if __name__ == "__main__":
    #we initialize our string with a nice roman march song
    text = "supra terram Britannorum volat aquila legionum. legio aeterna \
victrix. a ferventi aestuosa Libya volat aquila legionum supra terram \
Britannorum."

    #we call the capitalization function and print the result
    new_text = capitalize_sentences(text)
    print(new_text)
    
    #we call both functions for letter count and print the dictionaries for 
    #comparison
    letter_dict = letter_count_dict(text)
    letter_dict2 = letter_count_dict_long(text)
    print(letter_dict)
    print(letter_dict2)