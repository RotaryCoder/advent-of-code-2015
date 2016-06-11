# -*- coding: utf-8 -*-

"""
RULES:
Passwords must include one increasing straight of at least three letters, 
   like abc, bcd, cde, and so on, up to xyz. 
   They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be 
   mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of 
   letters, like aa, bb, or zz.
"""
import re

#    # iterator protocol
#    class uc_iter():
#        def __init__(self, text):
#            self.text = text
#            self.index = 0
#        def __iter__(self):
#            return self
#        def __next__(self):
#            try:
#                result = self.text[self.index].upper()
#            except IndexError:
#               raise StopIteration
#            self.index += 1
#            return result

class Password(object):  
    def __init__(self, seed='abcdefgh'):
        if len(seed) != 8:
            raise ValueError('Password must be 8 lowercase char')
        self._seed = seed
        self._current_password = None
#        
    def __iter__(self):
        return self
#    
    def __next__(self):
        if self.current_password() != None:
            p = Password.get_next_password(self._current_password)
        else:
            p = Password.get_next_password(self._seed)
        self._current_password = p
        return self._current_password
#                
    def current_password(self):
        return self._current_password
#        
    def next_password(self):
        return self.__next__()

    # Should skil iol here...
    @staticmethod
    def increment_letter(letter):
        letter = ord(letter)
        assert letter >= ord('a'), 'must be z or smaller: {0}'.format(letter)
        assert letter <= ord('z'), 'must bea or bigger: {0}'.format(letter)    
        letter += 1
        if letter > ord('z'):
            letter = ord('a')
        return chr(letter)

    @staticmethod
    def increment_word(word_to_increment):
        r_word = word_to_increment[::-1]
        for i, letter in enumerate(r_word):
            new_letter = Password.increment_letter(letter)
            r_word = r_word[:i] + new_letter + r_word[i+1:]
            if new_letter != 'a':
                break
        return r_word[::-1]

    @staticmethod
    def contains_sequence(word):
        for i, letter in enumerate(word):
            if i < 2:
                continue
            if (ord(word[i-2]) + 1)  == ord(word[i-1]):
                if (ord(word[i-1]) + 1) == ord(word[i]):
                    return True
        return False

    @staticmethod
    def contains_iol(word):
        pattern = r"i|o|l"
        if re.search(pattern, word):
            return True
        return False

    @staticmethod
    def contains_two_sets_of_overlap(word):
        pattern = r"(.)\1.*(.)\2"
        if re.search(pattern, word):
            return True
        return False

    @staticmethod
    def is_valid_password(word):
        if not Password.contains_iol(word):
            if Password.contains_sequence(word):
                if Password.contains_two_sets_of_overlap(word):
                    return True
        return False           

    @staticmethod    
    def get_next_password(seed):
        newword = seed        
        while True:
            newword = Password.increment_word(newword)
            if newword == seed:
                raise Exception('we tried everything... no more pwd')
            if Password.is_valid_password(newword):
                return newword            

#str = 'abcdefgh'
seed = 'hxbxwxba'
new_pass = 'hxbxxyzz'

password = Password(seed)
print(password.current_password())
print(password.next_password())

#
for i, pwd in enumerate(password):
    print(str(i) + ': ' + pwd)
    if  i > 5:
        break

print(password.current_password())
print(password.current_password())
print(password.next_password())
print(password.current_password())

value = Password.increment_word('zzzzzzzz')
print(value)
#answer 1 = hxbxxyzz

