from cs5322s23 import *

ready = False
rubbish_sentences = [ ]
rubbish_sentences_tags = [ ]
definition = 0
with open('rubbish.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue
        if line != '1' and not ready:
            continue
        elif not ready:
            ready = True
            definition = 1
        
        if line == '2':
            definition = 2
        
        if line != '1' and line != '2':
            rubbish_sentences.append(line)
            rubbish_sentences_tags.append(definition)

WSD_Solution = WSD_Test_Rubbish(rubbish_sentences)

correct = 0
for i in range(len(WSD_Solution)):
    if WSD_Solution[i] == rubbish_sentences_tags[i]:
        correct += 1

print('Accuracy:', correct / len(WSD_Solution))
print(len(rubbish_sentences), len(rubbish_sentences_tags), len(WSD_Solution))

#for i in range(len(rubbish_sentences)):
#    print(rubbish_sentences[i], rubbish_sentences_tags[i])
#    print()

ready = False
tissue_sentences = [ ]
tissue_sentences_tags = [ ]
definition = 0
with open('tissue.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue
        if line != '1' and not ready:
            continue
        elif not ready:
            ready = True
            definition = 1
        
        if line == '2':
            definition = 2
        
        if line != '1' and line != '2':
            tissue_sentences.append(line)
            tissue_sentences_tags.append(definition)

WSD_Solution2 = WSD_Test_Tissue(tissue_sentences)

correct2 = 0
for i in range(len(WSD_Solution2)):
    if WSD_Solution2[i] == tissue_sentences_tags[i]:
        correct2 += 1

print('Accuracy:', correct2 / len(WSD_Solution2))
print(len(tissue_sentences), len(tissue_sentences_tags), len(WSD_Solution2))

#----------------------------------------------------------

ready = False
yarn_sentences = [ ]
yarn_sentences_tags = [ ]
definition = 0
with open('yarn.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue
        if line != '1' and not ready:
            continue
        elif not ready:
            ready = True
            definition = 1
        
        if line == '2':
            definition = 2
        
        if line != '1' and line != '2':
            yarn_sentences.append(line)
            yarn_sentences_tags.append(definition)

WSD_Solution3 = WSD_Test_Yarn(yarn_sentences)

correct = 0
for i in range(len(WSD_Solution3)):
    if WSD_Solution3[i] == yarn_sentences_tags[i]:
        correct += 1

print('Accuracy:', correct / len(WSD_Solution3))
print(len(yarn_sentences), len(yarn_sentences_tags), len(WSD_Solution3))


'''
from pprint import pprint
pprint(WSD_Solution)
print('----------------------')
pprint(WSD_Solution2)
print('----------------------')
pprint(WSD_Solution3)

from nltk.corpus import wordnet as wn

#word1 = wn.synset('rubbish.n.01')
#word2 = wn.synset('trash.n.01')

for syn in wn.synsets('rubbish'):
    for i in syn.lemmas():
        print(i.name())

#print(word1)
#print(word2)
#print(word1.wup_similarity(word2))
'''