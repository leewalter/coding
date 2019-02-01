# ref  https://github.com/leewalter/Python_Tutorials/blob/master/Python_Basics/Intro/PythonBasicsWordCount.ipynb

Text="""
bands which have connected them with another, and to assume among the
powers of the earth, the separate and equal station to which the Laws
of Nature and of Nature's God entitle them, a decent respect to the
opinions of mankind requires that they should declare the causes which
impel them to the separation.  We hold these truths to be
self-evident, that all men are created equal, that they are endowed by
their Creator with certain unalienable Rights, that among these are
Life, Liberty and the pursuit of Happiness.--That to secure these
rights, Governments are instituted among Men, deriving their just
powers from the consent of the governed, --That whenever any Form of
Government becomes destructive of these ends, it is the Right of the
People to alter or to abolish it, and to institute new Government,
laying its foundation on such principles and organizing its powers in
such form, as to them shall seem most likely to effect their Safety
and Happiness. """

print(Text)

# Cleaning text and lower casing all words
for char in '-.,\n':
    Text=Text.replace(char,' ')
Text = Text.lower()

print(Text)

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = Text.split()
print(word_list)

# 1. Using for loops

# Initializing Dictionary
d = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in word_list:
    d[word] = d.get(word, 0) + 1

print(d)

# Reverses the key and values so they can be sorted
# using tuples
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

print(word_freq)

word_freq.sort(reverse=True)
print(word_freq)

'''
[(12, 'the'), (11, 'to'), (9, 'of'), (7, 'and'), (6, 'that'), (4, 'these'), (4, 'them'), (4, 'are'), (3, 'which'), (3, 'their'), (3, 'powers'), (3, 'among'), (2, 'with'), (2, 'they'), (2, 'such'), (2, 'rights'), (2, 'men'), (2, 'its'), (2, 'it'), (2, 'happiness'), (2, 'government'), (2, 'form'), (2, 'equal'), (1, 'whenever'), (1, 'we'), (1, 'unalienable'), (1, 'truths'), (1, 'station'), (1, 'should'), (1, 'shall'), (1, 'separation'), (1, 'separate'), (1, 'self'), (1, 'seem'), (1, 'secure'), (1, 'safety'), (1, 'right'), (1, 'respect'), (1, 'requires'), (1, 'pursuit'), (1, 'principles'), (1, 'people'), (1, 'organizing'), (1, 'or'), (1, 'opinions'), (1, 'on'), (1, 'new'), (1, "nature's"), (1, 'nature'), (1, 'most'), (1, 'mankind'), (1, 'likely'), (1, 'life'), (1, 'liberty'), (1, 'laying'), (1, 'laws'), (1, 'just'), (1, 'is'), (1, 'instituted'), (1, 'institute'), (1, 'in'), (1, 'impel'), (1, 'hold'), (1, 'have'), (1, 'governments'), (1, 'governed'), (1, 'god'), (1, 'from'), (1, 'foundation'), (1, 'evident'), (1, 'entitle'), (1, 'ends'), (1, 'endowed'), (1, 'effect'), (1, 'earth'), (1, 'destructive'), (1, 'deriving'), (1, 'declare'), (1, 'decent'), (1, 'creator'), (1, 'created'), (1, 'consent'), (1, 'connected'), (1, 'certain'), (1, 'causes'), (1, 'by'), (1, 'becomes'), (1, 'be'), (1, 'bands'), (1, 'assume'), (1, 'as'), (1, 'any'), (1, 'another'), (1, 'alter'), (1, 'all'), (1, 'abolish'), (1, 'a')]

Process finished with exit code 0

'''
