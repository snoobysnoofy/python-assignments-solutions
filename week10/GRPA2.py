class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        n = 0
        for word in self.words:
            if word == some_word:
                n += 1
        return n

    def words_of_length(self, length):
        l = [ ]
        for word in self.words:
            if len(word) == length:
                l.append(word)
        return l

    def words_start_with(self, char):
        l = [ ]
        for word in self.words:
            if word[0] == char:
                l.append(word)
        return l

    def longest_word(self):
        longest = ""
        for word in self.words:
            if len(word) > len(longest):
                longest = word
        return longest

    def palindromes(self):
        l = [ ]
        for word in self.words:
            reverse = ""
            for char in word:
                reverse = char + reverse
            if word == reverse:
                l.append(word)
        return l