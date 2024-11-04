# Word Finding
 ***Ask the user for a paragraph of text and count the words, sentences, and occurrences of a particular word***
 ```python
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
```
### Example and output
```console
**Enter a paragraph of text:** There was a time and a place for Stephanie to use her magic. The problem was that she had a difficult time determining this. She wished she could simply use it when the desire hit and there wouldn't be any unforeseen consequences. Unfortunately, that's not how it worked and the consequences could be devastating if she accidentally used her magic at the wrong time.
**Enter a word to search for:** and
**Word count:** 64
**Sentence count:** 4
**'and' occurrences:** 3

