import re

with open('input.txt', 'r') as f:
    words = f.read().splitlines() 

def boolean_regex(func):
    def boolfunc(word):
        if func(word):
            return True
        else:
            return False
    return boolfunc

@boolean_regex
def contains_three_vowels(word):
    pattern = r"[aeiou].*[aeiou].*[aeiou]"
    return re.search(pattern, word)

@boolean_regex
def contains_double_letter(word):
    pattern = r"(.)\1"
    return re.search(pattern, word)
    
@boolean_regex
def has_forbidden_string(word):
    # ab, cd, pq, or xy
    pattern = r"(ab)|(cd)|(pq)|(xy)"
    return re.search(pattern, word)
    
@boolean_regex
def contains_double_pair(word):
    pattern = r"(..).*\1"
    return re.search(pattern, word)
    
@boolean_regex
def contains_double_letter_separated(word):
    pattern = r"(.).\1"
    return re.search(pattern, word)
        

def is_nice_word(word):
    is_nice = contains_three_vowels(word)   \
        & contains_double_letter(word)      \
        & (not has_forbidden_string(word))
    return is_nice
    
def is_nice_word_part_deux(word):
    is_nice = contains_double_pair(word)   \
        & contains_double_letter_separated(word)
    return is_nice
    
print contains_double_pair("ugknbfddgicrmopn")
print contains_double_pair("aaa")
print contains_double_pair("xyxy")
print contains_double_pair("aabcdefgaa")

# nice_words_count = 0
# for word in words:
    # if is_nice_word(word):
        # nice_words_count += 1
# print nice_words_count

nice_words_count = 0
for word in words:
    if is_nice_word_part_deux(word):
        nice_words_count += 1
print nice_words_count

# print contains_three_vowels("aei")
# print contains_three_vowels("xazegov")
# print contains_three_vowels("aeiouaeiouaeiou")
# print 
# print contains_three_vowels("aeb")
# print contains_three_vowels("dvszwmarrgswjxmb")
    
