import string

# list of unimportant words
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


# filter the skip_words
def filter_words(words, skip_words):
    for x in skip_words:
        if x in words:
            words.remove(x)
    return words



# removes punctuation
def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


# normalise inputv(filter the input, removes punctuation, removes spaces)
def normalise_inputs(user_input):
    no_punct = remove_punct(user_input).lower()
    rmv_space = ' '.join(no_punct.split())
    cnvrt_list= rmv_space.split()
    return filter_words(cnvrt_list,skip_words)
