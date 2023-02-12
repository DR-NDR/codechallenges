# the new solution is basically the same but with shorter variable names
# and using the get method from the dictionaries, to replace the if and else blocks
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            d[key] = d.get(key,[]) + [word]
        return d.values()            

