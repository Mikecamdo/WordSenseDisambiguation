from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

def WSD_Test_Rubbish(list): # List is a list of strings, with each string being a sentence containing the word "rubbish"
    answer = [ ]
    definition1 = 'rubbish, trash, scrap (worthless material that is to be disposed of)'
    definition2 = 'folderol, rubbish, tripe, trumpery, trash, wish-wash, applesauce, codswallop (nonsensical talk or writing)'

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        lemmatizer = WordNetLemmatizer()
        stopWords = set(stopwords.words('english'))
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition

        def1Words = word_tokenize(definition1)
        def2Words = word_tokenize(definition2)
        
        for word in filtered_words:
            for otherWord in def1Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        if def1Similarity > def2Similarity:
            answer.append(1)
        else:
            answer.append(2)

    return answer

def WSD_Test_Yarn(list):
    answer = [ ]
    definition1 = 'narration, recital, yarn (the act of giving an account describing incidents or a course of events)'
    definition2 = 'thread, yarn (a fine cord of twisted fibers (of cotton or silk or wool or nylon etc.) used in sewing and weaving)'

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        lemmatizer = WordNetLemmatizer()
        stopWords = set(stopwords.words('english'))
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition

        def1Words = word_tokenize(definition1)
        def2Words = word_tokenize(definition2)
        
        for word in filtered_words:
            for otherWord in def1Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        if def1Similarity > def2Similarity:
            answer.append(1)
        else:
            answer.append(2)

    return answer


def WSD_Test_Tissue(list):
    answer = [ ]
    definition1 = 'tissue (part of an organism consisting of an aggregate of cells having a similar structure and function)'
    definition2 = 'tissue, tissue paper (a soft thin (usually translucent) paper)'

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        lemmatizer = WordNetLemmatizer()
        stopWords = set(stopwords.words('english'))
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition

        def1Words = word_tokenize(definition1)
        def2Words = word_tokenize(definition2)
        
        for word in filtered_words:
            for otherWord in def1Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Words:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        if def1Similarity > def2Similarity:
            answer.append(1)
        else:
            answer.append(2)

    return answer
