
from utils import sort_letters_in_word


# This class stores all the words in the dictionary words_hash with sorted string of the word as key
# If two words have same hash the it is appended to the list of words in the hash key
# All the words are initialized and added to the words_hash
class Words:

    def __init__(self, words_list):
        self.words_hash = {}
        self.words_list = words_list
        for word in words_list:
            self.append_word_to_hash_set(word)

    def append_word_to_hash_set(self, word):
        """
        Adds the word to dictionary words_hash with sorted letters of the word as a key
        :param word:
        :return:
        """
        sorted_letters_in_word = sort_letters_in_word(word)
        if sorted_letters_in_word in self.words_hash.keys():
            if not word in self.words_hash[sorted_letters_in_word]:
                self.words_hash[sorted_letters_in_word].append(word)
        else:
            self.words_hash[sorted_letters_in_word] = [word]

    def find_word(self, search_string):
        search_string_key = sort_letters_in_word(search_string)
        return self.words_hash.get(search_string_key, [])
