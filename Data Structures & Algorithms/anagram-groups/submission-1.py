class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())

#GPT sol:
#from collections import defaultdict
#
#class Solution:
#    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#        anagrams = defaultdict(list)
#        for word in strs:
#            key = tuple(sorted(word))  # Use tuple instead of string
#            anagrams[key].append(word)
#        return list(anagrams.values())
#