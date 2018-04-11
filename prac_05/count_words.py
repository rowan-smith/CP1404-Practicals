def main():

    word_counts = {}

    sentence = input("Text: ").split(sep=" ")
    for word in sentence:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word in sorted(word_counts.keys()):
        print("{} : {}".format(word, word_counts[word]))

main()
