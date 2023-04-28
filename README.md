# WordSenseDisambiguation
Program 2 for CS 5322 Introduction to Natural Language Processing

[Assignment Details](https://github.com/Mikecamdo/WordSenseDisambiguation/blob/main/5322s23prog2.pdf)

## General Approach:
For this Word Sense Disambiguation problem, I decided to use a dictionary- and knowledge-based method. My method was inspired by the Lesk algorithm, which uses the idea that words in a given section of text will have a similar meaning. For each sense of a word, I created a lengthy explanation using key words that are often associated with that sense of the word. The explanations were as follows:

### Rubbish Sense 1:
-	Rubbish, also known as trash, scrap, or litter, refers to materials that have little or no value and are typically discarded. These may include things such as food waste, broken items, packaging materials, or other unwanted materials that are no longer useful. Rubbish can accumulate quickly in households, public places, and businesses, and must be disposed of properly to maintain a clean and healthy environment. It can be thrown away.

### Rubbish Sense 2:
-	Rubbish can also refer to nonsensical talk or writing, sometimes described as folderol, tripe, trumpery, wish-wash, or other similar terms. This kind of rubbish may include statements or claims that are absurd, illogical, or unsupported by evidence, as well as exaggerations, fabrications, or outright lies. Rubbish in this sense is often criticized for being deceptive, misleading, or distracting, and can be harmful when it is used to manipulate or deceive people. One can listen to, spout, say, and read rubbish.

### Yarn Sense 1:
-	Yarn can refer to the act of giving an account, narrating a story, or telling a tale, typically one that is detailed or elaborate. The term is often used informally to describe a long, rambling tale that is embellished or exaggerated for effect. Yarns may be told for entertainment, to convey information, or simply to pass the time. They can take many forms, from personal anecdotes to fictional narratives. They can describe one's childhood, knowledge of things, or simply be an enticing story. You can listen to, hear, and write a book or poem about a yarn. Yarns can be encounters or adventures.

### Yarn Sense 2:
-	Yarn can also refer to a fine cord of twisted fibers, such as cotton, silk, wool, or nylon, that is commonly used in sewing, weaving, and knitting. Yarn is available in a wide range of colors, textures, and thicknesses, and can be made from natural or synthetic materials. It is used to create a variety of textile products, including clothing, blankets, and home decor items. The quality and characteristics of yarn can vary depending on the type of fiber used, the twist and ply of the yarn, and other factors. It is often in the form of a ball or skein, loosely coiled and knotted or in strands. You can wrap yarn around something.

### Tissue Sense 1:
-	Tissue refers to a group or layer of cells in an organism that share a similar structure and function. Tissues can be found in a variety of living organisms, including plants and animals, and they work together to perform specific functions such as providing structural support, transporting nutrients, or facilitating communication between cells. Examples of tissues in humans include muscle tissue, nerve tissue, and connective tissue. Tissue can be infected, inflamed, raw, scarred, examined under a microscope, and makes up most of the human body (under the skin).

### Tissue Sense 2:
- Tissue refers to a soft, thin, usually translucent paper that is commonly used for personal hygiene purposes or to wrap delicate objects. Tissue paper is often made  from recycled materials and is available in a variety of colors, textures, and patterns. It is commonly used for wrapping gifts, wiping one's nose or face, or as a   decorative element in crafting and other creative projects. Tissue paper is valued for its softness, light weight, and ease of use. It can wipe up spills, wipe up  tears, and are generally used when people hear bad or sad news. Tissue comes in dispensers or boxes.

My general strategy was to compare a given sentence to each explanation of the word, and whichever explanation the sentence was more similar to was the sense of the word I selected.

## Preprocessing Steps:
To preprocess the data, I did the following:
1.	Tokenize each sentence (split each sentence into individual words)
2.	Filter out stop words (words that don’t convey meaning, such as “and”, “or”, “but”, etc.)
3.	Lemmatize each word

This preprocessing was applied to both explanations for each word, as well as for each given sentence with the word that was to be disambiguated.

## Algorithm:
To find the similarity between each sentence and the explanations I provided, I considered the following factors:

-	Hypernyms: A hypernym is a word with a broad meaning that more specific words fall under. For example, “food” is a hypernym of “apple”.
-	Hyponyms: A hyponym is a word with a more specific meaning than a broad term applicable to it. For example, “apple” is a hyponym of “food”.
-	Meronyms: A meronym is a word that specifies a part of something but that refers to the whole of the thing. For example, “limb”, “trunk”, and “stump” are all meronyms of “tree”.
-	Synonyms: A synonym is a word that means essentially the same thing as another word. For example, “trash” is a synonym of “rubbish”.

After preprocessing both explanations and each given sentence, I used an algorithm to find all hypernyms, hyponyms, meronyms, and synonyms for each word and added them to a list. The algorithm was as follows:
1.	For each word in the given sentence/explanation, get all definitions of that word from WordNet.
2.	For each definition, get all hypernyms, hyponyms, meronyms, and synonyms (as defined in WordNet).
3.	For each word in the set of hypernyms, hyponyms, meronyms, and synonyms, lemmatize it and add it to the list.

The result is a list of all possible hypernyms, hyponyms, meronyms, and synonyms for each word in the explanation/sentence.

## Disambiguation Process:
Finally, to disambiguate the sense of the word, I compared the generated lists for each explanation to the generated list for the given sentence. For each word that was in the sentence’s list and in the first explanation’s list, I added 1 to simCount1 (similarity count 1); likewise, for each word that was in the sentence’s list and in the second explanation’s list, I added 1 to simCount2 (similarity count 2). Finally, I compared simCount1 to simCount2: if simCount1 was greater, I assigned a sense of 1 to the sentence; if simCount2 was greater, I assigned a sense of 2 to the sentence.

## Fine-Tuning Process:
To fine-tune the program, I provided a generic explanation of each sense of the word to the program and tested it on a training data set (where the sense of each word was known). I observed the sentences in which it wrongly disambiguated the word, manually found keywords related to that specific sense of the word and updated the explanations. For example, I added “It can wipe up spills, wipe up tears, and are generally used when people hear bad or sad news” to the explanation of the second sense of the word “tissue”, as the keywords “wipe”, “spills”, “tears”, and “bad/sad news” are more associated with the second sense of the word “tissue”.

## Results
A test data set was provided by my professor for each of the three words; each data set (one for each word) had 50 sentences in it that were to be disambiguated. The results were as follows:
- Rubbish: 30/50 correct
- Yarn: 36/50 correct
- Tissue: 37/50 correct

This resulted in an overall accuracy of **68.67%**. While there were several machine learning programs that outperformed this, I believe this result is very impressive for how simple and quick the program is.
