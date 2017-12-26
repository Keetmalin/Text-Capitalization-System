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
        sentences[i] = sentences[i].strip()[0].capialize()

    return sentences.join(sentences, " ")

"""This function will be the main function of the program"""
def main_function():
    input_text = input()
    sentence_capitalizer(input_text)


# run the main function
main_function()

