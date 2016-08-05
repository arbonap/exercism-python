# # -*- coding: utf-8 -*-
# import string


# def is_pangram(phrase):

#     punctuation = string.punctuation

#     phrase = phrase.lower()
#     alphadict = {}

#     for char in phrase:
#         char = char.strip()
#         if char in punctuation:
#             continue

#         if char not in alphadict:
#             alphadict[char] = 1
#         else:
#             continue

#     if len(alphadict) >= 26:
#         return True
#     return False

def is_pangram(test_str):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return_state = True
    for i in range(0,len(alphabet)):
        return_state = return_state == (alphabet[i] in test_str.lower())
        if return_state == False:
            break
    return return_state