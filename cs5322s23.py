from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

def WSD_Test_Rubbish(list): # List is a list of strings, with each string being a sentence containing the word "rubbish"
    answer = [ ]
    definition1 = '''
    Rubbish, also known as trash or scrap, refers to materials that have little or no value and are typically discarded. These may include things such as food waste, broken items, packaging materials, or other unwanted materials that are no longer useful. Rubbish can accumulate quickly in households, public places, and businesses, and must be disposed of properly to maintain a clean and healthy environment
    '''

    definition2 = '''
    Rubbish can also refer to nonsensical talk or writing, sometimes described as folderol, tripe, trumpery, wish-wash, or other similar terms. This kind of rubbish may include statements or claims that are absurd, illogical, or unsupported by evidence, as well as exaggerations, fabrications, or outright lies. Rubbish in this sense is often criticized for being deceptive, misleading, or distracting, and can be harmful when it is used to manipulate or deceive people.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))

    def1Words = word_tokenize(definition1)
    def2Words = word_tokenize(definition2)

    def1Filtered = [ ]
    def2Filtered = [ ]

    for word in def1Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def1Filtered.append(word)

    for word in def2Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def2Filtered.append(word)

    count = 1

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition
        
        for word in filtered_words:
            for otherWord in def1Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        print('Sentence ' + str(count) + ':', 'def1Similarity', def1Similarity / len(def1Words), 'def2Similarity', def2Similarity / len(def2Words))
        count += 1
        if (def1Similarity) > (def2Similarity):
            print(1)
            answer.append(1)
        else:
            print(2)
            answer.append(2)

    return answer

def WSD_Test_Yarn(list):
    answer = [ ]
    definition1 = '''
    Yarn can refer to the act of giving an account or narrating a story, typically one that is detailed or elaborate. The term is often used informally to describe a long, rambling tale that is embellished or exaggerated for effect. Yarns may be told for entertainment, to convey information, or simply to pass the time. They can take many forms, from personal anecdotes to fictional narratives.    '''
    definition2 = '''
    Yarn can also refer to a fine cord of twisted fibers, such as cotton, silk, wool, or nylon, that is commonly used in sewing, weaving, and knitting. Yarn is available in a wide range of colors, textures, and thicknesses, and can be made from natural or synthetic materials. It is used to create a variety of textile products, including clothing, blankets, and home decor items. The quality and characteristics of yarn can vary depending on the type of fiber used, the twist and ply of the yarn, and other factors.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))

    def1Words = word_tokenize(definition1)
    def2Words = word_tokenize(definition2)

    def1Filtered = [ ]
    def2Filtered = [ ]

    for word in def1Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def1Filtered.append(word)

    for word in def2Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def2Filtered.append(word)


    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition
        
        for word in filtered_words:
            for otherWord in def1Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        if (def1Similarity) > (def2Similarity):
            answer.append(1)
        else:
            answer.append(2)

    return answer


def WSD_Test_Tissue(list):
    answer = [ ]
    definition1 = '''
    Tissue refers to a group or layer of cells in an organism that share a similar structure and function. Tissues can be found in a variety of living organisms, including plants and animals, and they work together to perform specific functions such as providing structural support, transporting nutrients, or facilitating communication between cells. Examples of tissues in humans include muscle tissue, nerve tissue, and connective tissue.
    '''
    definition2 = '''
    Tissue can also refer to a soft, thin, usually translucent paper that is commonly used for personal hygiene purposes or to wrap delicate objects. Tissue paper is often made from recycled materials and is available in a variety of colors, textures, and patterns. It is commonly used for wrapping gifts, wiping one's nose or face, or as a decorative element in crafting and other creative projects. Tissue paper is valued for its softness, light weight, and ease of use.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = set(stopwords.words('english'))

    def1Words = word_tokenize(definition1)
    def2Words = word_tokenize(definition2)

    def1Filtered = [ ]
    def2Filtered = [ ]

    for word in def1Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def1Filtered.append(word)

    for word in def2Words: #filters out stop words
        if word not in stopWords:
            word = lemmatizer.lemmatize(word) #lemmatizes words
            def2Filtered.append(word)


    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filtered_words = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filtered_words.append(word)

        def1Similarity = 0 #the sentence's similarity to the first definition
        def2Similarity = 0 #the sentence's similarity to the second definition
        
        for word in filtered_words:
            for otherWord in def1Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def1Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def1Similarity += 0

            for otherWord in def2Filtered:
                try:
                    word1 = wn.synset(word + '.n.01')
                    word2 = wn.synset(otherWord  + '.n.01')
                    def2Similarity += word1.wup_similarity(word2) #calculates how similar the definitions of the two words are
                except:
                    def2Similarity += 0

        if (def1Similarity) > (def2Similarity):
            answer.append(1)
        else:
            answer.append(2)

    return answer
