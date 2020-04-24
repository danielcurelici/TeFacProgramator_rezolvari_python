import re

def read_text(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text
    
def first_regex(sentence):
    return re.findall("\d{2}:\d{2}", sentence)
    
def second_regex(sentence):
    return re.findall("(\d{2}\/\d{2}\/\d{4})|(\d{2}\/\d{2}\/\d{2})", sentence)
    
def third_regex(sentence):
    return re.findall("[^:\/\d]+(\d+([,\.]\d+)?)[^:\/\d]+", sentence)
    
def fourth_regex(sentence):
    return re.findall("[^\.\r\n\w][A-Z][a-z]+", sentence)

def run_regex_on_sentences(regex_function, sentences):
    print("Results for " + regex_function.__name__)
    for sentence in sentences:
        print(regex_function(sentence))
    
if __name__ == "__main__":
    sentences = [x.strip().replace('\n',' ') for x in read_text("in.txt").split(".")]
    print(sentences)
    run_regex_on_sentences(first_regex, sentences)
    run_regex_on_sentences(second_regex, sentences)
    run_regex_on_sentences(third_regex, sentences)
    run_regex_on_sentences(fourth_regex, sentences)