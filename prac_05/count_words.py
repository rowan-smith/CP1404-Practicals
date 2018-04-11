def main():

    word_counts = {}

    # sentence = "this is a collection of words of nice words this is a fun thing it is".split(sep=" ")
    sentence = input("Text: ").split(sep=" ")
    for word in sentence:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word in sorted(word_counts.keys()):
        print("{:{}} = {}".format(word, len(max(word_counts, key=len)), word_counts[word]))

main()
