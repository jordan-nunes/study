import string

word_frequency = {}
letter_frequency = {}

def remove_punctuations(text):
    text = text.strip()
    translation = str.maketrans('', '', string.punctuation)
    return text.translate(translation)

text = input("Write a text to be analysed: ")
text = remove_punctuations(text)
words = text.split(' ')
quantity = [1] * len(words)
tuple_word_frequency = zip(words, quantity)
word_frequency = dict(tuple_word_frequency)

def update_zero_dict_to_repeated_values(list_of_data, dict_of_data):
    for i, word in enumerate(words):
        j = i + 1
        while j < len(list_of_data):
            atual = list_of_data[j]
            if list_of_data[i] == list_of_data[j]:
                list_of_data.pop(j)
                dict_of_data[word] += 1
            else:
                j += 1
    return dict_of_data

#Continuee

word_frequency = update_zero_dict_to_repeated_values(words, word_frequency)