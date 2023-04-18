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



#rubbish_sentences = [ 
#    'There was a thick film of dust on every exposed surface; rubbish and the carcass of some small animal had liecn swept carelessly into a corner.',
#    "There's nothing under here except a large amount of mineral salts and other rubbish that's no use to us.",
#    'I dropped the satin rubbish on the floor, because it could only hamper me.',
#    'Like a man possessed he hurried around the room, tumbling rubbish and papers into piles and igniting them with his pocket lighter.',
#    'Rubbish and offal filled the corners.',
#    "Wendy wouldn't be sucked in by a load of specious rubbish spouted by a cracked demagogue hungry for martyrdom.",
#    "\"Oh, let's Stop talking rubbish,\" she cried.",
#    'Intelligent design should be viewed as a ground-clearing operation that gets rid of the intellectual rubbish that for generations has kept Christianity from receiving serious consideration.',
#    'Nonsensical talk or rubbish'
# ]

'''

WSD_Test_Rubbish(rubbish_sentences)

print('-----------------------------------------------------------------')

testing2 = [
    'As the weeks passed, he put on weight, removed the fatty tissue from his cheekbones, thickened his cheeks enough to remove the gauntness, and restored his complexion to a healthier hue.',
    'But she had flicked scar tissue and I answered almost sharply, "I am not employee of Warden."',
    'I strained with every bit of muscle tissue to no useful end.',
    'He wiped his nose and reached for a fresh tissue.',
    'Japanese tissue may be made from one of three plants, the kōzo plant (Broussonetia papyrifera, paper mulberry tree), the mitsumata (Edgeworthia chrysantha) shrub and the gampi tree (Diplomorpha sikokiana).',
    'He took a clean issue tissue tunic from the wall dispenser.'
]

WSD_Test_Tissue(testing2)

print('-----------------------------------------------------------------')

testing3 = [
    "The yarn is no longer novel -- too many other writers have since taken off from Gallun's inspiration -- but it is just as fine to me as it always was.",
    'I have just finished reading a rather lengthy yarn with several rather far-fetched theories in one field, two or three political premises stirred up with them, and then a bunch of characters, none clearly definable, trying to juggle the whole mess.',
    'Several thousand carbon fibers are twisted together to form a yarn, which may be used by itself or woven into a fabric.',
    'Warp knitting is defined as a loop-forming process in which the yarn is fed into the knitting zone, parallel to the fabric selvage.'
]

WSD_Test_Yarn(testing3)

'''