from cs5322s23 import *

rubbish_sentences = [ ]
with open('test_rubbish.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue

        rubbish_sentences.append(line)

WSD_Test_Rubbish(rubbish_sentences)

yarn_sentences = [ ]
with open('test_yarn.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue
        
        yarn_sentences.append(line)

WSD_Test_Yarn(yarn_sentences)

tissue_sentences = [ ]
with open('test_tissue.txt', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        if not line: # Skips blank lines
            continue

        tissue_sentences.append(line)

WSD_Test_Tissue(tissue_sentences)