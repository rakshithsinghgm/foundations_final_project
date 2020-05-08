from random import shuffle, randint

def scramble(sentence):
    try:
        split = sentence.split()  # Split the string into a list of words
        split_len = len(split) - 1
        #shuffle(split)  # This shuffles the list in-place.
        #return ' '.join(split)
        result_sentence = []
        extra_or_drop = randint(0,1)
        extra_or_drop = 0
        if extra_or_drop == 0:
            for word in split:
                if word == "a":
                    result_sentence.append("a")
                    result_sentence.append("a")
                    result_sentence.append("a")
                elif word == "the":
                    result_sentence.append("the")
                    result_sentence.append("the")
                elif word == "an":
                    result_sentence.append("an")
                    result_sentence.append("an")
                elif word == "these":
                    result_sentence.append("these")
                    result_sentence.append("these")
                    result_sentence.append("these")
                else:
                    result_sentence.append(word)
        else:
            word_to_be_removed = randint(0,split_len)
            del split[word_to_be_removed]
            for word in split:
                result_sentence.append(word)
        return ' '.join(result_sentence)
    except ValueError:
        return None

# Read Brown Corpus Line by Line
with open('brown.txt', 'r') as f:
    lines = f.readlines()
#print(len(lines))

# Scramble word order in brown corpus
scrambled_brown_corpus = []
for sentence in lines:
    res = scramble(sentence)
    if res is not None:
        scrambled_brown_corpus.append(res)

### Write to the oo
for line in scrambled_brown_corpus:
    with open("brown_en_2.txt", "a") as output:
        output.write(line+"\n")

