import string

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

"""This function will capitalize the first letter of the first
word in every sentence"""
def sentence_capitalizer(text):
    # tokenize the text by sentences
    sentences = nltk.sent_tokenize(text)

    # for each sentence in the text, capitalize the first word
    for i in range(0, len(sentences)):
        sentences[i] = sentences[i].strip().capitalize()

    return " ".join(sentences)

"""This function will capitalize the proper nouns"""
def proper_noun_capitalizer(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    for tag in tagged:
        if tag[1] == "NNP" or tag[1] == "NNPS":
            tag[0] = tag[0].capitalize()

    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()


"""This function will be the main function of the program"""
def main_function():
    input_file = open("files/input_text.txt", 'r')
    input_text = input_file.read()

    print("Input Text is: " + input_text)

    #convert it to lower case
    input_text = input_text.lower()

    output_text = sentence_capitalizer(input_text)
    output_text = proper_noun_capitalizer(output_text)

    print("Output Text = " + output_text)
    input_file.close()



# run the main function
main_function()

