def word_frequency_counter(sentence):
    words = sentence.lower().split()
    word_frequency = {}

    for word in words:
        word = word.strip('.,!?')
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
             
    return word_frequency

def main():
    user_sentence = input("Enter a sentence: ")
    result = word_frequency_counter(user_sentence)

    print("\nWord Frequency:")
    for word, frequency in result.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
