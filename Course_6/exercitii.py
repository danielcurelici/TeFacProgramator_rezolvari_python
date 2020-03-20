import json

def read_txt_file(filename):
    """
    This function reads a file and returns its content as a list of strings,
    where each element represents a line in the file.
    Parameters:
        -filename : string  => the path to the file to be read
    Returns:
        -a list of strings
    """
    with open(filename, "r") as f:
        data = f.read()
    return data

def multiple_split(to_split, delimiters):
    """
    This function splits a string by multiple delimiters, withour using the 
    re (regulat expresions) module. 
    Parameters:
        -to_split   :   string  => the string which is required to be split
        -delimiters :   string  => a string containing the delimiters which 
                                are to be used for splitting. Example: If you
                                want to split a string by the following 
                                delimiters: "a", "x", "?", then use the string
                                "ax?" for this parameter
    Returns:
        -a list of strings, containing the substrings extracted from the string
        given as parameter after the split is done
    """
    start = 0
    result = []
    for i in range(len(to_split)):
        if to_split[i] in delimiters:
            result.append(to_split[start:i])
            start = i + 1
    return result    

def word_appearances(words):
    """
    This function creates a dictionary whose keys are the elements from a list
    and the values are the number of appereances of these elements in the list.
    This is the short version.
    Parameters:
        -words  :   list    => a list containing strings
    Returns:
        -a dictionary containing the words count
    """
    app_dict = {key : words.count(key) for key in words if key}
    return app_dict
   
def word_appearances_long(words):
    """
    This function creates a dictionary whose keys are the elements from a list
    and the values are the number of appereances of these elements in the list.
    This is the long version, where we iterate over the elements and if we
    find the element as a key in the dictionary, then we increment the value
    associated to the key, otherwise, we insert the element in the dictionary
    as a new key, with the value 1 associated.
    Parameters:
        -words  :   list    => a list containing strings
    Returns:
        -a dictionary containing the words count
    """
    app_dict = {}
    for word in words:
        if word:
            if word in app_dict.keys():
                app_dict[word] += 1
            else:
                app_dict[word] = 1
    return app_dict        
    
def word_frequencies(word_dict, num_words):
    """
    This function creates a dictionary containing word frequency based on
    a dictionary containing word count.
    Parameters:
        -word_dict  :   dictionary  => a dictionary containing word count
        -num_words  :   number      => a number representing the total
                                    number of words
    Returns:
        -a dictionary containing word frequency
    """
    freq_dict = {}
    for key in word_dict:
        freq_dict[key] = round(word_dict[key] / num_words, 6) * 100
    return freq_dict
        
#This function doesn't work because we change the dictionary while we iterate
#over it
def prune_dict_wrong(dict):
    for key in dict:
        if dict[key] >= 1:
            del dict[key]
            
def prune_dict(dict):
    """
    This function prunes the dictionary, by removing the keys that have a 
    frequency greater or equal to 1%.
    Parameters:
        -dict   :   dictionary  => The dictionary to be pruned
    """
    to_remove = []
    for key in dict:
        if dict[key] >= 1:
            to_remove.append(key)
    for key in to_remove:
        del dict[key]
    
def write_dict_to_file(dict, filename):
    """
    This function writes a dictionary to a file.
    Parameters:
        -dict       :   dictionary  => The dictionary to be written
        -filename   :   string      => The name of the file
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent = 4)
    
def read_json_from_file(filename):
    """
    Reads a dictionary from a json file.
    Parameters:
        -filename   :   string  => The name of the file
    Returns:
        -the dictionary read from the file
    """
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data
    
def get_top_freq_words(dict, top_num):
    """
    This function extracts from a frequency dictionary the top least frequent
    keys. First, it extracts a list of keys sorted by the values associated.
    Afterwards, it creates a new dictionary containing these keys and their
    values.
    Parameters:
        -dict       :   dictionary  => The frequency dictionary
        -top_num    :   number      => The number of elements to be extracted
    Returns:
        -the dictionary containing the top least frequent keys
    """
    top_keys = sorted(dict, key=dict.get)[:top_num]
    top_dict = { key : dict[key] for key in top_keys}
    return top_dict
    
if __name__ == "__main__":
    filename = "in_file.txt"
    
    #We read the file containing a text
    data = read_txt_file(filename)
    print(data)
    
    #We split the text by the desired delimiters
    words = multiple_split(data, " ,.\n")
    print(words)

    #We create the appearances dictionary
    app_dict = word_appearances_long(words)
    print(app_dict)
    
    #We create the frequencies dictionary based on the appearances dictionary
    freq_dict = word_frequencies(app_dict, len(words))
    print(freq_dict)
    
    #We prune the frequencies dictionary, by removing the most common words.
    #We check that some keys were removed by checking the number of keys in the
    #dictionary before and after.
    print(len(freq_dict.values()))
    prune_dict(freq_dict)
    print(len(freq_dict.values()))
    
    #We write the dictionary to file
    write_dict_to_file(freq_dict, "word_frequencies.json")
    
    #We read the dictionary from file and print it indented
    dict = read_json_from_file("word_frequencies.json")
    print(json.dumps(dict, indent=4))
    
    #We create the dictionary with the least frequent 10 words
    top_dict = get_top_freq_words(dict, 10)
    print(json.dumps(top_dict, indent=4))