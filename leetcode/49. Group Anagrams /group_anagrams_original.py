'''
original solution
	if two words appear the same after sorting its letters, then those words are anagrams
	approach is based around sorting the letters of the words to use as keys for a dictionary where the values are the original words
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_for_words = {}
        for word in strs:
            letters_sorted = tuple(sorted(word))
            if letters_sorted in letters_for_words:
                letters_for_words[letters_sorted].append(word)
            else:
                 letters_for_words[letters_sorted] = [word]
        return letters_for_words.values()

