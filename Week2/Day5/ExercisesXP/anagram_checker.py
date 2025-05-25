
class AnagramChecker:
    def __init__(self, wordlist_path='words.txt'):
        with open(wordlist_path, 'r') as f:
            self.words = [line.strip().lower() for line in f if line.strip().isalpha()]

    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        return [w for w in self.words if self.is_anagram(word, w)]
