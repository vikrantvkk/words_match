# This is driver code.

from words import Words

if __name__ == '__main__':
    my_words = Words(["helloworld", "foo", "bar", "stylight_team", "seo"])
    print(my_words.find_word("eos"))

