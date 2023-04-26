from cs5322s23 import *

ready = False
rubbish_sentences = [ ]
rubbish_sentences_tags = [ ]
definition = 0
with open('custom_rubbish2.txt', encoding='utf8') as file:
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

WSD_Solution, def1Counts, def2Counts = WSD_Test_Rubbish(rubbish_sentences)

correct = 0
for i in range(len(WSD_Solution)):
    if WSD_Solution[i] == rubbish_sentences_tags[i]:
        correct += 1
    else:
        print(rubbish_sentences[i])
        print('def1Count:', def1Counts[i], 'def2Count:', def2Counts[i])
        print('Guess:', WSD_Solution[i], 'Should be:', rubbish_sentences_tags[i])

print('Accuracy:', correct / len(WSD_Solution))
print(len(rubbish_sentences), len(rubbish_sentences_tags), len(WSD_Solution))
print('-------------------------------------------------------------------------')



ready = False
tissue_sentences = [ ]
tissue_sentences_tags = [ ]
definition = 0
with open('custom_tissue2.txt', encoding='utf8') as file:
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

WSD_Solution2, def1Counts, def2Counts = WSD_Test_Tissue(tissue_sentences)

correct2 = 0
for i in range(len(WSD_Solution2)):
    if WSD_Solution2[i] == tissue_sentences_tags[i]:
        correct2 += 1
    else:
        print(tissue_sentences[i])
        print('def1Count:', def1Counts[i], 'def2Count:', def2Counts[i])
        print('Guess:', WSD_Solution2[i], 'Should be:', tissue_sentences_tags[i])

print('Accuracy:', correct2 / len(WSD_Solution2))
print(len(tissue_sentences), len(tissue_sentences_tags), len(WSD_Solution2))
print('-------------------------------------------------------------------------')



ready = False
yarn_sentences = [ ]
yarn_sentences_tags = [ ]
definition = 0
with open('custom_yarn2.txt', encoding='utf8') as file:
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

WSD_Solution3, def1Counts, def2Counts = WSD_Test_Yarn(yarn_sentences)

correct = 0
for i in range(len(WSD_Solution3)):
    if WSD_Solution3[i] == yarn_sentences_tags[i]:
        correct += 1
    else:
        print(yarn_sentences[i])
        print('def1Count:', def1Counts[i], 'def2Count:', def2Counts[i])
        print('Guess:', WSD_Solution3[i], 'Should be:', yarn_sentences_tags[i])

print('Accuracy:', correct / len(WSD_Solution3))
print(len(yarn_sentences), len(yarn_sentences_tags), len(WSD_Solution3))