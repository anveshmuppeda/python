
def count_words(text):
    words = text.split()
    sentences = text.replace('?', '.').replace('!', '.').split('.')
    sentences = [s for s in sentences if s.strip() != '']
    return len(words), len(sentences)
def count_word(text, word):
    return text.lower().count(word.lower())
def main():
    text = input("Enter a paragraph of text: ")
    word = input("Enter a word to search for: ")
    word_count, sentence_count = count_words(text)
    occurrence_count = count_word(text, word)
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    print(f"'{word}' occurrences: {occurrence_count}")
if __name__ == "__main__":
    main()

