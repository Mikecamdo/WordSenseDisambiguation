from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

def WSD_Test_Rubbish(list): # List is a list of strings, with each string being a sentence containing the word "rubbish"
    answer = [ ]
    definition1 = '''
    worthless material that is to be disposed of
    There was a thick film of dust on every exposed surface; rubbish and the carcass of some small animal had liecn swept carelessly into a corner.
    "There's nothing under here except a large amount of mineral salts and other rubbish that's no use to us.
    I dropped the satin rubbish on the floor, because it could only hamper me.
    Like a man possessed he hurried around the room, tumbling rubbish and papers into piles and igniting them with his pocket lighter.
    Rubbish and offal filled the corners.
    A rock crashed off the rearview window and for an instant a hail of rubbish banged and clattered.
    I've got a small flashlight and we grope through a pile of rubbish, out into a corridor.
    He was hungry now as he walked through the alley, his eyes shifting lusterlessly from one heap of rubbish to the next.
    Cold morning wind whipped around the rubbish that littered the deserted inter-system field at the rim of the syndrome.
    They adjourned with an order strictly forbidding suburbanite burning of rubbish.
    But your clothes have been cleaned off the field along with all the rubbish of our shriek; the officials are already preparing for the next one."
    Overgrown with trees and smothering in its own dust, it was hardly more than a centuries-old rubbish heap now.
    And the winds swept away from the picture the rubbish, the shovel and many of the objects.
    The garbage collector passed slowly along it every hour, collecting all the rubbish that chanced to be there.
    I put everything down and poked assiduously in the rubbish in back with the broomstick handle and even lit a fire with some of the litter I found outside, thrusting burning stuff into the back of the cave in several places.
    I scrambled up the slope outside, trying not to touch anything in the rubbish.
    The intense, yellow-white light stared pitilessly down on a gently swelling floor of seawater, out of which rose, to the right of where the plane sat in the shallows, a derelict pile of rubbish reaching roughly a third of the way to the roof.
    The most important precaution is to remove and reduce trash and rubbish from your property,
    Don't bury rubbish like cans, plastic bottles or broken glass. It is often dug out by native animals and may harm them.
    The mice had their own society, using rubbish thrown away by humans.
    Because of this, in 1532 a Stannary Court decree ordained that all rubbish should be deposited in old Hatches, Tipittes, miry Places, or other convenient Places away from the main streams. 
    Today the old nir looks half-abandoned and out of place in its current setting, with broken down cars parked haphazardly and rubbish lying around. 
    The fine or punishment is normally defined by the local council that operates in the local area that the rubbish was dumped in. 
    Around four fifths of oceanic debris is from rubbish blown onto the water from landfills, and urban runoff. 
    Moreover, with recent increases in tourism on the island, new sources of hard rubbish have begun to appear.
    '''

    definition2 = '''
    nonsensical talk or writing
    Wendy wouldn't be sucked in by a load of specious rubbish spouted by a cracked demagogue hungry for martyrdom.
    "Oh, let's Stop talking rubbish," she cried.
    There Is an awful lot of rubbish published.
    "You talk rubbish, old man," the young man said, but he sounded uneasy.
    "You believed all that rubbish you told Tylo about what the Federation really wants, didn't you?"
    The words, the history books, the ideas, the science -- Underhill could sense all that in his own mind, reflected back from Captain Wow's mind, as so much rubbish.
    What kind of rubbish have you been reading?"
    I'm talking sense and rubbish at the same time.
    Good riddance to childish rubbish.
    Now there's been so much rubbish written about how Ben's vaccine is either the world's worst disaster or else its greatest hope that I thought I'd wind this up by telling what really happened down here.
    "Your confession is the biggest pile of rubbish I've read in my life.
    All he did was mutter, 'That golden shape on the golden steps, that music, that me is a true me, that golden shape, that golden shape, I want to be with that golden shape,' and rubbish like that.
    "She's talking rubbish," I said, but already a few voices in the crowd shouted that she was merely spreading rumor.
    To Colonel Smith's question about the possibility of an "overkill" if such and such size bomb dropped on such and such enemy city the answer came back, "Rubbish.
    Our sense of humour and perception of what's good and what's rubbish are uncommonly in tune. 
    She criticised stories in the magazine as absolute rubbish and ridiculously alarmist.
    Using his Twitter account, he derided the language as being an old, unadaptive language with relatively few words for things and Gaelic poetry as basically doggerel and and mainly a bit of rubbish. 
    She described the psychoanalyzing of dogs as a lot of rubbish.
    After the performance he declared'' Such rubbish should never have been written''
    But this new book is wretched; a high-varnished preface to a heap of rubbish, in a very vulgar style, and too void of method even for such a farrago. 
    I am not going to write any more of that bloody rubbish with those idiots.
    However, its production at the Metropolitan Opera in New York City in 1890 inspired dismal reviews, with one spectator commenting that its music was simply rubbish. 
    Judge Hlophe was reported to have rejected the allegations as utter rubbish and as another ploy to damage his reputation.
    In October 2007, Bald expressed a desire to leave Celtic stating I don't want to be at a club where I am not wanted, but I want to make clear it is rubbish to say I am just taking the money.
    Intelligent design should be viewed as a ground-clearing operation that gets rid of the intellectual rubbish that for generations has kept Christianity from receiving serious consideration.
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
        if (def1Similarity / len(def1Words)) > (def2Similarity / len(def2Words)):
            print(1)
            answer.append(1)
        else:
            print(2)
            answer.append(2)

    return answer

def WSD_Test_Yarn(list):
    answer = [ ]
    definition1 = '''
    the act of giving an account describing incidents or a course of events
    The yarn is no longer novel -- too many other writers have since taken off from Gallun's inspiration -- but it is just as fine to me as it always was.
    I have just finished reading a rather lengthy yarn with several rather far-fetched theories in one field, two or three political premises stirred up with them, and then a bunch of characters, none clearly definable, trying to juggle the whole mess.
    But spin those reporters some yarn and keep them there if you can.
    They censored all that out of my copy -- made it strictly a yarn about the nullies.
    "Nan, do you think that kind of yarn is going to stop me from writing about what happened tonight?
    Just swallow the premise and enjoy the yarn.
    It is almost a truism that Clement's books never smile, but he pens a credible, workmanlike and always interesting yarn.
    That one man can kill the world with a button is the story skeleton of a well-muscled yarn.
    He spun his yarn from the material in his head.
    I have seen the transition of SF from the original crude gimmick yarn to today's polished story of ideas.
    I hate to say it in public, but this is the first Doc Smith yarn I've had a chance to read.
    His illustration was the yarn of a sea captain who after a storm found himself alone in the ocean with a bit of driftwood.
    Some of us come in from the farm, others from the city; some are connoisseurs, some just like a good yarn.
    These books thrive on yarn spinning, but they also take immense delight in the inner workings of things
    If you can hold off a while longer, I may be able to give you a better yarn."
    He can come back down afterward again if he likes, but I'll be much more convinced of his yarn if I see him breathing air again, and I'll feel a lot safer if he's in this boat with me when I drive it out of here.
    We know from historical accounts and from the occasional yarn from an old-timer that within living memory children could be trusted with matches and clasp knives and were known to look after each other without constant adult intervention or correction.
    In this cavalry yarn, great pains have been exerted to provide interesting characters.
    After publication, the book received praise from President Ronald Reagan, who called the work "the best yarn", subsequently boosting sales to 300,000 hardcover and two million paperback copies of the book, making it a national bestseller.
    The book was published in May 2005 and is billed as "A road trip, a rich historical yarn, and testimony to the odd nature of a great many friendships".
    The Telegraph's story was picked up by various newspapers in Australia but not by the Melbourne Herald Sun because of concerns that the Telegraph was "running with a yarn which is highly libellous".
    Fortinbras operates on a far less ambitious plane, but it is a ripping yarn and offers Keith Reddin a role in which he can commit comic mayhem".
    What makes this one of the good ones is superlative photography of the storied Grecian isles, a crackerjack cast and a yarn about WWII in which unlikely incident succeeds unlikely incident with rare largesse.
    Local heartthrob Won Bin transforms himself into an action hero in writer-helmer Lee Jeong-beom’s swift and blood-soaked yarn, about a mystery man who gets caught up in a gang war while trying to protect a child,
    The New York Times observed that it was "a natural, tender and amusing yarn" with "laughs that leave the spirits soaring."
    '''
    definition2 = '''
    a fine cord of twisted fibers (of cotton or silk or wool or nylon etc.) used in sewing and weaving
    "Then, if you like, I'll teach you a knitting stitch and you can pick any color yarn you like."
    If you were in the yarn business, especially in New England, you had to work hard -- most of the mills had moved south long ago.
    He had a hank of red yarn in his hand and I could see the yarn and the clothes he was wearing distinctly, but all of a sudden his face blurred and his features ran together -- like a fadeout in the movies, if you know what I mean.
    Yet they were separate, as one strand of colored thread in a ball of yarn is looped and knotted and intertwined with every other strand, although it retains its own integrity.
    Go and pick out any color of yarn you like and I'll show you how to knit.
    It has a rubber or cork center, wound in yarn and covered in white cowhide, 
    I checked out videos and some of them show wrapping the yarn on the needle before doing the knit/purl stitch. 
    I knitted mittens with that same yarn and have the shedding problem also.
    Below you can see that the tails of yarn are visible on the back of the work 
    String each- paper sign onto the yarn, threading through each hole. 
    Several thousand carbon fibers are twisted together to form a yarn, which may be used by itself or woven into a fabric. 
    Moreover, the size of the buttonhole is totally dependent on the weight of the yarn and the needle size. 
    It was slow-going but it also felt therapeutic to methodically wrap the yarn around the cardboard.
    When dry, tape piece of yarn on the back for a hanger,
    China’s phenomenal growth in cotton garments is partly because we continue to be its largest supplier of cotton fibre and yarn.
    These machines are designed to provide higher operating speeds, larger yarn packages, and greater flexibility of application to different types of yarn.
    The industry, which produces yarn, fabric and garments for high-end brands, mostly employs young village women from poor, illiterate and low-caste communities.
    Thread is a type of yarn but similarly used for sewing. 
    A swift is a tool used to hold a hank of yarn while it is being wound off 
    White also participates in real estate investment, owns the yarn brand Vanna's Choice, and patronizes St. Jude Children's Research Hospital.
    Warp knitting is defined as a loop-forming process in which the yarn is fed into the knitting zone, parallel to the fabric selvage.
    Weaving is a method of textile production in which two distinct sets of yarns or threads are interlaced at right angles to form a fabric or cloth. 
    Sometimes medium to hard rubber mallets, very hard core, or yarn mallets are used for softer effects.
    Rovings are produced during the process of making spun yarn from wool fleece, raw cotton, or other fibres.
    The port was opened in 1762, mainly for the export of coir-matting and coir-yarn. Kesavadas built three ships for trade with Calcutta and Bombay, and alleppey afforded a convenient depot for the storage and disposal of goods produce in the east.
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

        if (def1Similarity / len(def1Words)) > (def2Similarity / len(def2Words)):
            answer.append(1)
        else:
            answer.append(2)

    return answer


def WSD_Test_Tissue(list):
    answer = [ ]
    definition1 = '''
    part of an organism consisting of an aggregate of cells having a similar structure and function
    As the weeks passed, he put on weight, removed the fatty tissue from his cheekbones, thickened his cheeks enough to remove the gauntness, and restored his complexion to a healthier hue.
    Then the terrifying drrrnngg of the pain-making aura that seared every nerve ending without numbing or damaging tissue.
    Tooth enamel was long thought to be dead tissue, for instance.
    And then the news was broken to everyone about the culturing of the scar tissue, and there were a few dissenters but they were soon conditioned out of their dissension and the population was stabilized.
    See that your damaged tissues are repaired as fully as possible.
    But she had flicked scar tissue and I answered almost sharply, "I am not employee of Warden."
    Sidis grin was sagging, hooked up on the bad side by twisted scar tissue.
    It puffed around his face, stinging the skin tissues there, a pink mist that went into his lungs.
    Alfieri's heart pumped Alfieri's blood through the new tissue.
    You pump air into the wing, and the tissue -- skin, cells, stiffeners and all -- absorbs it and stores it as semistable compounds.
    But the optic nerve is brain tissue, not ordinary nerve tissue.
    I wouldn't be surprised if you could rupture lung tissues that way.
    They don't expend themselves futilely trying to get rid of what they consider invading tissue.
    Organs and tissues for later transplants can be more readily preserved.
    After that, the tissues of the lungs are exposed to emptiness and begin to release their liquids through surface boiling, with fatal and agonizing results.
    I strained with every bit of muscle tissue to no useful end.
    I could almost feel cartilage tear and muscle tissues pop.
    His vision was blurring, shot through with red; his lungs ached, his tissues screamed their torture.
    "Do you choose to experience the destruction of your body's tissues?"
    Ms. Armul says there is also some evidence that a ketogenic diet breaks down muscle tissue for energy.
    But despite the advances of medicine through the centuries there still wasn't any way for our techs to get blood or several other kinds of tissue samples out of a humanoid body without poking it with a syringe or punch.
    In experiments they have used a plug of tissues consisting mainly of blood vessels.
    We cannot establish the significance of the multiple substances  that were detected in Ms. Fisher's blood and tissue with regard to the cause of death.
    Meningitis is the inflammation of tissue surrounding the brain and spinal cord, which can be caused by viral or bacterial infections.
    “For most dinosaurs that I looked at, there would have been a substantial amount of physiologically active soft tissues in their noses,” said Bourke.
    '''
    definition2 = '''
    a soft thin (usually translucent) paper
    He dabbed at his forehead with a large floral-patterned tissue.
    Durlston took a tissue and flicked the seat, then he sat down with his jacket on, looking cool and calm and impeccable.
    Both had been torn loose from their mountings and wadded into the nose like so much tissue paper, crushing the instrument panel.
    Magnan trailed, mopping at his face with a scented tissue.
    Turning her back on Adam, she lifted the lid of the top box, pulled aside the tissue paper and carefully drew out a garland of stephanotis.
    Chuck turned his large frame and caromed a box of tissues off Steve's left shoulder.
    He took a clean issue tissue tunic from the wall dispenser.
    Inside each was a multitude of tiny compartments, each with a bit of something wrapped in cloth or paper tissue.
    I did not want to shoot Mr. Castile at all,  Yanez said as he took off his glasses and wiped away tears with a tissue.
    He'd run out of tissues, and his nose was a continual drip, while breathing seemed almost impossible.
    He wiped his nose and reached for a fresh tissue.
    He wiped his brow with a paper tissue.
    Finished, he climbed over the rail and joined Wenzl, mopping his brow with a tissue.
    He sneezed as the dry air caught the tissue pf his nostrils.
    She quickly stuffed the tissue in the disposal and sat up, touching her blond hair lightly with her hands.
    She didn't want a tissue or a cup of water from the cooler or anything at all.
    Winston followed her around the room, collecting the small frail objects (Christmas, birthday, and anniversary) and wrapping them in tissue paper.
    Winston folded the tissue paper carefully.
    Ben winced as she unwrapped the bloody tissue and wiped the slash with anesthetic, then turned his attention to the pen and paper the Deskman was offering, and almost laughed.
    Tissue paper production and consumption is predicted to continue to grow because of factors like urbanization, increasing disposable incomes and consumer spending.
    Japanese tissue may be made from one of three plants, the kōzo plant (Broussonetia papyrifera, paper mulberry tree), the mitsumata (Edgeworthia chrysantha) shrub and the gampi tree (Diplomorpha sikokiana).
    The tissue paper might be treated with softeners, lotions or added perfume to get the right properties or "feeling".
    Orchids Paper Products Company is a manufacturer of tissue products serving the at-home tissue market. 
    For example, common mistakes include putting tissue boxes in the recycling bin without first removing the plastic insert, 
    The underlying demand for dissolving pulp, packaging, office paper and tissue, in South Africa, and speciality papers abroad, remains strong, driven by global sustainability trends
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

        if (def1Similarity / len(def1Words)) > (def2Similarity / len(def2Words)):
            answer.append(1)
        else:
            answer.append(2)

    return answer
