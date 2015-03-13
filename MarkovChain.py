# original code from agiliq.com, author: Shabda Raaj
# added a choice between 2 and 3 word choices, and optional length

import random

class MarkovChain(object):

    def __init__(self, open_file, decision):
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        if int(decision) == 2:
            self.database_two()
        elif int(decision) == 3:
            self.database_three()

    def file_to_words(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words


    def database_two(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]


    def triples(self):
        if len(self.words) < 3:
            return
        
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])
    

    def generate_text_two(self, size=200):
        seed = random.randint(0, self.word_size-4)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)


    def database_three(self):
        for w1, w2, w3, w4 in self.quadruples():
            key = (w1, w2, w3)
            if key in self.cache:
                self.cache[key].append(w4)
            else:
                self.cache[key] = [w4]

    
    def quadruples(self):
        if len(self.words) < 4:
            return

        for i in range(len(self.words) - 3):
            yield (self.words[i], self.words[i+1], self.words[i+2], 
                    self.words[i+3])

    def generate_text_three(self, size=200):
        seed = random.randint(0, self.word_size-4)
        seed_word, next_word, third_word = self.words[seed], self.words[seed+1], self.words[seed+2]
        w1, w2, w3 = seed_word, next_word, third_word
        gen_words = []
        for i in xrange(size):
            gen_words.append(w1)
            w1, w2, w3 = w2, w3, random.choice(self.cache[(w1, w2, w3)])
        gen_words.append(w2)
        return ' '.join(gen_words)
