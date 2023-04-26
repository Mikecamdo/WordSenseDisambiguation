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
    Rubbish can also refer to nonsensical talk or writing, sometimes described as folderol, tripe, trumpery, wish-wash, or other similar terms. This kind of rubbish may include statements or claims that are absurd, illogical, or unsupported by evidence, as well as exaggerations, fabrications, or outright lies. Rubbish in this sense is often criticized for being deceptive, misleading, or distracting, and can be harmful when it is used to manipulate or deceive people. One can listen to, spout, say, and read rubbish.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = stopwords.words('english')

    def1Words = word_tokenize(definition1)
    def2Words = word_tokenize(definition2)

    def1Filtered = [ ]
    def2Filtered = [ ]

    for word in def1Words: 
        if word not in stopWords: #filters out stop words
            theWord = lemmatizer.lemmatize(word)
            def1Filtered.append(theWord)
            

    for word in def2Words: 
        if word not in stopWords: #filters out stop words
            theWord = lemmatizer.lemmatize(word)
            def2Filtered.append(theWord)

    def1Counts = [ ]
    def2Counts = [ ]

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filteredWords = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                theWord = lemmatizer.lemmatize(word)
                filteredWords.append(theWord)

        newDef1Filtered = [ ]
        newDef2Filtered = [ ]
        newFilteredWords = [ ]

        for word in def1Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef1Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef1Filtered.append(theWord)

        for word in def2Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef2Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef2Filtered.append(theWord)

        for word in filteredWords:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newFilteredWords.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newFilteredWords.append(theWord)

        simCount1 = 0
        simCount2 = 0
        for word in newFilteredWords:
            for otherWord in newDef1Filtered:
                if word == otherWord:
                    simCount1 += 1

            for otherWord in newDef2Filtered:
                if word == otherWord:
                    simCount2 += 1


        if (simCount1) > (simCount2):
            answer.append(1)
        else:
            answer.append(2)
        def1Counts.append(simCount1)
        def2Counts.append(simCount2)

    return answer, def1Counts, def2Counts

def WSD_Test_Yarn(list):
    answer = [ ]
    definition1 = '''
    Yarn can refer to the act of giving an account, narrating a story, or telling a tale, typically one that is detailed or elaborate. The term is often used informally to describe a long, rambling tale that is embellished or exaggerated for effect. Yarns may be told for entertainment, to convey information, or simply to pass the time. They can take many forms, from personal anecdotes to fictional narratives. They can describe one's childhood, knowledge of things, or simply be an enticing story.'''
    definition2 = '''
    Yarn can also refer to a fine cord of twisted fibers, such as cotton, silk, wool, or nylon, that is commonly used in sewing, weaving, and knitting. Yarn is available in a wide range of colors, textures, and thicknesses, and can be made from natural or synthetic materials. It is used to create a variety of textile products, including clothing, blankets, and home decor items. The quality and characteristics of yarn can vary depending on the type of fiber used, the twist and ply of the yarn, and other factors. It is often in the form of a ball or skein, loosely coiled and knotted.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = stopwords.words('english')

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

    def1Counts = [ ]
    def2Counts = [ ]

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filteredWords = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filteredWords.append(word)

        newDef1Filtered = [ ]
        newDef2Filtered = [ ]
        newFilteredWords = [ ]

        for word in def1Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef1Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef1Filtered.append(theWord)

        for word in def2Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef2Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef2Filtered.append(theWord)

        for word in filteredWords:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newFilteredWords.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newFilteredWords.append(theWord)

        simCount1 = 0
        simCount2 = 0
        for word in newFilteredWords:
            for otherWord in newDef1Filtered:
                if word == otherWord:
                    simCount1 += 1

            for otherWord in newDef2Filtered:
                if word == otherWord:
                    simCount2 += 1

        if (simCount1) > (simCount2):
            answer.append(1)
        else:
            answer.append(2)

        def1Counts.append(simCount1)
        def2Counts.append(simCount2)

    return answer, def1Counts, def2Counts


def WSD_Test_Tissue(list):
    answer = [ ]
    definition1 = '''
    Tissue refers to a group or layer of cells in an organism that share a similar structure and function. Tissues can be found in a variety of living organisms, including plants and animals, and they work together to perform specific functions such as providing structural support, transporting nutrients, or facilitating communication between cells. Examples of tissues in humans include muscle tissue, nerve tissue, and connective tissue. Tissue can be infected, inflamed, raw, examined under a microscope, and makes up most of the human body (under the skin).
    '''
    definition2 = '''
    Tissue refers to a soft, thin, usually translucent paper that is commonly used for personal hygiene purposes or to wrap delicate objects. Tissue paper is often made from recycled materials and is available in a variety of colors, textures, and patterns. It is commonly used for wrapping gifts, wiping one's nose or face, or as a decorative element in crafting and other creative projects. Tissue paper is valued for its softness, light weight, and ease of use. It can wipe up spills, wipe up tears, and are generally used when people hear bad or sad news.
    '''

    lemmatizer = WordNetLemmatizer()
    stopWords = stopwords.words('english')

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

    def1Counts = [ ]
    def2Counts = [ ]

    for sentence in list: #iterates through every sentence
        words = word_tokenize(sentence)
        filteredWords = [ ]
        for word in words: #filters out stop words
            if word not in stopWords:
                word = lemmatizer.lemmatize(word) #lemmatizes words
                filteredWords.append(word)

        newDef1Filtered = [ ]
        newDef2Filtered = [ ]
        newFilteredWords = [ ]

        for word in def1Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef1Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef1Filtered.append(theWord)

        for word in def2Filtered:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newDef2Filtered.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newDef2Filtered.append(theWord)

        for word in filteredWords:
            for definition in wn.synsets(word):
                    hypernyms = definition.hypernyms()
                    hyponyms = definition.hyponyms()
                    meronyms = definition.part_meronyms() + definition.substance_meronyms() + definition.member_meronyms()
                    synonyms = definition.lemmas()

                    for related_word in hypernyms + hyponyms + meronyms:
                        theWord = lemmatizer.lemmatize(related_word.name().split('.')[0])
                        newFilteredWords.append(theWord)

                    for synonym in synonyms:
                        theWord = lemmatizer.lemmatize(synonym.name()) #lemmatizes words
                        newFilteredWords.append(theWord)

        simCount1 = 0
        simCount2 = 0
        for word in newFilteredWords:
            for otherWord in newDef1Filtered:
                if word == otherWord:
                    simCount1 += 1

            for otherWord in newDef2Filtered:
                if word == otherWord:
                    simCount2 += 1

        if (simCount1) > (simCount2):
            answer.append(1)
        else:
            answer.append(2)

        def1Counts.append(simCount1)
        def2Counts.append(simCount2)

    return answer, def1Counts, def2Counts
