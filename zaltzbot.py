import nltk


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()


with open('trammels.txt') as f:
    text = f.read().split()
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

