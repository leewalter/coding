# use Counter
# ref - https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/


from collections import Counter

data_set = "Welcome to the world of Geeks " \
"This portal has been created to provide well written well" \
"thought and well explained solutions for selected questions " \
"If you like Geeks for Geeks and would like to contribute " \
"here is your chance You can write article and mail your article " \
" to contribute at geeksforgeeks org See your article appearing on " \
"the Geeks for Geeks main page and help thousands of other Geeks. "

split_it = data_set.split()

Counter = Counter(split_it)

most_occur = Counter.most_common(4)

print(most_occur)

'''
[('Geeks', 5), ('to', 4), ('and', 4), ('for', 3)]

or use iterator

a = "John is the son of John second. Second son of John second is William second."

# replace below punctuation marks, 

for i in '-.,\n':
    a = a.replace(i,' ')
b = a.split()
#print(b)

# build the new dictionary for key value pair

c = {}
for k in b:
    c[k] = c.get(k,0)+ 1

#print(c)

# build new list for word freq, so it can be sorted 

word_freq = []
for k,v in c.items():
    word_freq.append((v,k))
print(word_freq)

# sort from top to bottom

word_freq.sort(reverse=True)
print(word_freq)

top_n = 4
for i in range(top_n):
    print(word_freq[i])

'''
