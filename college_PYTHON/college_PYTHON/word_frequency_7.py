# Word Frequency Counter using Dictionary
def word_frequency(text):
    words=text.lower().split()

    word_count={}

    for word in words:
        word=word.strip(".,!?/';:(){}[]")

        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    return word_count

text="this is a test.The Test is good"
word_freq=word_frequency(text)

print(word_freq)
