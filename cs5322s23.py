from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

def WSD_Test_Rubbish(list): # List is a list of strings, with each string being a sentence containing the word "rubbish"
    options = wn.synsets('rubbish')
    options.pop()
    answer = [ ]
    for sentence in list:
        a1 = lesk(word_tokenize(sentence), 'rubbish', 'n', options)
        if a1.definition() == options[0].definition():
            answer.append(1)
        elif a1.definition() == options[1].definition():
            answer.append(2)

    return answer

def WSD_Test_Yarn(list):
    options = wn.synsets('yarn')
    options.pop()
    answer = [ ]
    for sentence in list:
        a1 = lesk(word_tokenize(sentence), 'yarn', 'n', options)
        if a1.definition() == options[0].definition():
            answer.append(1)
        elif a1.definition() == options[1].definition():
            answer.append(2)

    return answer


def WSD_Test_Tissue(list):
    options = wn.synsets('tissue')
    options.pop()
    answer = [ ]
    for sentence in list:
        a1 = lesk(word_tokenize(sentence), 'tissue', 'n', options)
        if a1.definition() == options[0].definition():
            answer.append(1)
        elif a1.definition() == options[1].definition():
            answer.append(2)

    return answer