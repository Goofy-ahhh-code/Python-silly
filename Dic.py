import nltk
from nltk.corpus import words

# Download the words dataset (only needed the first time)
nltk.download("words")

class WordLibrary:
    def __init__(self):
        """Initialize the library with all English words."""
        self.dictionary = set(words.words())  # Store words in a set for fast lookup

    def can_form_word(self, word, available_letters):
        """Check if a word can be formed using the given letters (allowing reuse)."""
        for letter in word:
            if letter not in available_letters:
                return False
        return True

    def find_longest_word(self, letters):
        """Find the longest word that can be formed using the given letters."""
        letters = set(letters.lower())  # Convert input to lowercase set
        valid_words = [word for word in self.dictionary if self.can_form_word(word, letters)]
        return max(valid_words, key=len, default="No valid words found.")

# Example Usage
library = WordLibrary()

while True:
    user_input = input("Enter letters (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        break

    longest_word = library.find_longest_word(user_input)
    print(f"Longest word you can make: {longest_word}\n")
